from Service.Api_or_Url import GetApi
from Service.Api_or_Url import GetUrl
from Service.Api_or_Url import ConfigApi

from Service.Chunking import Ids
from Service.Chunking import LoadDocuments
from Service.Chunking import Chunk

from Service.Embendings import Embendder

from Service.Generator import LLM

from Service.Prompts import CreatePrompt

from Service.Vectorstore import SetupQdran
from Service.Vectorstore import VectorConnection
import os
import sys
sys.path.append(os.path.abspath("Service/Config"))
import Service.Config as cf



#Obtenmos las API Key
ApiGoogle = GetApi.GetApi.ApiGenai()
ApiQdrant = GetApi.GetApi.ApiQdrant()

#Obtenemos la Url de Qdrant
UrlQdrant = GetUrl.GetUrl.UrlQdrant()

#Fragmentamos los documentos
archivos = LoadDocuments.LoadAll()

#Creamos los chunks 
chunks = Chunk.GetChunk(archivos)

#Creamos una lista de ids para cada chunk
ids = Ids.CreateId(chunks)

#Creamos un cliente configurado de Genai
clienteGenai = ConfigApi.ConfigApi.ConfigGenai(ApiGoogle)

#Creamos un cliente configurado de Qdrant
clienteQdrant = ConfigApi.ConfigApi.ConfigQdrant(UrlQdrant,ApiQdrant)

#Creamos los embeddings
embeddings = Embendder.GetEmbedding(ApiGoogle)

#Cramos un collection name para Qdrant
collection_name = SetupQdran.Setup(clienteQdrant)

#Creamos una instancia de Qdrant
Qdrant = VectorConnection.CreateQdrant(clienteQdrant,collection_name,embeddings)

#Cargamos los chunks a nuestra vase de datos vectorizada
Qdrant.add_documents(documents = chunks, ids = ids)

#Creamos una consulta

mem = []

def RagMain(pregunta: str) -> str:
    """
    Ejecuta el flujo principal de RAG (Retrieval-Augmented Generation) para una pregunta del usuario.

    Este método:
    1. Agrega la pregunta al historial de memoria (`mem`) como parte del rol "user".
    2. Genera una respuesta usando la función `CreatePrompt.Prompt`, pasando la pregunta, la memoria, la conexión a Qdrant y el cliente GenAI.
    3. Imprime la respuesta en consola (para depuración).
    4. Agrega la respuesta generada al historial como parte del rol "model".
    5. Devuelve la respuesta como cadena.

    Args:
        pregunta (str): Pregunta ingresada por el usuario.

    Returns:
        str: Respuesta generada por el modelo de lenguaje.
    """
    mem.append({
        "role":"user",
        "parts":pregunta
    })

    respuesta = CreatePrompt.Prompt(pregunta,mem,Qdrant,clienteGenai)

    
    mem.append({    
        "role":"model",
        "parts":respuesta
    })
    return respuesta




# end-point (POST)=  ingresar_consulta
"""
{
    consulta : "Mensaje"(valor),
}
"""