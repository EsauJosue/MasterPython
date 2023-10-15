# Importar modulo

import sqlite3

# Conexión 

conexion = sqlite3.connect('pruebas.db')

# Crear cursor
cursor = conexion.cursor()

# Crear una tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo varchar(255),
    descripcion text,
    precio int(255)
);
""")
#Cuardar cambios
conexion.commit()

#Insertar datos
# cursor.execute("INSERT INTO productos VALUES(null, 'Primer producto', 'Descripcion de mi producto',550)")
conexion.commit()

# Insertar muchos registros al mismo tiempo

productos = [
    ("Telefono","es de 5G",1500),
    ("Tablet","Con lápiz",5000),
    ("PC","All in One",7800),
]

cursor.executemany("INSERT into productos VALUES (null,?,?,?)",productos)

#UPDATE
cursor.execute("UPDATE productos SET precio=678 WHERE precio=80")

#Listar datos
cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()
# print(productos)
for producto in productos:
    print(f"ID: {producto[0]}")
    print(f"Título: {producto[1]}")
    print(f"Descripción: {producto[2]}")
    print(f"Precio: {producto[3]}")


producto = cursor.fetchone()
print(producto)

# Borrar registros
cursor.execute("DELETE FROM productos")
conexion.commit()

#Cerrer conexion
conexion.close()