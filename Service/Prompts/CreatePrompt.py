import os
import sys
import re
from collections import deque
from dotenv import load_dotenv

from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from langchain_qdrant import QdrantVectorStore
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

sys.path.append(os.path.abspath("Config"))
import Service.Config as cf
from Service.Generator.LLM import LLM


def markdown_to_html(text: str) -> str:
    """
    Convierte Markdown básico a HTML: listas con '*', negritas con '**', y saltos de línea.
    """
    # Negrita **texto**
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)

    # Listas: líneas que empiezan con '* '
    lines = text.splitlines()
    html_lines = []
    inside_ul = False

    for line in lines:
        if re.match(r'^\* ', line.strip()):
            if not inside_ul:
                html_lines.append('<ul>')
                inside_ul = True
            item = line.strip()[2:]
            html_lines.append(f'<li>{item}</li>')
        else:
            if inside_ul:
                html_lines.append('</ul>')
                inside_ul = False
            html_lines.append(line)

    if inside_ul:
        html_lines.append('</ul>')

    return '<br>'.join(html_lines)


def Prompt(
    pregunta: str, 
    historial: list, 
    vector_store: QdrantVectorStore, 
    model: genai.GenerativeModel
) -> str | None:
    """
    Genera una respuesta basada en la arquitectura RAG (Retrieval-Augmented Generation).

    Args:
        pregunta (str): Pregunta o consulta del usuario.
        historial (list): Lista de interacciones anteriores en formato [(usuario, respuesta_modelo), ...].
        vector_store (QdrantVectorStore): Instancia de Qdrant para la búsqueda de vectores.
        model (genai.GenerativeModel): Instancia del modelo de Gemini configurada.

    Returns:
        str | None: Respuesta generada por el modelo formateada en HTML.
    """
    # 1. Obtener la memoria previa conversacional
    mensaje_historial = LLM.GetMemory(historial)
    
    # 2. Recuperar el contexto de la base de datos vectorial
    contexto = LLM.GenerateSearch(pregunta, vector_store, k=cf.DOCUMENTOS)

    # 3. Construir el prompt RAG
    prompt_final = f"""
    Pregunta: {pregunta}
    Contexto: {contexto}
    Instrucción: Siempre responde en el mismo idioma de la pregunta.
    """

    # 4. Iniciar el chat pasando la historia existente
    chat = model.start_chat(history=mensaje_historial)

    # 5. Enviar el prompt actual y recibir respuesta
    respuesta = chat.send_message(prompt_final)

    # 6. Extraer el texto devuelto por el modelo
    texto_respuesta = respuesta.text

    # 7. Convertir a HTML estructurado
    respuesta_html = markdown_to_html(texto_respuesta)

    return respuesta_html