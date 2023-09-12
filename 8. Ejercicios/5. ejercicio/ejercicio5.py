# Mostrar todos los numeros que exiten entre dos numeros que el usuario indique

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

contador = 0

if num1 < num2:
    for contador in range (num1,num2+1):
        print(contador)
else:
    print("El primer número debe ser menor al segundo")
