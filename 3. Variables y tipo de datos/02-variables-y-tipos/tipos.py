entero = 24
flotante = 3.4
lista = [23,34,45,56,67,78]
booleano = False
tuplaNOCambia = ("master", "en", "Python")
# Un diccionario tiene la misma forma que un JSON
diccionario = {
    "Nombre": "Victor Robles",
    "Edad": 38,
    "FechaNac": "16 de Septiembre"
}
rango = range(9)
print(id(diccionario))

def suma(a,b):
    resultado = a + b
    return resultado

# print("El resultado de la suma es de: " + str(suma(entero,flotante)))

#Convirtiendo datos
# Texto 
numerito = str(775)
print(type(numerito))
# Entero
numerito = int(765)
print(type(numerito))
# Flotante
numerito = float(776)
print(type(numerito))
print(numerito)


