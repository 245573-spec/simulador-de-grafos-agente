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



def GetEmbedding(api_key: str) -> object | None:
    """
    Crea un generador de embeddings usando la API de Google Generative AI.

    Args:
        api_key (string): La clave API de Google.

    Returns:
        GoogleGenerativeAIEmbeddings: Objeto de embeddings configurado.
    """
    embending = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=api_key
    )

    return embending
