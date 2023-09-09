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

#ELIF
dia = int(input("Ingrese el número de la semana: "))

if dia == 1:
    print("Es lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miércoles")
elif dia == 4:
    print("Es jueves")
elif dia == 5:
    print("Es viernes")
elif dia == 6:
    print("Es sábado")
elif dia == 7:
    print("Es Domingo")
