class Motor:
    def __init__(self):
        self.encendido = False
    

    def arrancarMotor(self):
        if self.encendido:
            print('El motor ya está encendido')
        else:
            self.encendido = True
    
    def apagarMotor(self):
        if not self.encendido:
            print('El motor ya esta apagado')
        else:
            self.encendido = False
    
    def getOnOff(self):
        return self.encendido
