import json
import random

def cargar_preguntas():
    try:
        with open('PREGUNTAS.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            random.shuffle(data) # Mezcla el orden de las preguntas
            return data
    except FileNotFoundError:
        # Preguntas de respaldo por si no encuentran el archivo
        return [{"pregunta": "Error: PREGUNTAS.json no encontrado", 
                "opciones": ["A", "B", "C", "D"], "correcta": "A"}]