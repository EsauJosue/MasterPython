#Escribir un programa que añada elementos a una lista mientras que la longitud de la lista sea menor a 120
#Usar while y for 

coleccion = []
contador = 0

# for contador in range(0,120):
#     coleccion.append(f"elemento-{contador}")
#     print("Mostrando el: " + coleccion[contador])

# print(coleccion)

while contador <= 120:
    coleccion.append(f"Elemento-{contador}")
    print("Mostrando el: " + coleccion[contador])
    contador += 1