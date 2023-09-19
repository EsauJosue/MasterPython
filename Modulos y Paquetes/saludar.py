# Modulo para saludos y otros mensajes

def hola(nombre = None):
    #Saluda al nombre que se le pasa como argumeto
    if nombre: 
        print(f"Hola {nombre}")
    else:
        print("Hola Mundo")
