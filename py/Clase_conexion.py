import mysql.connector
class conexion:
  
 def __init__(self):
     self.user="root"
     self.password=""
     self.database="bd_python"
     self.host="localhost"

 def hacer_conexion():
    conexion = mysql.connector.connect(host="localhost", database="bd_python", user = "root", password="")
    try:
        if conexion.isconnected():
           print("conexion exitosa.....")
    except:
       print("Error de conexion.....")
    return conexion

 def hacer_consulta(dato_conex):
    if dato_conex:
       puntero = dato_conex.cursor()
       puntero.execute("SELECT * FROM clientes")
       resultado = puntero.fetchall()
       print(resultado)
       return
    
 def hacer_consulta2(dato_conex):
    if dato_conex:
       puntero = dato_conex.cursor()
       puntero.execute("SELECT * FROM productos")
       resultado = puntero.fetchall()
       print(resultado)
       return