# SET es un tipo de dato para tener una coleccion de valores, pero no tiene ni indice ni orden

personas = {
    'Victor',
    'Manolo',
    'Francisco'
}
print(type(personas))

personas.add('Josue')
print(personas)

personas.remove('Francisco')
print(personas)
