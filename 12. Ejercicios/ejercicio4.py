#Crear un script que tenga 4 variables, una lista, un string, un entero y un booleano y que imprima un mensaje según el tipo de dato de cada variable. Usar funciones

lista = ["Hola mundo", 77]
titulo = "Master en python"
numero = 100
verdadero = True

def comprobar(dato, tipo):
    
    comprobar = isinstance(dato, tipo)

    if comprobar: 
        print(f"El tipo de dato del valor {dato} es {tipo}")

comprobar(lista,type(lista))
comprobar(titulo,type(titulo))
comprobar(numero,type(numero))
comprobar(verdadero,type(verdadero))