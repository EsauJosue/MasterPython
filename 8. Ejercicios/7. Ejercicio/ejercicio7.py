# Muestra todos los impares que indique el usuario

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

contador = 0

if num1 < num2:
    for contador in range (num1,num2+1):
        if contador % 2 != 0:
            print(contador)
else:
    print("El primer número debe ser menor al segundo")
