# Importar modulo

import sqlite3

# Conexión 

conexion = sqlite3.connect('pruebas.db')

# Crear cursor
cursor = conexion.cursor()

# Crear una tabla
cursor.execute("CREATE TABLE IF NOT EXISTS productos("+
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"+
               "titulo varchar(255),"+
               "descripcion text,"+
               "precio int(255)"+
               ")")
#Cuardar cambios
conexion.commit()
#Cerrer conexion
conexion.close()