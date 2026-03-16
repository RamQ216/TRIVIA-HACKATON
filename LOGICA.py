import unicodedata

def normalizar(texto):
    """Elimina tildes y convierte a minúsculas para comparar correctamente."""
    if not texto: return ""
    return "".join(
        c for c in unicodedata.normalize('NFD', str(texto))
        if unicodedata.category(c) != 'Mn'
    ).lower().strip()

class MotorJuego:
    def __init__(self, lista_preguntas, tematica):
        tema_buscado = normalizar(tematica)
        # Filtramos comparando ambas versiones normalizadas
        self.preguntas = [
            p for p in lista_preguntas 
            if normalizar(p.get("categoria", "")) == tema_buscado
        ]
        self.puntuacion = 0
        self.vidas = 3
        self.indice = 0

    def obtener_pregunta_actual(self):
        return self.preguntas[self.indice]

    def validar_respuesta(self, respuesta_usuario):
        correcta = self.preguntas[self.indice]["correcta"]
        if respuesta_usuario == correcta:
            self.puntuacion += 10
            return True
        else:
            self.vidas -= 1
            return False

    def tiene_mas_preguntas(self):
        # Corregido para que permita llegar a la última pregunta correctamente
        return (self.indice + 1) < len(self.preguntas) and self.vidas > 0