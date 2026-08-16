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

sys.path.append(os.path.abspath("Config"))
import Service.Config as cf


class LLM:
    @classmethod 
    def GenerateSearch(cls, consulta: str, qdrant: QdrantVectorStore, k: int = 5) -> str:
        """
        Realiza una búsqueda semántica usando el motor de embeddings (Qdrant).

        Args:
            consulta (str): La consulta o pregunta del usuario.
            qdrant (QdrantVectorStore): El vectorstore Qdrant previamente configurado.
            k (int, opcional): Número de documentos similares a recuperar. Por defecto es 5.

        Returns:
            str: Texto concatenado de los fragmentos encontrados con su fuente.
        """
        s = ""
        fragmentos = qdrant.similarity_search(consulta, k)

        for fragmento in fragmentos:
            # Uso de comillas simples internas para evitar SyntaxError en el f-string
            fuente = fragmento.metadata.get('source', 'Desconocida')
            s += f"Fuente : {fuente}\n"
            s += fragmento.page_content + "\n\n"

        return s

    @classmethod
    def GetMemory(cls, historial: list) -> list:
        """
        Construye la memoria conversacional previa para alimentar el modelo LLM.

        Args:
            historial (list): Lista de tuplas [(usuario, respuesta_modelo), ...] representando el diálogo.

        Returns:
            list: Lista de mensajes estructurados para el modelo GenAI.
        """
        cola = deque(maxlen=cf.MEMORIA)

        for usuario, bot in historial:
            cola.append({
                "role": "user",
                "parts": [usuario]
            })
            cola.append({
                "role": "model",
                "parts": [bot]
            })
        
        mensajes = list(cola)

        mensajes.insert(0, {
            "role": "user",
            "parts": [cf.PROMPT_SISTEMA]
        })

        return mensajes