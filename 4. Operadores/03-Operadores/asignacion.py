#Operadores de asignacion 

edad = 55

print("Hola tengo {}".format(edad))

#Con el operador += primero a la variable edad se le suna cinco y después se asigna el valor a la variable edad
#Esto es equivalente a edad = edad + 5
edad += 5
print("Ahora tengo {}".format(edad))

edad -=15
print("Ahora tengo {}".format(edad))

#Operadores de incremento y decremento year++
year = 2021

#Incremento 

year = year +1
year += 1
print(year)

#Decremento 
year = year -1 
year -= 1
print(year)

#Preincremento
year = 1 + year 

#Predecremento 
year = 1 - year