import os
import sys
from collections import deque
from dotenv import load_dotenv

from langchain_community.document_loaders.text import TextLoader
from langchain_community.document_loaders import PyPDFLoader, CSVLoader

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from langchain_qdrant import QdrantVectorStore
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_text_splitters import RecursiveCharacterTextSplitter


def CreateQdrant(Base_datos: QdrantClient, collection_name: str, embedding) -> QdrantVectorStore:
    """
    Crea una instancia del vector store Qdrant para gestionar búsquedas semánticas.

    Args:
        Base_datos (QdrantClient): Cliente conectado al servicio Qdrant.
        collection_name (str): Nombre de la colección en Qdrant.
        embedding (Embeddings): Objeto de embeddings para convertir textos a vectores.

    Returns:
        QdrantVectorStore: Instancia de vector store Qdrant lista para operaciones.
    """
    qdrant = QdrantVectorStore(
        client=Base_datos,
        collection_name=collection_name,
        embedding=embedding  # Parámetro en singular para la versión actualizada
    )

    return qdrant