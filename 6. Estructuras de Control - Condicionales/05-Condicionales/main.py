#Condicional

print("Ejemplo 1")
edad = input("Cuál es tu edad?")
if int(edad) >= 18:
    print("Eres mayor de edad")
else: 
    print("No eres mayor de edad. Niño")

#Opradores de comparación 

# == Igual 
# != Diferente 
# < menor que 
# > mayor que 
# <= menor o igual
# >= mayor o igual 

persona = {
    "Nombre" : "Esaú",
    "Apellido" : "Martínez",
    "Lenguaje" : "Python",
    "Edad" : edad
}
def validaPersona(persona):
    edad = int(persona["Edad"])
    apellido = persona["Apellido"]
    #IFs Anidados
    if  edad > 18:
        if apellido == "Martínez":
            print("La persona tiene {}, por lo tanto es mayor de edad \n y se apellida {}".format(edad,apellido))

    print(persona)

validaPersona(persona)