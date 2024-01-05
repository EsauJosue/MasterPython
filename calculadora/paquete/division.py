class Division():
    def __init__(self, numero1, numero2):
        self.numero1 = getNumeros(numero1)
    

    def getNumeros(self,numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def setDivision(self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        division = numero1 / numero2
        return division




