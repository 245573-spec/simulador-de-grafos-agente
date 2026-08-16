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


class GetApi():
    @classmethod
    def ApiGenai(cls) -> str| None:
        """
        Esta funcion recura la API Key de la IA de GOOGLE, Genai

        Args:
            No recibe parametros

        Retunrs:
            api_key(str): La Api key
        """
        
        load_dotenv()

        api_key = os.getenv("Api_key_Google")

        if api_key is None:
            print("❌ Clave no encontrada. Verifica el .env.")
        else:
            print("✅ API key cargada correctamente.")
            return api_key
        
    @classmethod
    def ApiQdrant(cls) -> str| None:

        """
        Esta funcion recura la API Key de la IA de la base de datos Vectorizada, Qdrant

        Args:
            No recibe parametros

        Retunrs:
            api_key(str): La Api key
            

        """

        load_dotenv()

        api_key = os.getenv("Api_key_Qdrant")

        if api_key is None:
            print("❌ Clave no encontrada. Verifica el .env.")
        else:
            print("✅ API key cargada correctamente.")
            return api_key
        

