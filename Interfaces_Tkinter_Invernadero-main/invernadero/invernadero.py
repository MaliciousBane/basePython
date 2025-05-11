class Invernadero:
    def __init__(self, nombre, superficie, cultivo, fecha, responsable, capacidad, sistema_riego):
        self.nombre = nombre
        self.superficie = superficie
        self.cultivo = cultivo
        self.fecha = fecha
        self.responsable = responsable
        self.capacidad = capacidad
        self.sistema_riego = sistema_riego

    def __str__(self):
        return f"Invernadero {self.nombre} - Superficie {self.superficie} - Cultivo {self.cultivo} - Fecha {self.fecha} - Responsable {self.responsable} - Capacidad: {self.capacidad} - Riego: {self.sistema_riego}"

def obtener_invernaderos():
    return [
        Invernadero("Invernadero Las Flores", "3000", "Flores", "01/01/2025", "Juan Pérez", "500kg/mes", "Manual"),
        Invernadero("Invernadero Los Andes", "2000", "Verduras", "15/02/2025", "María López", "300kg/mes", "Automatizado"),
    ]
