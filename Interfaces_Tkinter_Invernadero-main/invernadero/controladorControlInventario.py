from invernadero import Invernadero

class ControlInventario:
    def __init__(self, view):
        self.view = view
        self.invernaderos = [
            ("Invernadero Los Andes", "Operativo"),
            ("Invernadero Las Flores", "Reparación"),
            ("Invernadero Los Pinos", "Inspección"),
            ("Invernadero El Mirador", "Expansión"),
            ("Invernadero Las Brisas", "Operativo"),
        ]

    def cargar_invernaderos(self):
        self.view.mostrar_invernaderos(self.invernaderos)

    def editar(self, nombre):
        print(f"Editar: {nombre}")

    def eliminar(self, nombre):
        print(f"Eliminar: {nombre}")

    def detalles(self, nombre):
        print(f"Detalles: {nombre}")

    def regresar(self):
        self.view.destroy()
        from VistaMenu import VistaMenu
        VistaMenu()