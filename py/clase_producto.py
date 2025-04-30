from Clase_conexion import conexion

class Producto:
    def __init__(self):
        self.db = conexion().hacer_conexion()

    def agregar(self, nombre, precio, stock, categoria):
        cursor = self.db.cursor()
        sql = "INSERT INTO productos (nombre, precio, stock, categoria) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nombre, precio, stock, categoria))
        self.db.commit()

    def listar(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM productos")
        return cursor.fetchall()

    def eliminar(self, id_producto):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM productos WHERE id = %s", (id_producto,))
        self.db.commit()

    def actualizar(self, id_producto, nombre, precio, stock, categoria):
        cursor = self.db.cursor()
        sql = "UPDATE productos SET nombre=%s, precio=%s, stock=%s, categoria=%s WHERE id=%s"
        cursor.execute(sql, (nombre, precio, stock, categoria, id_producto))
        self.db.commit()
