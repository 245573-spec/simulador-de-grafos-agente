
def CreateId(chunks) -> list | None:
    """
    Crea una lista de ids para los chunks

    Args:
        chunks(list()): Lista de archivos fragmentados

    Returns:
        ids(list()) : Lista de ids en el orde de los chuks en la lista chunks
    """

    ids = list()

    for i, chunk in enumerate(chunks):
        ids.append(i)

    return ids