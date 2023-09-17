#Las funciones se crean al principio del archivo y se recomienda que esten juntas
#En las funciones se deben evitar las funciones print() y utlizar return 
#En vez de utilizar las variables como globales en las funciones, se recomienda mejor pasarlas como parametros cada vez que se hace una instancia

def mi_funcion(nombre):
    return "Hola que tal " + nombre

def mi_segunda_funcion(apellidos):
    return "Hola que tal 2" + apellidos

nombre = "Josué"
apellidos = "Robles"

print(mi_funcion(nombre))
print(mi_segunda_funcion(apellidos))