"""
Ejercicio 1. Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente: 
-Recorrer una lista y mostrarla 
- Ordenarla y mostrarla
- Mostrar su longitud
"""
lista = [3,7,8,3,9,2,6,5]

for elemento in lista:
    print(elemento)

lista.sort()
print(lista)
print(f"El tamaño de la lista es de: {len(lista)} elementos")