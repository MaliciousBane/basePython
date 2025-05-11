import tkinter as tk
from controladorControlInventario import ControlInventario

class VistaControlInventario(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller = ControlInventario(self)
        self.title("Lista de Invernaderos")
        self.geometry("670x430")
        self.configure(bg="white")

        header = tk.Frame(self, bg="lightgreen", height=40)
        header.pack(fill="x")
        tk.Label(header, text="Vivero vital", bg="lightgreen", font=("Arial", 14, "bold")).pack(side="left", padx=10)

        self.contenedor_central = tk.Frame(self, bg="white")
        self.contenedor_central.pack(expand=True)

        self.controller.cargar_invernaderos()

        tk.Button(self, text="Regresar", bg="lightgreen", fg="white", command=self.controller.regresar).place(x=550, y=360)

        footer = tk.Frame(self, bg="orange", height=20)
        footer.pack(side="bottom", fill="x")
        tk.Label(footer, text="Control invernadero", bg="orange", fg="black").pack(side="right", padx=10)

        self.mainloop()


    def mostrar_invernaderos(self, invernaderos):
        for nombre, estado in invernaderos:
            fila = tk.Frame(self.contenedor_central, bg="white", pady=8)
            fila.pack()

            tk.Label(fila, text=nombre, width=25, bg="lightgray", font=("Arial", 10)).pack(side="left", padx=5)
            tk.Label(fila, text=estado, bg="#f4f4c2", width=12, font=("Arial", 10, "bold")).pack(side="left", padx=5)
            tk.Button(fila, text="Editar", bg="#f9f9dd", width=10, command=lambda n=nombre: self.controller.editar(n)).pack(side="left", padx=2)
            tk.Button(fila, text="Eliminar", bg="#f9f9dd", width=10, command=lambda n=nombre: self.controller.eliminar(n)).pack(side="left", padx=2)
            tk.Button(fila, text="Detalles", bg="orange", width=10, command=lambda n=nombre: self.controller.detalles(n)).pack(side="left", padx=2)