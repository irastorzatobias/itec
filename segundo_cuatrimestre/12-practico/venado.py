from animal import Animal

class Venado(Animal):
    def __init__(self, identificador, peso):
        super().__init__()
        self.identificador = identificador
        self.peso = peso
        self.setHealth(self.peso, 120)


