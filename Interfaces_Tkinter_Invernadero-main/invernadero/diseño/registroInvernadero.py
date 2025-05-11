import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Vivero vital")
ventana.geometry("920x460")
ventana.configure(bg="white")

# ----- Encabezado -----
header = tk.Frame(ventana, bg="lightgreen", height=40)
header.pack(fill="x")

tk.Label(header, text="Vivero vital", bg="lightgreen", font=("Arial", 14, "bold")).pack(side="left", padx=10)

# ----- Cuerpo Principal -----
main_frame = tk.Frame(ventana, bg="white", padx=30, pady=20)
main_frame.pack(fill="both", expand=True)

# Subframe del formulario
form_frame = tk.Frame(main_frame, bg="white")
form_frame.pack(side="left", anchor="center", expand=True)

# Subframe de la imagen
image_frame = tk.Frame(main_frame, bg="white")
image_frame.pack(side="right", anchor="center", padx=30)

# ----------------- FORMULARIO -----------------
tk.Label(form_frame, text="Nombre del invernadero", bg="white").pack(anchor="w")
tk.Entry(form_frame, width=30).pack(pady=2)

tk.Label(form_frame, text="Superficie (m²)", bg="white").pack(anchor="w")
tk.Entry(form_frame, width=30).pack(pady=2)

tk.Label(form_frame, text="Tipo de cultivo", bg="white").pack(anchor="w")
tipos_cultivo = ["Flores", "Frutas", "Verduras"]
ttk.Combobox(form_frame, values=tipos_cultivo, state="readonly", width=27).pack(pady=2)

tk.Label(form_frame, text="Fecha de creación", bg="white").pack(anchor="w")
tk.Entry(form_frame, width=30).pack(pady=2)

tk.Label(form_frame, text="Responsable del invernadero", bg="white").pack(anchor="w")
tk.Entry(form_frame, width=30).pack(pady=2)

tk.Label(form_frame, text="Capacidad de producción", bg="white").pack(anchor="w")
tk.Entry(form_frame, width=30).pack(pady=2)

tk.Label(form_frame, text="Sistema de riego", bg="white").pack(anchor="w")
sistemas_riego = ["Manual", "Automatizado", "Por goteo"]
ttk.Combobox(form_frame, values=sistemas_riego, state="readonly", width=27).pack(pady=2)

# Botones
botones_frame = tk.Frame(form_frame, bg="white")
botones_frame.pack(pady=10)
tk.Button(botones_frame, text="Guardar", bg="green", fg="white", width=10).pack(side="left", padx=5)
tk.Button(botones_frame, text="Cancelar", bg="red", fg="white", width=10).pack(side="left", padx=5)

# Si solo es un marcador visual:
tk.Label(image_frame, text="[ Imagen del invernadero ]", bg="lightgray", fg="black",
         width=35, height=15, anchor="center", font=("Arial", 12)).pack()

# ----- Pie de página -----
footer = tk.Frame(ventana, bg="orange", height=20)
footer.pack(side="bottom", fill="x")

tk.Button(footer, text="Registrar invernadero", bg="orange", fg="black").pack(side="right", padx=10)
tk.Button(footer, text="Regresar", bg="lightgreen", fg="white", height=1).pack(side="left", padx=10)

ventana.mainloop()

