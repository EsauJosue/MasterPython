# Herencia es la posibilidad de compartir metodos y atributos entre clases, y que diferentes clases hereden de otras

class Persona:
    def setNombre(self,nombre):
        self.nombre = nombre
    def setApellidos(self, apellidos):
        self.apellidos = apellidos
    def setAltura(self,altura):
        self.altura = altura
    def setEdad(self,edad):
        self.edad = edad

    def getNombre(self):
        return self.nombre
    def getApellidos(self):
        return self.apellidos
    def getAltura(self):
        return self.altura
    def getEdad(self):
        return self.edad
    
    def hablar(self):
        return "Estoy Hablando"
    def caminar(self):
        return "Estoy caminando"
    def dormir(self):
        return "Estoy durmiendo"
    
class Informatico (Persona):
    def __init__(self):
        self.lenguajes = "PHP, JAVASCRIPT, HTML, CSS"
        self.experiencia = "5 años"
    
    def getLenguajes(self):
        return self.lenguajes
    
    def aprenderLenguajes(self,lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes
    def programar(self):
        return "Estoy programando"
    def repararPC(self):
        return "He reparado tu ordenador"

class tecnicoRedes(Informatico):
    def __init__(self):
        super().__init__() #Con esta instrucción se puede heredar tambien los atributos del constructor de su clase padre, es decir de Informatico
        self.auditarRedes = "Experto"
        self.experienciaRedes = "15 años"