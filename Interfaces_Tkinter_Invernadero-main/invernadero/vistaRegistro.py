import tkinter as tk
from tkinter import ttk
from controladorRegistro import controladorRegistro

class Registro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.controller = controladorRegistro(self)
        self.title("Registrar Invernadero")
        self.geometry("680x420")
        self.configure(bg="white")

        # Encabezado
        header = tk.Frame(self, bg="lightgreen", height=40)
        header.pack(fill="x")
        tk.Label(header, text="Vivero vital", bg="lightgreen", font=("Arial", 14, "bold")).pack(side="left", padx=10)

        # Contenedor principal
        main_frame = tk.Frame(self, bg="white")
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Columna izquierda del formulario
        form_left = tk.Frame(main_frame, bg="white")
        form_left.pack(side="left", padx=10, pady=10)

        self.entry_nombre = self._crear_entrada(form_left, "Nombre del invernadero")
        self.entry_superficie = self._crear_entrada(form_left, "Superficie (m²)")
        self.entry_cultivo = self._crear_combo(form_left, "Tipo de cultivo", ["Flores", "Frutas", "Verduras"])
        self.entry_fecha = self._crear_entrada(form_left, "Fecha de creación")
        self.entry_responsable = self._crear_entrada(form_left, "Responsable del invernadero")

        # Columna derecha del formulario
        form_right = tk.Frame(main_frame, bg="white")
        form_right.pack(side="left", padx=10, pady=10)

        self.entry_capacidad = self._crear_entrada(form_right, "Capacidad de producción")
        self.entry_riego = self._crear_combo(form_right, "Sistema de riego", ["Manual", "Automatizado", "Por goteo"])

        # Botones guardar/cancelar
        button_frame = tk.Frame(form_right, bg="white")
        button_frame.pack(pady=15)

        tk.Button(button_frame, text="Guardar", bg="green", fg="white", font=("Arial", 10, "bold"),
                  command=self.controller.guardar, width=10).pack(side="left", padx=5)

        tk.Button(button_frame, text="Cancelar", bg="red", fg="white", font=("Arial", 10, "bold"),
                  command=self.destroy, width=10).pack(side="left", padx=5)

        # Label simulando imagen
        imagen_simulada = tk.Label(main_frame, text="Vista del\ninvernadero", bg="lightgray", width=25, height=12,
                                   relief="solid", borderwidth=1, font=("Arial", 10, "italic"), justify="center")
        imagen_simulada.pack(side="left", padx=20)

        # Botón regresar flotante
        tk.Button(self, text="Regresar", bg="green", fg="white", command=self.controller.regresar).place(x=550, y=360)

        # Footer
        footer = tk.Frame(self, bg="orange", height=20)
        footer.pack(side="bottom", fill="x")
        tk.Label(footer, text="Registrar invernadero", bg="orange", fg="black").pack(side="right", padx=10)

        self.mainloop()

    def _crear_entrada(self, parent, label_text):
        tk.Label(parent, text=label_text, bg="white", anchor="w", font=("Arial", 9, "bold")).pack(fill="x")
        entry = tk.Entry(parent, bg="#eaf7e4", relief="solid", borderwidth=1)
        entry.pack(fill="x", pady=4)
        return entry

    def _crear_combo(self, parent, label_text, values):
        tk.Label(parent, text=label_text, bg="white", anchor="w", font=("Arial", 9, "bold")).pack(fill="x")
        combo = ttk.Combobox(parent, values=values)
        combo.pack(fill="x", pady=4)
        return combo
