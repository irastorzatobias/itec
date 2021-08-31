from datetime import datetime

class Auto:
    def __init__(self, marca:str, anio:int):
        self.marca = marca
        self.anio = anio
    
    def getMarca(self):
        """ Retorna la marca del auto"""
        return self.marca

    def getAnio(self):
        """ Retorna el año del modelo del auto"""
        return self.anio        
    
    def getAntiguedad(self):
        """ Retorna la antiguedad del auto"""
        return datetime.now().year - self.anio

class Marca(Auto):
    def __init__(self, modelo, anio, marca):
        super().__init__(marca,anio)
        self.modelo = modelo
    
    def getMarcaModelo(self):
        """ Retorna tupla con marca y modelo del auto"""
        return self.marca, self.modelo
    


if __name__ == '__main__':
    auto1 = Marca('Gol',2020,'VW') # heredada de auto, recibe modelo, anio y marca
    print(auto1.getMarcaModelo())