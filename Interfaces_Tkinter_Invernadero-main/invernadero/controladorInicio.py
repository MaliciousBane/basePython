from tkinter import messagebox
from VistaMenu import VistaMenu  # Importamos la vista del menú

class controladorInicio:
    def __init__(self, view):
        self.view = view

    def validar_login(self):
        usuario = self.view.entry_usuario.get()
        clave = self.view.entry_clave.get()
        
        if usuario == "a" and clave == "1":  
            messagebox.showinfo("Acceso permitido", "Bienvenido al sistema")
            self.view.destroy()  # Cierra la ventana de login
            VistaMenu()  # Abre la ventana del menú
        else:
            messagebox.showerror("Acceso denegado", "Usuario o contraseña incorrectos")