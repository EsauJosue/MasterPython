"""
    Programa que calcule el x porcioento de la cantidad que ingrese el usuario.
    Por ejemplo: 20% de 150

"""

cantidad = int(input("Ingrese la cantidad: "))
porcentaje = int(input("¿Cual es el porcentaje que desea calcular?: "))

print(f"El {porcentaje}% de {cantidad} es igual a: {cantidad * (porcentaje/100)}")
