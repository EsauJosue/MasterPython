import mysql.connector

# Conexion
database = mysql.connector.connect(
   host = "localhost",
   user = "root",
   password = "root",
   port = "8889",
   database = "master_python"
)

# Validar que la conexión es correcta
# print(database)

# Crear Base de Datos
cursor = database.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
# cursor.execute("SHOW DATABASES")
# for bd in cursor:
#     print(bd)

#Creación de una tabla
# nombre_tabla = input("Ingrese el valor de una tabla: ")
cursor.execute(f"""
CREATE TABLE IF NOT EXISTS Vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)  
""")
# cursor.execute("SHOW TABLES")
# for tables in cursor:
#     print(tables)

# cursor.execute("INSERT INTO Vehiculos VALUES(null,'Opel', 'Astra',18300.20)")

coches = [
    ('Opel','Astra',2000),
    ('Nissan','Platina',3000),
    ('Mercedes','Clase C',35000),
    ('Ford','Mustang',37000),
    ('GM','Sierra',65000)
]
cursor.executemany("INSERT INTO Vehiculos VALUES(null, %s, %s, %s)",coches)
database.commit()

#SELECT

cursor.execute("SELECT * FROM Vehiculos WHERE marca = 'NISSAN'")
result = cursor.fetchall() #Se puede cambiar por fetchone para que salga solo el primer resultado

for coche in result:
    print(coche[1], coche[2])

#Eliminando registros
cursor.execute("DELETE FROM Vehiculos") #Si no coloco el WHERE elimina todos los registros de la BD
database.commit()
print(cursor.rowcount, "Borrados !!") #Para mostrar que se ha borrado

#ACTUALIZAR 
cursor.execute("UPDATE Vehiculos SET modelo = 'Leon' WHERE marca = 'SEAT" )
database.commit()