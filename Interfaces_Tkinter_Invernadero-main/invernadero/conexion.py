import mysql.connector

class conexion:

   def __init__(self):
        self.user = "root"
        self.password = ""
        self.database = "invernaderopy"
        self.host = "localhost"

   def hacer_conexion(self):
        try:
            conex = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if conex.is_connected():
                print("Conexión exitosa...")
            return conex
        except Exception as e:
            print("Error de conexión:", e)
            return None



   def hacer_consulta(dato_conex):
         if dato_conex:
            puntero = dato_conex.cursor()
            puntero.execute("SELECT * FROM iniciosesion")
            resultado = puntero.fetchall()
            print(resultado)
            return
         
   def hacer_consulta2(dato_conex):
         if dato_conex:
            puntero = dato_conex.cursor()
            puntero.execute("SELECT * FROM registroinvernadero")
            resultado = puntero.fetchall()
            print(resultado)
            return