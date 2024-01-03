"""
Mostrar todos los números impares que hay enre dos numeros que proprocione el usuario
"""
num_inicio = int(input("Ingrese el número de inicio: "))
num_fin = int(input("Ingrese el número final: "))

for num in range(num_inicio, num_fin):
    if not num % 2 == 0:
        print(num)