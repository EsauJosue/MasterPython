"""
Ingresar todos los números que existen entre dos numeros que el usuario ingrese

"""

num_inicio = int(input("Ingrese el número de inicio: "))
num_fin = int(input("Ingrese el número final: "))

for numero in range(num_inicio,num_fin+1):
    print(numero)