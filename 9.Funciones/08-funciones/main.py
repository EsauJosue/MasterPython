# Funciones: 
# Una función es un conjunto de instrucciones agrupadas bajo un nombre concreto que pueden reutilizarse invocando a la función tantas veces como sea necesario

# def nombreDeMiFuncion(parametros):
#     Bloque de instrucciones

# Ejemplo 1
# nombre = input("Ingrese un nombre: ")
# def muestraNombres(nombre):
#     print(f"El nombre es: {nombre}")

# muestraNombres(nombre)

# numero = int(input("Ingrese la tabla de multiplicar que desea consultar: "))

def tabla(numero):
    contador = 0
    for contador in range(1,11):
        print(f"{numero} x {contador} = {numero * contador}")

x = 1
for x in range(1,10):
    tabla(x)
