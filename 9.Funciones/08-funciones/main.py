# Funciones: 
# Una función es un conjunto de instrucciones agrupadas bajo un nombre concreto que pueden reutilizarse invocando a la función tantas veces como sea necesario

# def nombreDeMiFuncion(parametros):
#     Bloque de instrucciones

# Ejemplo 1
# nombre = input("Ingrese un nombre: ")
# def muestraNombres(nombre):
#     print(f"El nombre es: {nombre}")

# muestraNombres(nombre)

# numero = int(input("Ingrese la tabla de multiplicar que desea consultar: "))

def tabla(numero):
    contador = 0
    for contador in range(1,11):
        print(f"{numero} x {contador} = {numero * contador}")

x = 1
for x in range(1,10):
    tabla(x)

def getEmpleado(nombre, dni = None):
    print("Empleado")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Josue Martinez")

# ejercicio 5

def saludame(nombre): 
    saludo = f"Hola, saludos {nombre}"
    return saludo
print(saludame("Josué"))

# ejercicio 6 

def getNom(nombre):
    texto = f"El nombre es: {nombre}"
    return texto


def getApellido(apellido):
    texto = f"El apellido es: {apellido}"
    return texto



def devuelveTodo(nombre,apellido = None):
    if apellido == None:
        texto = f"{getNom(nombre)}" 
    else:
        texto = f"{getNom(nombre)} \n {getApellido(apellido)}" 
    return texto

print(devuelveTodo("Josue"))