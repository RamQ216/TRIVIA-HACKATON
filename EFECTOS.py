import pygame
import os

class ManejadorSonidos:
    def __init__(self):
        pygame.mixer.init()
        # Nombres extraídos de tu captura de pantalla
        self.sonidos = {
            "acierto": "assets/universfield-new-notification-037-485898.mp3",
            "error": "assets/u_8iuwl7zrk0-error-170796.mp3",
            "record": "assets/driken5482-applause-cheer-236786.mp3"
        }

    def reproducir(self, tipo):
        ruta = self.sonidos.get(tipo)
        if ruta and os.path.exists(ruta):
            try:
                # Nota: pygame.mixer.Sound puede ser caprichoso con MP3 largos. 
                # Si falla, el bloque try-except evitará que el juego se cierre.
                pygame.mixer.Sound(ruta).play()
            except:
                    pass