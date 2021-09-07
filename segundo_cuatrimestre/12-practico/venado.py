from animal import Animal

class Venado(Animal):
    def __init__(self, identificador, peso):
        super().__init__()
        self.identificador = identificador
        self.peso = peso
        self.salud = self.setHealth(peso, 120)


