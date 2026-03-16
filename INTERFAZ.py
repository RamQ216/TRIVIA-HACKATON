import tkinter as tk

class VistaTrivia:
    def __init__(self, root, callback_tema):
        self.root = root
        self.root.title("Trivia de Datos Útiles")
        self.root.geometry("500x650")
        self.root.configure(bg="#F8F9FA")
        
        # Colores
        self.color_primario = "#4A90E2"
        self.color_blanco = "#FFFFFF"
        self.callback_tema = callback_tema
        
        self.mostrar_menu()

    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostrar_menu(self):
        self.limpiar_pantalla()
        
        tk.Label(
            self.root, text="SELECCIONA UNA TEMÁTICA", 
            font=("Segoe UI", 16, "bold"), bg="#F8F9FA", fg="#333333"
        ).pack(pady=50)

        # Usamos los nombres exactos que están en tu JSON actual
        temas = ["Programacion", "Economia", "Deporte"]
        for tema in temas:
            btn = tk.Button(
                self.root, text=tema, width=25, font=("Segoe UI", 12),
                bg=self.color_blanco, fg=self.color_primario,
                relief="flat", pady=15, cursor="hand2",
                command=lambda t=tema: self.callback_tema(t)
            )
            btn.pack(pady=10)
            # ... resto del código de binds ...
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#E3F2FD"))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=self.color_blanco))

    def preparar_interfaz_juego(self, callback_respuesta):
        self.limpiar_pantalla()
        
        # Encabezado de estadísticas
        self.frame_stats = tk.Frame(self.root, bg=self.color_blanco, pady=15, highlightthickness=1, highlightbackground="#E0E0E0")
        self.frame_stats.pack(fill="x")

        self.lbl_stats = tk.Label(self.frame_stats, text="", font=("Segoe UI", 12, "bold"), bg=self.color_blanco, fg=self.color_primario)
        self.lbl_stats.pack()

        # Tarjeta de Pregunta
        self.card = tk.Frame(self.root, bg=self.color_blanco, padx=25, pady=25, highlightthickness=1, highlightbackground="#DCE0E5")
        self.card.pack(pady=30, padx=25, fill="both")

        self.lbl_pregunta = tk.Label(self.card, text="", wraplength=380, font=("Segoe UI", 14), bg=self.color_blanco, fg="#333333", justify="center")
        self.lbl_pregunta.pack()

        # Botones de opciones
        self.botones = []
        for i in range(4):
            btn = tk.Button(
                self.root, text="", width=38, font=("Segoe UI", 11),
                bg=self.color_blanco, fg="#444444", relief="flat", pady=12, cursor="hand2",
                command=lambda i=i: callback_respuesta(self.botones[i].cget("text"), self.botones[i])
            )
            btn.pack(pady=8)
            self.botones.append(btn)

    def actualizar(self, pregunta_dict, vidas, puntos):
        corazones = "❤️" * vidas if vidas > 0 else "💀"
        self.lbl_stats.config(text=f"{corazones}   |   PUNTOS: {puntos}")
        self.lbl_pregunta.config(text=pregunta_dict["pregunta"], fg="#333333")
        for i, opcion in enumerate(pregunta_dict["opciones"]):
            self.botones[i].config(text=opcion, bg=self.color_blanco, state="normal", fg="#444444")

    def mostrar_curiosidad(self, texto):
        self.lbl_pregunta.config(text=f"¿SABÍAS QUE...?\n\n{texto}", fg=self.color_primario)
        for btn in self.botones:
            btn.config(state="disabled")