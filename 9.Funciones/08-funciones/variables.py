"""
Variables locales: 
Se definen dentro de una función y no se pueden usar fuera de ella, solo están disponibles dentro. A no ser que hagamos un return. 

Variables globales: 
Son las que se declaran de una función estás están disponibles dentro y fuera de ellas. 

"""

#Variable Global 
frase = "Ni los genios son tan genios"
print(frase)

def HolaMundo():
    #Variable local
    frase =  "Hola Mundo!!"
    print("Dentro de la función")
    print(frase)

HolaMundo()
