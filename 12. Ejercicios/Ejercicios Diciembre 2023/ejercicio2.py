'''
Escribir un programa que añada valores a una lista mientras que su longitud sea menor a 120 y luego mostrar la lista
Plus: Usar while y For 
'''

coleccion = []

# for contador in range(0,120):
#     coleccion.append(f"elemento-{contador}")
#     print(f"Mostrando el: {coleccion[contador]}")

print("Impresión de la lista con While")

contador = 0
while contador < 120:
    coleccion.append(f"elemento-{contador}")
    print(f"Mostrando el: {coleccion[contador]}")
    contador = contador + 1
