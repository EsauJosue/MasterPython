#Escribir un programa que añada elementos a una lista mientras que la longitud de la lista sea menor a 120
#Usar while y for 

coleccion = []

for contador in range(0,120):
    coleccion.append(f"elemento-{contador}")
    print("Mostrando el: " + coleccion[contador])

print(coleccion)