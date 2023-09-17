nombre = "Esau Josue"
#Funciones generales
print(nombre)
print(f"El tipo de la variable es: {type(nombre)}")
#Limpiar espacios
frase = "     mi  contenido    "
print(frase.strip())
#Eliminar variables
year = 2023
print(year)
del year
#Comprobar variables vacias
texto = " ff "
if len(texto) <= 0: #Con la función len se pueden contar el número de caracteres que tiene una variable.
    print("La variable esta vacia")
else: 
    print("La variable tiene contenido: {} carácteres".format(len(texto)))