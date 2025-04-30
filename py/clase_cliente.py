from Clase_conexion import conexion

class Cliente:
    def __init__(self):
        self.db = conexion().hacer_conexion()

    def agregar(self, nombre, apellidos, email):
        cursor = self.db.cursor()
        sql = "INSERT INTO clientes (nombre, apellidos, email) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nombre, apellidos, email))
        self.db.commit()

    def listar(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM clientes")
        return cursor.fetchall()

    def eliminar(self, id_cliente):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = %s", (id_cliente,))
        self.db.commit()

    def actualizar(self, id_cliente, nombre, apellidos, email):
        cursor = self.db.cursor()
        sql = "UPDATE clientes SET nombre=%s, apellidos=%s, email=%s WHERE id=%s"
        cursor.execute(sql, (nombre, apellidos, email, id_cliente))
        self.db.commit()
