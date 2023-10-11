from io import open #Este módulo sirve para poder crear archivos
import pathlib #Este módulo sirve para usar rutas relativas sin problemas en cualquier proyecto
import shutil #Este módulo se usa para copiar archivos 

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
"""
#Copiar archivo
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_relativa = str(pathlib.Path().absolute()) + "/../7.Bucles/fichero_copiado3.txt"

shutil.copyfile(ruta_original, ruta_nueva)
"""

# Mover