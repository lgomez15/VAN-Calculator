import json

def load_data(file_path):
    """
    Carga el archivo JSON y devuelve los datos.
    
    Args:
        file_path (str): Ruta al archivo JSON.
        
    Returns:
        dict: Los datos cargados desde el archivo JSON.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data