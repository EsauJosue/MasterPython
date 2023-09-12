#Bucle While 
# Estructura de control que itera o repite la ejecución de una serie de instrucciones tantas veces como sea necesario, hasta que deje de cumplirse la condición. 

# contador = 1
# muestrame = str(0)
# while contador <=10: 
    # print("Estoy en el número {}".format(contador))
    # muestrame = muestrame + ", " + str(contador)
    # contador = contador + 1
    # print(muestrame)
numero_usuario = int(input("De que número quieres la tabla? : "))

if numero_usuario < 1:
    numero_usuario = 1
print("###TABLA DEL {}###".format(numero_usuario))
contador = 1
while contador <= 10: 
    print("{} x {} = {}".format(numero_usuario,contador,numero_usuario*contador))
    contador += 1 # Es importante siempre aumentar el valor del contador si no se cicla infinitamente
else: 
    print("Tabla terminada")

