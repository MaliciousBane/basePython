import tkinter as tk
from tkinter import ttk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Vivero vital")
ventana.geometry("800x400")
ventana.configure(bg="white")

# Encabezado verde
header = tk.Frame(ventana, bg="lightgreen", height=40)
header.pack(fill="x")
tk.Label(header, text="Vivero vital", bg="lightgreen", font=("Arial", 14, "bold")).pack(side="left", padx=10)


# Botones del menú principal
menu_frame = tk.Frame(ventana, bg="white")
menu_frame.pack(pady=5)
for texto in ["Registrar invernaderos", "Control invernaderos", "Control de humedad", "Control de piso", "Enfermedades"]:
    tk.Button(menu_frame, text=texto, bg="lightyellow", relief="groove").pack(side="left", padx=10)

# Filtro con Combobox
filtro_frame = tk.Frame(ventana, bg="white")
filtro_frame.pack(anchor="w", padx=20, pady=10)

tk.Label(filtro_frame, text="Filtrar por:", bg="white").pack(side="left")

opciones = ["Todos", "Las Flores", "Los Andes"]
filtro_combobox = ttk.Combobox(filtro_frame, values=opciones, state="readonly")
filtro_combobox.set("Todos")
filtro_combobox.pack(side="left", padx=5)

# Área de tarjetas de invernaderos
cards_frame = tk.Frame(ventana, bg="white")
cards_frame.pack()

def crear_tarjeta(nombre, capacidad, sistema, usuario):
    tarjeta = tk.Frame(cards_frame, bd=1, relief="solid", padx=30, pady=30)
    tarjeta.pack(side="left", padx=15)

    tk.Label(tarjeta, text=nombre, font=("Arial", 12, "bold")).pack()

    campos = [
        ("Nombre del invernadero:", nombre),
        ("Capacidad de producción:", capacidad),
        ("Sistema de riego:", sistema),
        ("Usuario encargado:", usuario),
        ("Fecha de creación:", "2025-05-04"),
    ]
    
    for campo, valor in campos:
        fila = tk.Frame(tarjeta)
        fila.pack(anchor="w")
        tk.Label(fila, text=campo).pack(side="left")
        tk.Entry(fila, width=20)
    
    # Etiqueta en lugar de imagen
    tk.Label(tarjeta, text="[Imagen Invernadero]", fg="gray").pack(pady=5)

    # Botones
    botones = tk.Frame(tarjeta)
    botones.pack()
    tk.Button(botones, text="Guardar", bg="green", fg="white").pack(side="left", padx=5)
    tk.Button(botones, text="Cancelar", bg="red", fg="white").pack(side="left", padx=5)

# Crear tarjetas de ejemplo
crear_tarjeta("Invernadero Las Flores", "3000", "Manual", "Juan Pérez")
crear_tarjeta("Invernadero Los Andes", "2000", "Automatizado", "María López")

# Pie de página
footer = tk.Frame(ventana, bg="orange", height=20)
footer.pack(side="bottom", fill="x")
tk.Label(footer, text="Menu", bg="orange").pack(side="right", padx=10)

ventana.mainloop()
