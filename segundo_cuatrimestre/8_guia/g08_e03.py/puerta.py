from ventana import Ventana

class Puerta(Ventana):
    def __init__(self):
        super().__init__()
        self.abierta = False
    
    def abrirPuerta(self):
        if self.abierta:
            print('La puerta ya esta abierta')
        else:
            self.abierta = True

    def cerrarPuerta(self):
        if not self.abierta:
            print('La puerta ya esta cerrada')
        else:
            self.abierta = False
            
            
    def getClosedOpen(self):
        return self.abierta

if __name__ == '__main__':
    puerta1 = Puerta()
        
        
        
        