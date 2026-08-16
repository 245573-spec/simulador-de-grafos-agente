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

class GetUrl():
    @classmethod
    def UrlQdrant(cls) -> str| None:
        """
        Este metodo retorna la url del end-point del cluster de Qdrant

        Args:
            No recibe argumentos

        Returns:
            str | None: La URL del endpoint, o None si no se encuentra definida.
        """

        load_dotenv()
        url = os.getenv("Url_Qrandt_endpoint")
        if url is None:
            print("❌ Url no encontrada. Verifica el .env.")
        else:
            print("✅ Url cargada correctamente.")
            return url