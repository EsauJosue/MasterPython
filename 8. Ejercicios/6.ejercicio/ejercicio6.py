# Muestra todas las tablas de multiplicar
tabla = 1

for tabla in range(1,11):
    numero = 1
    for numero in range(1,11):
        print("{} x {} = {}".format(tabla,numero,numero*tabla))