
try:
    nombre = input("Ingrese su nombre: ")
    if len(nombre) > 1:
        mi_nombre = f"El nombre es {nombre}"
    print(mi_nombre)
except:
    print("Ingrese bien su nombre")
else: 
    print("Todo OK")
finally: 
    print("Fin de la iteración")

# Multiples excepciones
import math
try:
    numero = int(input("Número para elevarlo al cuadrado: "))
    print("El cuadrado es: {}".format(str(math.pow(numero,2))))
except TypeError:
    print("Error en el tipo de dato")
# except ValueError: 
#     print("Error en el valor ingresado")
except Exception as e: 
    print("Ha ocurrido un error: {}".format(type(e).__name__))

#Excepciones Personalizadas o lanzar excepciones

try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))
    if edad < 5 or edad >110:
        raise ValueError("No cuenta con edad adecuada")
        # print("No cuenta con edad adecuada")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido al master en Python {nombre}")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print("Existe un error: ", e)