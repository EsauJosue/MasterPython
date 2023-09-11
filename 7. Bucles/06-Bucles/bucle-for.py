#Bucle FOR 

#for variable in elemento_iterable (lista,rango, etc)
    #Bloque de instrucciones

numero_usuario = int(input("Que número quieres la tabla de multiplicar"))

for numero_tabla in range(0,10):
    print("{} x {} = {}".format(numero_usuario,numero_tabla,numero_usuario*numero_tabla))
else: #En python también se pueden agregar else cuando se usa un for 
    print("Tabla finalizada")
