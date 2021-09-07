from animal import Animal

class Puma(Animal):
    def __init__(self, identificador:int, edad:int, peso:int):
        super().__init__()
        self.identificador = identificador
        self.edad = edad
        self.peso = peso
        self.salud = self.setHealth(peso,200)

    def getAdulto(self):
        """ Devuelve si true puma es adulto, false si es cachorro"""
        if self.edad > 5:
            return True
        else:
            return False


if __name__ == '__main__':
    ezequiel = Puma(12,22,203)
    print(ezequiel.getHealth())
    print(ezequiel.getAdulto())
    

