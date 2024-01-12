import sqlite3

conn = sqlite3.connect("pruebas.db")

#Se crea un objeto cursor para ejecutar comandos SQL
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER
    )
''')

#confirmar los cambios y cerrar la conexión
conn.commit()

# Insertar datos

cursor.execute('''
    INSERT INTO usuarios VALUES (null,'Josue',39)
''')
conn.commit()

# Leer datos 
cursor.execute("SELECT * FROM usuarios")
conn.commit()
usuarios = cursor.fetchall()
for usuario in usuarios:
    print(usuario)

#Eliminar datos

cursor.execute("DELETE FROM usuarios")
conn.commit()

# conn.close()