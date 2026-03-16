class MotorJuego:
    def __init__(self, lista_preguntas):
        self.preguntas = lista_preguntas
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
        # Permitimos avanzar si el índice actual aún no es el último
        return self.indice < len(self.preguntas) - 1 and self.vidas > 0
