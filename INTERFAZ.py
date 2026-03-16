import tkinter as tk

class VistaTrivia:
    def __init__(self, root, callback_respuesta):
        self.root = root
        self.root.title("Trivia de Datos Útiles")
        self.root.geometry("500x650")
        self.root.configure(bg="#F8F9FA")
        
        # Paleta de colores
        self.color_primario = "#4A90E2"
        self.color_blanco = "#FFFFFF"

        # 1. DEFINICIÓN DE LBL_STATS (Debe estar aquí dentro)
        self.frame_stats = tk.Frame(root, bg=self.color_blanco, pady=15, highlightthickness=1, highlightbackground="#E0E0E0")
        self.frame_stats.pack(fill="x")

        self.lbl_stats = tk.Label(
            self.frame_stats, 
            text="", 
            font=("Segoe UI", 12, "bold"), 
            bg=self.color_blanco, 
            fg=self.color_primario
        )
        self.lbl_stats.pack()

        # Contenedor de la Pregunta
        self.card = tk.Frame(root, bg=self.color_blanco, padx=25, pady=25, highlightthickness=1, highlightbackground="#DCE0E5")
        self.card.pack(pady=30, padx=25, fill="both")

        self.lbl_pregunta = tk.Label(
            self.card, 
            text="", 
            wraplength=380, 
            font=("Segoe UI", 14), 
            bg=self.color_blanco, 
            fg="#333333",
            justify="center"
        )
        self.lbl_pregunta.pack()

        # Botones
        self.botones = []
        for i in range(4):
            btn = tk.Button(
                root, 
                text="", 
                width=38, 
                font=("Segoe UI", 11),
                bg=self.color_blanco,
                fg="#444444",
                relief="flat",
                pady=12,
                cursor="hand2",
                command=lambda i=i: callback_respuesta(self.botones[i].cget("text"), self.botones[i])
            )
            btn.pack(pady=8)
            self.botones.append(btn)

    def actualizar(self, pregunta_dict, vidas, puntos):
        # Ahora self.lbl_stats sí existirá para el programa
        corazones = "❤️" * vidas if vidas > 0 else "💀"
        self.lbl_stats.config(text=f"{corazones}   |   PUNTOS: {puntos}")
        self.lbl_pregunta.config(text=pregunta_dict["pregunta"], fg="#333333")
        
        for i, opcion in enumerate(pregunta_dict["opciones"]):
            self.botones[i].config(text=opcion, bg=self.color_blanco, state="normal", fg="#444444")

    def mostrar_curiosidad(self, texto):
        self.lbl_pregunta.config(text=f"¿SABÍAS QUE...?\n\n{texto}", fg=self.color_primario)
        for btn in self.botones:
            btn.config(state="disabled")
