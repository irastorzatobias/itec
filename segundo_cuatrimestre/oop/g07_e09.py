from datetime import datetime


class Auto: # auto redefinido
    def __init__(self, marca:str,modelo:str, anio:int):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
    
    def getModelo(self):
        """ Retorna modelo del auto"""
        return self.modelo

    def getMarca(self):
        """ Retorna la marca del auto"""
        return self.marca

    def getAnio(self):
        """ Retorna el año del modelo del auto"""
        return self.anio
        
    def fullAuto(self):
        """ Retorna el auto con todas sus caracteristicas"""
        return self.marca, self.modelo, self.anio

    def getAntiguedad(self):
        """ Retorna la antiguedad del auto"""
        return datetime.now().year - self.anio


class TuAuto(Auto):
    def __init__(self,marca:str,modelo:str,anio:int, duenio:str, color:str):
        super().__init__(marca,modelo,anio)
        self.duenio = duenio
        self.color = color
    
    def getDuenio(self):
        """ Retorna el dueño del auto"""
        return self.duenio

    def getColor(self):
        """ Retorna el color del auto """
        return self.color


if __name__ == '__main__':
    autos = []
    # instanciacion de los tres autos
    myCar1 = TuAuto('VW','Vivastella',1933,'Tobias','azul')    
    myCar2 = TuAuto('Renault','Captur',2013,'Marcelo','gris')    
    myCar3 = TuAuto('BMW','',2021,'Lautaro','azul')
    autos.extend([myCar1,myCar2,myCar3]) # agrego a una lista los tres autos
    color = input('Ingrese un color para brindarle informacion acerca de los autos de ese color: ')
    autosByColor = list(filter(lambda car: True if car.getColor().lower() == color.lower() else False, autos))
    if len(autosByColor) >= 1:
        print(f'Autos en {color.lower()}')
        for e in autosByColor:
            print(e.fullAuto()) # full auto heredado de la clase Auto, yo instancie TuAuto
    else:
        print(f'No hay autos de color {color}')
       