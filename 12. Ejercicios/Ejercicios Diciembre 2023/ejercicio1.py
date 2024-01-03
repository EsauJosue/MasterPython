""" 
Hacer un programa que tenga una lista de 8 numeros enteros
1. Recorres una lista y mostrarla
2. Ordenarla y mostrarla
3. Mostrar su longitud
4. Mostrar algún elemento ( que el usuario pida por teclado)
"""
numeros = []

for x in range(1,9):
    numero = int(input("Ingrese un numero para agregarlo a la lista: "))
    numeros.append(numero)
print("Lista ingresada")
print(numeros)
print("Lista Ordendada")
numeros.sort()
print(numeros)
print("Longitud de la lista")
print(len(numeros))

numeroAbuscar = int(input("Ingrese el número a buscar: "))
#La función isinstance es usada para comprobar que el usuario esta ingresando valores de tipo entero

comprobar = isinstance(numeroAbuscar, int)
if comprobar:
    if numeroAbuscar in numeros:
        print("Si se encuentra en la lista")
    else: 
        print("No se encuentra en la lista")
else:
    print("Solo se permiten valores de tipo entero")