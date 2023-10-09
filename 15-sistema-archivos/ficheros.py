from io import open
import pathlib

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "a+") 

# Escribir
archivo.write("*****Soy un texto metido desde Python**** \n")

# Cerrar archivo
archivo.close()


archivo_lectura = open(ruta, "r")

# Leer contenido

# contenido = archivo_lectura.read()
# print(contenido)

# Leer contenido y guardar en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

# print(lista)

for elemento in lista:
    print("- "+elemento.upper())