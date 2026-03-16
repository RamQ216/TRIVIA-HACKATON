import json
import random
import os

def cargar_preguntas():
    # Buscamos el archivo con el nombre exacto que confirmaste
    archivo = 'PREGUNTAS.JSON'
    
    if not os.path.exists(archivo):
        print(f"Error: No se encuentra el archivo {archivo}")
        return []

    try:
        # Usamos utf-8-sig para evitar problemas con carácteres invisibles de Windows
        with open(archivo, 'r', encoding='utf-8-sig') as f:
            data = json.load(f)
            random.shuffle(data)
            return data
    except Exception as e:
        print(f"Error al leer el JSON: {e}")
        return []