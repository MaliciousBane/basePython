import tkinter as tk
from tkinter import ttk
from controladorMenu import ControladorMenu

class VistaMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller = ControladorMenu(self)
        self.title("Vivero vital")
        self.geometry("800x400")
        self.configure(bg="white")

        # Encabezado
        header = tk.Frame(self, bg="lightgreen", height=40)
        header.pack(fill="x")
        tk.Label(header, text="Vivero vital", bg="lightgreen", font=("Arial", 14, "bold")).pack(side="left", padx=10)

        # Menú
        menu_frame = tk.Frame(self, bg="white")
        menu_frame.pack(pady=5)
        for texto in ["Registrar invernaderos", "Control invernaderos", "Control de humedad", "Control de piso", "Enfermedades"]:
            tk.Button(menu_frame, text=texto, bg="lightyellow", relief="groove", command=lambda t=texto: self.controller.navegar(t)).pack(side="left", padx=10)

        # Filtro
        filtro_frame = tk.Frame(self, bg="white")
        filtro_frame.pack(anchor="w", padx=20, pady=10)
        tk.Label(filtro_frame, text="Filtrar por:", bg="white").pack(side="left")
        opciones = ["Todos", "Las Flores", "Los Andes"]
        filtro_combobox = ttk.Combobox(filtro_frame, values=opciones, state="readonly")
        filtro_combobox.set("Todos")
        filtro_combobox.pack(side="left", padx=5)

        # Tarjetas
        self.cards_frame = tk.Frame(self, bg="white")
        self.cards_frame.pack()

        self.mostrar_tarjetas()

        # Footer
        footer = tk.Frame(self, bg="orange", height=20)
        footer.pack(side="bottom", fill="x")
        tk.Label(footer, text="Menu", bg="orange").pack(side="right", padx=10)

        self.mainloop()

    def mostrar_tarjetas(self):
        invernaderos = self.controller.obtener_datos_invernadero()
        for inv in invernaderos:
            self.crear_tarjeta(inv)

    def crear_tarjeta(self, inv):
        tarjeta = tk.Frame(self.cards_frame, bd=1, relief="solid", padx=30, pady=30)
        tarjeta.pack(side="left", padx=15)

        tk.Label(tarjeta, text=inv.nombre, font=("Arial", 12, "bold")).pack()

        campos = [
            ("Nombre del invernadero:", inv.nombre),
            ("Capacidad de producción:", inv.capacidad),
            ("Sistema de riego:", inv.sistema_riego),
            ("Usuario encargado:", inv.responsable),
        ]
        for campo, valor in campos:
            fila = tk.Frame(tarjeta)
            fila.pack(anchor="w")
            tk.Label(fila, text=campo).pack(side="left")
            tk.Entry(fila, width=20)

        tk.Label(tarjeta, text="[Imagen Invernadero]", fg="gray").pack(pady=5)

        botones = tk.Frame(tarjeta)
        botones.pack()
        tk.Button(botones, text="Guardar", bg="green", fg="white").pack(side="left", padx=5)
        tk.Button(botones, text="Cancelar", bg="red", fg="white").pack(side="left", padx=5)
