class Ventana:
    def __init__(self):
        self.open = True
    
    def abrirVentana(self):
        if self.open == True:
            print('La ventana ya está abierta')
        else:
            self.open = True
    
    def cerrarVentana(self):
        if self.open == False:
            print('La ventana ya esta cerrada')
        else:
            self.open = False
    
    def getWindowState(self):
        return self.open