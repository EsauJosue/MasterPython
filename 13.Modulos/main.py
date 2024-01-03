import mimodulo
import datetime
import math
import random
# from mimodulo import * Con este tipo de import, se pueden importar todas las funciones que contenga el módulo.
 #Para importar un modulo es necesario utilizar la palabra import
print(mimodulo.holaMundo("Josue Martinez"))

# num1 = int(input("Ingrese el primer número: "))
# num2 = int(input("Ingrese el segundo número: "))

# print(f"La suma de los númeroes {num1} + {num2} es: {mimodulo.suma(num1,num2) }")

#Modulo Datetime
# print(datetime.date.today())
# fecha_completa = datetime.datetime.now()
# print(fecha_completa)
# print(fecha_completa.year)
# print(fecha_completa.month)
# print(fecha_completa.day)

# fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
# print(f"Mi fecha personalizada es: {fecha_personalizada}")


#Modulo Math
numero = 10 
raiz = math.sqrt(numero)
print(raiz)


print("Numero aleatori entre 15 y 67: ", random.randint(15,67))