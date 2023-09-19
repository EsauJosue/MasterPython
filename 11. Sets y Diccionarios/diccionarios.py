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

#Lista con diccionarios

contactos = [
    {
        'nombre' : 'Antonio',
        'email' : 'antonio@gmail.com'
    },
      {
        'nombre' : 'Luis',
        'email' : 'luis@gmail.com'
    },
      {
        'nombre' : 'Salvador',
        'email' : 'salvador@gmail.com'
    },
]
print(contactos)
print(contactos[0]['nombre'])
contactos[0]['nombre'] = 'Josue'
print(contactos)

# Recorriendo la lista
for contacto in contactos: 
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Email del contacto: {contacto['email']}")
    print("-------------------------")
