"""
Ejercicio 1. Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente: 
-Recorrer una lista y mostrarla 
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar un elemento
"""
lista = [13,75,80,33,49,90,6,78]


lista.sort()
print(lista)
print(f"El tamaño de la lista es de: {len(lista)} elementos")

def recorreLista(lista):
    for elemento in lista:
        print(elemento)

recorreLista(lista)

# Buscando un elemento

dato = input("Que número quieres buscar en en la lista: ")

comprobar = isinstance(dato,int)
if comprobar:
    if int(dato) in lista:
        print("El número si se encuentra en la lista")
    else:
        print("El número no se encuentra en la lista")