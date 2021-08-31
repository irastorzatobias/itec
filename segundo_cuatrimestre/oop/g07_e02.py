from datetime import datetime
class Auto:
    def __init__(self, marca:str, anio:int):
        self.marca = marca
        self.anio = anio

    
    def getMarca(self):
        return self.marca.title()

    def getAnio(self):
        return self.anio        

    def getAntiguedad(self):
        return datetime.now().year - self.anio
        
    


if __name__ == '__main__':
    autos = []
    autosAntiguos = []
    auto1 = Auto('gol',2003)
    auto2 = Auto('bora',2020)
    auto3 = Auto('clio',2005)
    autos.extend([auto1,auto2,auto3])
    i = 1
    for e in autos:
        print(f'Marca de auto {i}: {e.getMarca()}')
        i += 1
    
    
