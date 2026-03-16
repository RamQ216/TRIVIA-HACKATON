import tkinter as tk
from datos import cargar_preguntas
from logica import MotorJuego
from interfaz import VistaTrivia
from efectos import ManejadorSonidos

def manejar_respuesta(texto_boton, boton_presionado):
    # Bloqueo inmediato para evitar clics múltiples durante la curiosidad
    for btn in vista.botones:
        btn.config(state="disabled")

    es_correcta = motor.validar_respuesta(texto_boton)
    
    if es_correcta:
        boton_presionado.config(bg="#4CAF50", fg="white", state="disabled") 
        efectos.reproducir("acierto")
        if motor.puntuacion == 30:
            efectos.reproducir("record")
    else:
        boton_presionado.config(bg="#E53935", fg="white", state="disabled")
        efectos.reproducir("error")

    # Obtener curiosidad de forma segura
    curiosidad = motor.obtener_pregunta_actual().get("curiosidad", "¡Sigue aprendiendo!")
    vista.mostrar_curiosidad(curiosidad)
    
    root.after(3000, siguiente_paso)
def siguiente_paso():
    if motor.tiene_mas_preguntas():
        motor.indice += 1
        vista.actualizar(motor.obtener_pregunta_actual(), motor.vidas, motor.puntuacion)
    else:
        import tkinter.messagebox as mb
        mb.showinfo("Fin", f"¡Trivia Terminada!\nPuntos: {motor.puntuacion}")
        root.destroy()

root = tk.Tk()
preguntas = cargar_preguntas()
motor = MotorJuego(preguntas)
efectos = ManejadorSonidos()
vista = VistaTrivia(root, manejar_respuesta)
vista.actualizar(motor.obtener_pregunta_actual(), motor.vidas, motor.puntuacion)
root.mainloop()