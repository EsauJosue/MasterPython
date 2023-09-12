# Cuadrado de los primeros sesenta numeros naturales

contador = 0
contador_w = 0

for contador in range(1,61):
    print(f"{contador} al cuadrado es: {pow(contador,2)} ciclo for")
else: 
    print("Fin del ciclo For")

while contador_w <= 60:
    print(f"{contador_w} al cuadrado es: {pow(contador_w,2)} ciclo while")
    contador_w += 1
else: 
    print("Fin del ciclo While")

