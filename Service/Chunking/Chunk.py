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

sys.path.append(os.path.abspath("Config"))

import Service.Config as cf

path = os.path.join(os.getcwd(), "Doc")


def GetChunk(archivos) -> list | None:
    """
    Divide una lista de documentos en fragmentos mas pequeños para su uso en el RAG

    Args:
        archivos(list()): Lista de documentos Laingchain

    Returns:
        chunks(list()): Lista de chunk (fragmentos de los documentos)
    """
    Text_Spliter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 150,
    )
    #se queda
    chunks =  Text_Spliter.split_documents(archivos)

    return chunks