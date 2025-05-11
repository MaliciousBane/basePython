from invernadero import Invernadero

class controladorInverdadero:
    def __init__(self):
        self.lista = []

    def agregar(self, nombre, superficie, cultivo, fecha, responsable, capacidad, riego):
        nuevo = Invernadero(nombre, superficie, cultivo, fecha, responsable, capacidad, riego)
        self.lista.append(nuevo)
        print("Invernadero guardado:", vars(nuevo))
    
        
