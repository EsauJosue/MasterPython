# Una variable es un contenedro de información que dentyro guardara un dato, se pueden crear muchas variables y que cada una tenga un dato distinto

# Python es un lenguaje debilmente tipado

# Crear variables y mostrar un valor
texto = "Master en Python"
texto2 = "Con Victor Robles"
numero = 45
decimal = 6.7
#Constante
PI = 3.1416 
# print(texto)
# print(texto2)
# print(numero)
# print(type(decimal))

#Concatenación de cadenas de texto

nombre = "Josué"
apellidos = "Martínez Carrasco"
web = "esaujosue.dev"

print(nombre + " " + apellidos +" " + web)
# Otro tipo de concatenación utilizando f (Recomendado)
print(f"{nombre} {apellidos} - {web}")
# Otro tipo de concatenación utilizando el método format()
print("Hola me llamo {} {} y mi web es: {}".format(nombre,apellidos, web))
