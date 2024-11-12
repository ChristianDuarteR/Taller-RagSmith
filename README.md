# RagServer: Implementación del Tutorial y Proyecto

En este repositorio **Taller-RagSmith**! se muestra cómo integrar la arquitectura de **RAG APP** para crear una **LLM Chain** (Large Language Model Chain) en un entorno seguro e implementando 
un RAG (Retrieval Augmented Generation)

## 🚀 Descripción del Proyecto

Este proyecto implementa el tutorial [LLM Chain]([https://python.langchain.com/docs/tutorials/llm_chain/](https://python.langchain.com/docs/tutorials/rag/)) y lo integra con cualquier tema de interes
, En mi caso lo implemente con generos musicales. 

## 📂 Estructura del Repositorio

```plaintext
ragSimpleApp.ipynb
ragServer.py
└── README.md
```

### Requisitos Previos

Para ejecutar este proyecto, necesitarás tener instalado:

- Python.
- Un IDE de Python de su preferencia.
- Un navegador web para interactuar con el servidor y la API.

### Instalación

1. Tener instalado Git en tu máquina local.
2. Elegir una carpeta en donde guardar el proyecto.
3. Abrir la terminal de GIT (ccho y seleccionar "Git bash here").
4. Clonar el repositorio en tu máquina local:lic dere
   ```bash
   git clone https://github.com/ChristianDuarteR/Taller-RagSmith
5. Instalar un ambiente virtual de python, para que jupyter notebook pueda correr todas las dependencias

6. Proporcione el API Key en las variable que se encuentran vacias sobre los archivos
   - ragSimpleApp
   - ragServer
   Esto es importante para que La Api y el servidor puedan utilizar el modelo de lenguaje OpenIA

   
### Deployment

1. Abre el proyecto con tu IDE favorito o navega hasta el directorio del proyecto.
2. Ejecute todos los comandos del archivo jupyter Notebook (Asegurese de tener un ambiente virtual instalado previamente)
![image](https://github.com/user-attachments/assets/969cedb0-4365-464c-9cad-ee29349e55eb)

4. Desde la terminal, ejectuta los dos archivos de python
     ```bash
   python ragServer.py
5. El servidor iniciara
   ![image](https://github.com/user-attachments/assets/ddccecf0-e174-4988-9fc5-eecdd4068864)
     
6. Es posible interactuar con la aplicacion en el puerto (http:localhost:8000/docs y ver los endpoitns disponibles)
   ![image](![image](https://github.com/user-attachments/assets/d2039e7e-da6b-49c7-b92f-43a95b40e568)
)
   

  
### IMPORTANTE:

Es importante contar con un APIKEY, tanto en el servidor como en la API se deja uan variable vacia en donde deberia estar, sino se proporciona la aplicacion no servira

![image](https://github.com/user-attachments/assets/7081e72a-9570-4e4f-acfb-4ec8ff293408)

## Arquitectura

### Servidor

El Servidor RAG se alimente de la pagina HTML que describe un top de generos musicales y los explica y adapta una implementacion sencilla para que realize una peticion a la API de una pregunta acerca de los generos musicales
![image](https://github.com/user-attachments/assets/b0f22e69-d122-4855-a9dd-2d937016270d)

Seguidamente se puede hcar cuaqluier pregunta y la implementacion respondera segun su conocimiento como en este ejemplo
![image](https://github.com/user-attachments/assets/31b2b2c4-2e2c-498c-ae91-2c7a739b8abf)


### Api 

La API se alimenta de la informacion HTML importante en el documento proporcionado para poder responder en el endpoint - POST /ask
