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
    
    #Usando métodos con getter y setter

    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color

# fin definición clase

# Crear objetos / Instanciar una clase

coche = Coche()
print(coche.velocidad)
coche.acelerar()
print(coche.velocidad)
coche.setColor("Verde cocodrilo")
print(f"El color del coche ahora es: {coche.getColor()}")

coche2 = Coche()
print(f"Color del coche 2: {coche2.color}")
print(f"Color del coche 1: {coche.color}")
