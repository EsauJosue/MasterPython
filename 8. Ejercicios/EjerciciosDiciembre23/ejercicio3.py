"""
Que imprima en pantalla el cuadrado de los 60 primeros números naturales

"""

for num in range(1,61):
    print(f"Con for {pow(num,2)}")

numero = 1
while numero<=60:
    print(f"Con While {pow(numero,2)}")
    numero = numero + 1
