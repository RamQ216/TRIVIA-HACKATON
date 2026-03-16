puntos = 0
vidas = 3

def respuesta (respuesta_usuario, respuesta_correcta):
    puntos, vidas

    if respuesta_usuario == respuesta_correcta:
        puntos += 1
        print("Correcto Ganaste 1 punto.")
    else:
        vidas -= 1
        print("Incorrecto. Pierdes 1 vida.")

    print("Puntos:", puntos)
    print("Vidas restantes:", vidas)
