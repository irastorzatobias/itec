class Rueda:
    def __init__(self):
        self.inflada = False

    def inflarRueda(self):
        if self.inflada:
            print('La rueda ya esta inflada')
        else:
            self.inflada = True
    
    def desinflarRueda(self):
        if not self.inflada:
            print('La rueda ya esta desinflada')
        else:
            self.inflada = False
    
    def getInflated(self):
        return self.inflada

