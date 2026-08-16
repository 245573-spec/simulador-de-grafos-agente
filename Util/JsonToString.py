import json

def JsonToString(jsondata:json) -> str|None:
    """
    Convierte una cadena JSON a un diccionario de Python y devuelve el valor de la clave 'consulta'.

    Args:
        jsondata (str): Cadena JSON que contiene al menos la clave 'consulta'.

    Returns:
        str: El valor asociado a la clave 'consulta'.

    """


    dato = json.loads(jsondata)
    return dato["consulta"]