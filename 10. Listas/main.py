"""
LISTAS (arrays)
Son colecciones o conjuntos de datos/valores, bajo un único nombre.
Para acceder a esos valores podemos usar un indice númerico. 

"""

pelicula = "Batman"
#Definir una lista
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]
#Con la función list se dee pasar una tupla
cantantes = list(('2pac','Drake','Jenifer Lopez'))
years = list(range(2020,2050))
variada = ["Josué", 39, 4.4, True, "Texto"]
#Indices
print(peliculas[2])
#Con indices negativos se cuenta del último elemento de la lista para atrás
print(peliculas[-2])
#Se puede imprimir elementos por rango de indices
print(cantantes[1:3])
#Se puede sacar todos los elementos que hay en una lista a partir de un indice
print(peliculas[1:])#Se imprimiran todos los elementos de la lista a partir del indice 1
print(cantantes)
print(years)
print(variada)
#Se pueden cambiar los nombres de cualquier elemento de una lista reasignando el valor: 
peliculas[1] = "Gran Torino"
print(peliculas)

#Añadir elemento a lista
cantantes.append("Kase O")
cantantes.append("Natos y Waor")
print(cantantes[0:])

#Recurriendo peliculas
for pelicula in peliculas:
    print(pelicula)