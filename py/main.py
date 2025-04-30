import tkinter as tk
from clase_modulo_producto import ProductoUI
from clase_modulo_cliente import ClienteUI

def abrir_productos():
    root.destroy()
    ProductoUI()

def abrir_clientes():
    root.destroy()
    ClienteUI()

root = tk.Tk()
root.title("Sistema de Gestión de Tienda")
root.resizable(False, False)

ancho_ventana = 400
alto_ventana = 200
pantalla_ancho = root.winfo_screenwidth()
pantalla_alto = root.winfo_screenheight()
x = (pantalla_ancho // 2) - (ancho_ventana // 2)
y = (pantalla_alto // 2) - (alto_ventana // 2)
root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")


tk.Label(root, text="Bienvenido al Sistema de Gestión", font=("Arial", 16)).pack(pady=10)
tk.Button(root, text="Gestionar Productos",font=("Arial", 12), width=30, command=abrir_productos).pack(pady=5)
tk.Button(root, text="Gestionar Clientes", font=("Arial", 12), width=30, command=abrir_clientes).pack(pady=5)

root.mainloop()
