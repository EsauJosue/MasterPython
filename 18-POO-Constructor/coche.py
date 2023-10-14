
class Coche:
    # Atributos o propiedades
    
    # Caracteristicas del coche
    # color = ""
    # marca = ""
    # modelo = ""
    # velocidad = 0
    # caballos = 0
    # plazas = 0

    def __init__(self,color,marca,modelo,velocidad,caballos,plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballos = caballos
        self.plazas = plazas
        
    # Métodos (Acciones antes conocidas como funciones)
    # def acelerar(self): #Se utiliza self para que el método pueda acceder a los atributos de la clase
    #     self.velocidad += 1
    
    # def frenar(self):
    #     self.velocidad -= 1
    
    # def getVelocidad(self):
    #     return self.velocidad
    
    #Usando métodos con getter y setter
    # def setMarca(self, marca):
    #     self.marca = marca
    
    # def setColor(self, color):
    #     self.color = color
    
    # def getColor(self):
    #     return self.color
    
   
    
    # def getMarca(self):
    #     return self.marca
    
    def getInfo(self):
        info = "Información del coche \n"
        info += f"Color: {self.color}\n"
        info += f"Marca: {self.marca}\n"
        info += f"Modelo: {self.modelo}\n"
        info += f"Velocidad: {self.velocidad}\n"
        info += f"Caballos de fuerza: {self.caballos}\n"
        info += f"Plazas: {self.plazas}\n"
        return info
# fin definición clase
