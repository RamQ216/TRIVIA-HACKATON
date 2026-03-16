import tkinter as tk
from tkinter import messagebox
from DATOS import cargar_preguntas
from LOGICA import MotorJuego
from INTERFAZ import VistaTrivia
from EFECTOS import ManejadorSonidos

def elegir_tematica(tema):
    global motor
    preguntas_totales = cargar_preguntas()
    
    if not preguntas_totales:
        messagebox.showerror("Error de Archivo", "No se pudo cargar PREGUNTAS.JSON.\nVerifica que el archivo esté en la misma carpeta.")
        return

    motor = MotorJuego(preguntas_totales, tema)
    
    if not motor.preguntas:
        messagebox.showwarning("Aviso", f"No se encontraron preguntas para la categoría: {tema}")
        return

    vista.preparar_interfaz_juego(manejar_respuesta)
    vista.actualizar(motor.obtener_pregunta_actual(), motor.vidas, motor.puntuacion)

def manejar_respuesta(texto_boton, boton_presionado):
    # Desactivamos botones para evitar múltiples clics
    for btn in vista.botones:
        btn.config(state="disabled")

    es_correcta = motor.validar_respuesta(texto_boton)
    
    if es_correcta:
        boton_presionado.config(bg="#4CAF50", fg="white")
        efectos.reproducir("acierto")
        if motor.puntuacion >= 30:
            efectos.reproducir("record")
    else:
        boton_presionado.config(bg="#E53935", fg="white")
        efectos.reproducir("error")

    curiosidad = motor.obtener_pregunta_actual().get("curiosidad", "¡Dato interesante!")
    vista.mostrar_curiosidad(curiosidad)
    root.after(3000, siguiente_paso)

def siguiente_paso():
    if motor.tiene_mas_preguntas():
        motor.indice += 1
        vista.actualizar(motor.obtener_pregunta_actual(), motor.vidas, motor.puntuacion)
    else:
        msg = "¡Juego Terminado!" if motor.vidas > 0 else "¡Te has quedado sin vidas!"
        messagebox.showinfo("Fin", f"{msg}\nPuntos finales: {motor.puntuacion}")
        vista.mostrar_menu()

root = tk.Tk()
efectos = ManejadorSonidos()
vista = VistaTrivia(root, elegir_tematica)
root.mainloop()