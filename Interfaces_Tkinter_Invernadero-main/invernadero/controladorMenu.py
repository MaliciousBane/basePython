from invernadero import obtener_invernaderos

class ControladorMenu:
    def __init__(self, view):
        self.view = view

    def obtener_datos_invernadero(self):
        return obtener_invernaderos()

    def navegar(self, opcion):
        if opcion == "Registrar invernaderos":
            self.view.destroy()
            from vistaRegistro import Registro
            Registro()
        elif opcion == "Control invernaderos":
            self.view.destroy()
            from VistaControlInventario import VistaControlInventario
            VistaControlInventario()
        else:
            print(f"Funcionalidad {opcion} aún en desarrollo.")
