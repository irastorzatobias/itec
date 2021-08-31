from motor import Motor
from puerta import Puerta
from rueda import Rueda
from ventana import Ventana

class Coche:
    def __init__(self):
        self.motor = Motor()
        self.ruedas = [Rueda(),Rueda(), Rueda(),Rueda()]
        self.puertas = [Puerta(), Puerta()]

    def inflarRuedas(self):
        """ Infla todas las ruedas"""
        for r in self.ruedas:
            r.inflarRueda()
    
    def cerrarPuertasYVentanas(self):
        """ Cierra todas las puertas y ventanas"""
        for p in self.puertas:
            p.cerrarPuerta()
            p.cerrarVentana()        
    
    def arrancar(self):
        self.inflarRuedas()
        self.cerrarPuertasYVentanas()
        self.motor.arrancarMotor()
        return f'Se inflaron las ruedas, cerraron las puertas, las ventanas y se encendio el motor. El auto esta listo para arrancar'

if __name__ == '__main__':
    auto1 = Coche()
    print(auto1.arrancar())
