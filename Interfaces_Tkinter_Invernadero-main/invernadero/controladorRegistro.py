from invernadero import Invernadero

class controladorRegistro:
    def __init__(self, view):
        self.view = view

    def guardar(self):
        nombre = self.view.entry_nombre.get()
        superficie = self.view.entry_superficie.get()
        cultivo = self.view.entry_cultivo.get()
        fecha = self.view.entry_fecha.get()
        responsable = self.view.entry_responsable.get()
        capacidad = self.view.entry_capacidad.get()
        riego = self.view.entry_riego.get()

        nuevo_invernadero = Invernadero(nombre, superficie, cultivo, fecha, responsable, capacidad, riego)
        print(f"Invernadero creado: {nuevo_invernadero}")

        self.view.destroy()
        from VistaMenu import VistaMenu
        VistaMenu()

    def regresar(self):
        self.view.destroy()
        from VistaMenu import VistaMenu
        VistaMenu()
        