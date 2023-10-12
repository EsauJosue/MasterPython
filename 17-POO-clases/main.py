# Programación Orientada a objetos (POO o OOP)

# Definición de una clase
class Coche:
    # Atributos o propiedades
    # Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballos = 500
    plazas = 2

    # Métodos (Acciones antes conocidas como funciones)
    def acelerar(self): #Se utiliza self para que el método pueda acceder a los atributos de la clase
        self.velocidad += 1
    
    def frenar(self):
        self.velocidad -= 1
    
    def getVelocidad(self):
        return self.velocidad

# fin definición clase

# Crear objetos / Instanciar una clase

coche = Coche()
print(coche.velocidad)

coche.acelerar()
print(coche.velocidad)
