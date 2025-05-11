import tkinter as tk
from tkinter import messagebox

# Función para manejar el botón de confirmar
def confirmar():
    usuario = entry_usuario.get()
    clave = entry_clave.get()
    if usuario == "Admin" and clave == "12345678":  # ejemplo de validación
        messagebox.showinfo("Acceso permitido", "Bienvenido al sistema")
    else:
        messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos")

# Ventana principal
ventana = tk.Tk()
ventana.title("Vivero vital")
ventana.geometry("700x500")
ventana.configure(bg="white")

# Encabezado verde
header = tk.Frame(ventana, bg="green", height=40)
header.pack(fill="x")
tk.Label(header, text="Vivero vital", bg="green", fg="black", font=("Arial", 12, "bold")).pack(side="left", padx=10)

# Título de inicio de sesión
frame_login = tk.Frame(ventana, bg="lightyellow", pady=70, padx=70, bd=1, relief="solid")
frame_login.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame_login, text="Iniciar Sesion", bg="lightyellow", font=("Arial", 28)).pack(pady=5)

# Entrada de usuario
entry_usuario = tk.Entry(frame_login, width=35)
entry_usuario.insert(0, "Admin")
entry_usuario.pack(pady=2)

# Entrada de contraseña
entry_clave = tk.Entry(frame_login, width=35, show="●")
entry_clave.pack(pady=2)

# Botón de confirmar
btn_confirmar = tk.Button(frame_login, text="Confirmar", bg="green", fg="white", command=confirmar)
btn_confirmar.pack(pady=5)

# Pie de página
footer = tk.Frame(ventana, bg="orange", height=30)
footer.pack(side="bottom", fill="x")

ventana.mainloop()
