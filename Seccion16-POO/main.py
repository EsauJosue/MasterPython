# Programación Orientada a Objetos 

#Definición de una clase (molde para crear objetos de ese tipo

class Coche:
    def __init__(self,color,marca, modelo, velocidad, caballaje, plazas):
        #Atributos o Propiedades de la clase
        self.setColor(color)
        self.setMarca(marca)
        self.setModelo(modelo)
        self.setVelocidad(velocidad)
        self.setCaballaje(caballaje)
        self.setPlazas(plazas)  
    
    #Caracteristicas del coche
    # color = "Rojo"
    # marca = "Ferrari"
    # modelo = "Aventador"
    # velocidad = 300
    # caballaje = 500
    # plazas = 2

    #Métodos, son acciones que hace el objeto (coche) (funciones)
        
    #Setters
    def setColor(self, color):
        self.color = color
    def setMarca(self, marca):
        self.marca = marca
    def setModelo(self, modelo):
        self.modelo = modelo
    def setCaballaje(self, caballaje):
        self.caballaje = caballaje
    def setPlazas(self,plazas):
        self.plazas = plazas
    def setVelocidad(self,velocidad):
        self.velocidad = velocidad


    def acelerar(self):
        self.velocidad += 1
    def frenar(self):
        self.velocidad -= 1
    
    # Getters
    
    def getColor(self):
        return self.color
    def getMarca(self):
        return self.marca
    def getCaballaje(self):
        return self.caballaje
    
    
    def getVelocidad(self):
        return self.velocidad

# fin definición de clase 
    
    #Crear objeto o instanciar la clase

coche1 = Coche("Rojo","Tsuru","T2",0,200, 4)
print(coche1.getColor())



