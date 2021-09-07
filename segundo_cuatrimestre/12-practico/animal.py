from validacion_entero import validacionEntero

class Animal:
    def __init__(self):
        self.sano = True 

    def setHealth(self,weight, goodWeight):
        if weight >= goodWeight:
           self.sano = True
        else:
            self.sano = False

    def getHealth(self):
        return self.sano

