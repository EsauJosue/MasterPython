""" 
Los diccionarios tienen indices alfanumericos, es como un json
Es un tipo de dato que almacena un conjunto de datos. 
En formato clave > valor
"""

persona = {
    "nombre" : "Josue",
    "apellidos" : "Robles",
    "Web" : "esaujosue.dev"
}
print(type(persona))
print(persona["apellidos"]) # Para poder imprimir a un elemento del diccionario es necesario agregar el nombre de la clave
print(persona["Web"])
