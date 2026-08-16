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



class ConfigApi():
    @classmethod
    def ConfigGenai(cls, apikey:str) -> object | None:
        """
        Este metodo se encarga de configuar el cliente de Genai con la API key

        Args:
            apikey(string) : La API key

        Returns:
            client(object) : Retorna un cliente de Genai

        """
        genai.configure(api_key=apikey)

        client = genai.GenerativeModel(
            model_name="gemini-1.5-flash"
        )

        return client
    @classmethod
    def ConfigQdrant(cls, urlQdrant : str, apikeyQdrant : str) -> object | None:
        """
        Este metodo se encarga de configuar el cliente de Qdrant con la API key

        Args:
            urlQdrant(string): La url del end-point de cluster de Qdrant
            apikeyQdrant(string) : La API key

        Returns:
            client(object) : Retorna un cliente de Genai

        """
        client = QdrantClient(
            url=urlQdrant,
            api_key=apikeyQdrant
        )
        return client