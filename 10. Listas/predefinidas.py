cantantes = ['2pac','Drake', 'Bad Bunny', 'Julio Iglesias']
numeros = [1,2,5,8,3,4]

#Ordenar
print(numeros)
numeros.sort() #Con el método sort podemos ordenar una lista
print(numeros)

# Añadir elementos
cantantes.append("Natos y Waor") #append es un metodo que solo recibe un parámetro y este lo coloca al final de la lista
print(cantantes)
cantantes.insert(2,"David Bisbal") # El método insert recibe dos parametros, el indice de la lista dond e se va a colocar el nuevo elemento, y el elemento a ingresar
print(cantantes)

# Elimiar el ementos

cantantes.pop(1) #El método pop elimina un elemento de la lista, en este caso es el del indice 1
cantantes.remove('Bad Bunny') # El método remove te permite eliminar elementos de una lista por su nombre
print(cantantes)

#Dar la vuelta 
numeros.reverse() # Ordena al reves la lista
print(numeros)

#Buscar dentro de una lista

print('Drake' in cantantes) # con in busca elementos de una lista y devuelve false o true
print(cantantes)

# Devuelve cantidad de elementos

print(f"Número de cantantes: {len(cantantes)}")


# Cuantas veces aparece un elemento en la lista con count(), como parametro ingresamos el elemento que vamos a contabilizar
print(numeros.count(8)) 
numeros.append(8)
print(numeros.count(8))

# Conseguir indice de un elemento

print(cantantes.index("David Bisbal"))

#Unir listas

cantantes.extend(numeros)
print(cantantes)