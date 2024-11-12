#!/usr/bin/env python
import os
import bs4
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

# Configuración de la clave API
os.environ["OPENAI_API_KEY"] = ""

# Configuración de FastAPI
app = FastAPI(
    title="RAG LangChain Server",
    version="1.0",
    description="A server combining LangChain RAG functionality with FastAPI",
)

# Modelo para solicitudes
class QueryRequest(BaseModel):
    question: str

# Modelo para respuestas
class QueryResponse(BaseModel):
    answer: str

# Configurar el LLM
llm = ChatOpenAI(model="gpt-4o-mini")

# Función para cargar y procesar documentos
def initialize_rag():
    # Cargar documentos desde la web
    loader = WebBaseLoader(
        web_paths=["https://www.significados.com/generos-musicales/"],
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                name=["p", "ul", "ol", "table"]  # Incluye párrafos, listas y tablas
            )
        ),
    )
    docs = loader.load()


    # Dividir los documentos en chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    # Crear un vectorstore para la búsqueda
    vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

    # Configurar el flujo de RAG
    retriever = vectorstore.as_retriever()

    # Crear la plantilla del sistema
    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the "
        "answer concise."
        "\n\n"
        "{context}"
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, question_answer_chain)

# Inicializar la cadena de RAG
rag_chain = initialize_rag()

# Endpoint para responder preguntas
@app.post("/ask", response_model=QueryResponse)
async def ask_question(request: QueryRequest):
    try:
        # Ejecutar la cadena de RAG con la pregunta
        response = rag_chain.invoke({"input": request.question})
        return QueryResponse(answer=response["answer"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Ejecución del servidor
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)