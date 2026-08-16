from langchain_community.document_loaders.text import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import CSVLoader

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from langchain_qdrant import QdrantVectorStore
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

from langchain_text_splitters import RecursiveCharacterTextSplitter

from collections import deque


import os
import sys



def Setup(Base_datos:object) -> str | None:

    """
    Crea una colección en Qdrant si no existe, sino retonar el nombre de la coleccion.

    Args:
        Base_datos(QdrantClient): Cliente de conexión a la base de datos Qdrant.

    Returns:
        collection_name(str): Nombre de la colección utilizada.
    """

    collection_name = "embedding_data"
    if not Base_datos.collection_exists(collection_name):
        Base_datos.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=1500,      
                distance=Distance.COSINE
            )
        )

    return collection_name

