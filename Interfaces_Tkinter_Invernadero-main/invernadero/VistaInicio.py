import tkinter as tk
from tkinter import messagebox
from controladorInicio import controladorInicio

class VistaInicio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller = controladorInicio(self)
        self.title("Vivero Vital - Login")
        self.geometry("500x300")
        self.configure(bg="white")

        header = tk.Frame(self, bg="green", height=40)
        header.pack(fill="x")
        tk.Label(header, text="Vivero vital", bg="green", fg="black", font=("Arial", 12, "bold")).pack(side="left", padx=10)        

        tk.Label(self, text="Iniciar Sesión", font=("Arial", 40)).pack(pady=30)

        self.entry_usuario = tk.Entry(self, width=25,bg="lightyellow")
        self.entry_usuario.pack(pady=2)
        
        self.entry_clave = tk.Entry(self, width=25, show="●",bg="lightyellow")
        self.entry_clave.pack(pady=2)

        self.btn_confirmar = tk.Button(self, text="Confirmar", command=self.controller.validar_login)
        self.btn_confirmar.pack(pady=10)

        footer = tk.Frame(self, bg="orange", height=30)
        footer.pack(side="bottom", fill="x")

        self.mainloop()