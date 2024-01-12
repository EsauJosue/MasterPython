import mysql.connector

#Conexión
conexion = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    password="root"
)

#Se crea objeto cursor para las consultas SQL 

cursor = conexion.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python"
)

cursor.execute("SHOW DATABASES")
bd_buscar = 'master_python'

for bd in cursor:
    print("Base de datos: ", bd)
    

