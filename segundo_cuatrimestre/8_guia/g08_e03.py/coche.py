
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
    
    
    def aPuerta(self, numPuerta:int):
        """ Recibe el numero de puerta y abre la misma tras el uso del metodo de la clase puertas"""
        if numPuerta > len(self.puertas):
            print('La puerta no existe')
        else:
            self.puertas[numPuerta].abrirPuerta()


    def cPuerta(self, numPuerta:int):
        """ Recibe el numero de la puerta y cierra la misma tras el uso del metodo de la clase puertas"""
        if numPuerta > len(self.puertas):
            print('La puerta no existe')
        else:
            self.puertas[numPuerta].cerrarPuerta()

    def aVentana(self, numPuerta:int):
        """" Recibe el numero de la puerta y abre la ventana de la misma tras el uso del metodo de la clase ventana, heredado en puertas"""
        if numPuerta > len(self.puertas):
            print('La puerta no existe')
        else:
            self.puertas[numPuerta].abrirVentana()
    
    def cVentana(self, numPuerta:int):
        """" Recibe el numero de la puerta y cierra la ventana de la misma tras el uso del metodo de la clase ventana, heredado en puertas"""
        if numPuerta > len(self.puertas):
            print('La puerta no existe')
        else:
            self.puertas[numPuerta].abrirVentana()
    
    
    
    def checkAuto(self):
        """ Chequea las puertas, ventanas, ruedas y motor del auto"""
        if self.motor.getOnOff():
            print('El motor esta prendido')
        else:
            print('El motor esta apagado')
        for i in range(len(self.ruedas)):
            if self.ruedas[i].getInflated():
                print(f'La rueda {i} esta inflada')
            else:
                print(f'La rueda {i} no está inflada')
        for i in range(len(self.puertas)):
            if self.puertas[i].getClosedOpen():
                print(f'La puerta {i} esta abierta')
            else:
                print(f'La puerta {i} esta cerrada')
            if self.puertas[i].getWindowState():
                print(f'La ventana de la puerta {i} está abierta')
            else:
                print(f'La ventana de la puerta {i} está cerrada')
    
    
    def arrancar(self):
        self.inflarRuedas()
        self.cerrarPuertasYVentanas()
        self.motor.arrancarMotor()
        return f'Se inflaron las ruedas, cerraron las puertas, las ventanas y se encendio el motor. El auto esta listo para arrancar'

if __name__ == '__main__':
    auto1 = Coche()
    auto1.checkAuto()
    print(auto1.puertas[0].getWindowState())
    # Testeando metodos
    auto1.aPuerta(0)
    auto1.aVentana(0)
    auto1.checkAuto()
    auto1.inflarRuedas()
    auto1.checkAuto()
    print(auto1.arrancar())
