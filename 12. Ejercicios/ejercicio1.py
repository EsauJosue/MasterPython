"""
Ejercicio 1. Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente: 
-Recorrer una lista y mostrarla 
- Ordenarla y mostrarla
- Mostrar su longitud
"""
lista = [13,75,80,33,49,90,6,78]


lista.sort()
print(lista)
print(f"El tamaño de la lista es de: {len(lista)} elementos")

def recorreLista(lista):
    for elemento in lista:
        print(elemento)

recorreLista(lista)

