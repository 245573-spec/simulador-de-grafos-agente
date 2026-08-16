from flask import Blueprint, jsonify,request
from Service import RAG


#Creamos una ruta con flask
#Blueprint permite definir rutas en modulos
ChatBot = Blueprint("ChatBot",__name__)

#End-point que ejecuta el Metodo de http POST

@ChatBot.route("/api/v1/consulta", methods=["POST"])
def PostData():
    """
    Endpoint POST que recibe una consulta del usuario y devuelve una respuesta generada por el modelo RAG.

    Este endpoint espera una solicitud JSON con el siguiente formato:
    {
        "consulta": "¿Cuál es el contenido del documento?"
    }

    Procesos que realiza:
    1. Extrae el campo 'consulta' del cuerpo JSON.
    2. Pasa la pregunta al método `RAG.RagMain()` para obtener la respuesta.
    3. Retorna un JSON con la respuesta generada.

    Returns:
        Response: Objeto JSON con la clave 'respuesta' conteniendo el texto generado.
    """
    data = request.get_json()
    respuesta = RAG.RagMain(data["consulta"])
    return jsonify({"respuesta": respuesta})

