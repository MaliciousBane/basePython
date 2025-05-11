import tkinter as tk

# Lista de invernaderos con estado
invernaderos = [
    ("Invernadero Los Andes", "Operativo"),
    ("Invernadero Las Flores", "Reparación"),
    ("Invernadero Los Pinos", "Inspección"),
    ("Invernadero El Mirador", "Expansión"),
    ("Invernadero Las Brisas", "Operativo"),
]

# Funciones
def editar(nombre):
    print(f"Editar: {nombre}")

def eliminar(nombre):
    print(f"Eliminar: {nombre}")

def detalles(nombre):
    print(f"Detalles: {nombre}")

# Ventana principal
ventana = tk.Tk()
ventana.title("Control invernadero")
ventana.geometry("730x430")
ventana.configure(bg="white")

# Encabezado
header = tk.Frame(ventana, bg="lightgreen", height=40)
header.pack(fill="x")

tk.Label(header, text="Vivero vital", bg="lightgreen", font=("Arial", 14, "bold")).pack(side="left", padx=10)

# Contenedor centrado
contenedor_central = tk.Frame(ventana, bg="white")
contenedor_central.pack(expand=True)

# Mostrar cada invernadero en una fila
for nombre, estado in invernaderos:
    fila = tk.Frame(contenedor_central, bg="white", pady=8)
    fila.pack()

    tk.Label(fila, text=nombre, width=25, bg="lightgray", font=("Arial", 10)).pack(side="left", padx=5)
    tk.Label(fila, text=estado, bg="#f4f4c2", width=12, font=("Arial", 10, "bold")).pack(side="left", padx=5)
    tk.Button(fila, text="Editar", bg="#f9f9dd", width=10, command=lambda n=nombre: editar(n)).pack(side="left", padx=2)
    tk.Button(fila, text="Eliminar", bg="#f9f9dd", width=10, command=lambda n=nombre: eliminar(n)).pack(side="left", padx=2)
    tk.Button(fila, text="Detalles", bg="orange", width=10, command=lambda n=nombre: detalles(n)).pack(side="left", padx=2)

# Botón Regresar y Pie de página
tk.Button(ventana, text="Regresar", bg="lightgreen", fg="white").place(x=620, y=350)

footer = tk.Frame(ventana, bg="orange", height=30)
footer.pack(side="bottom", fill="x")

tk.Label(footer, text="Control invernadero", bg="orange", fg="black").pack(side="right", padx=10)

ventana.mainloop()
