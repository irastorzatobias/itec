class Cafetera:
    def __init__(self):
        self.capacidadMaxima = 1000
        self.cantidadActual = 0

    def llenarCafetera(self):
        """ Llena la cafetera"""
        self.cantidadActual = self.capacidadMaxima
    
    def servirTaza(self, cantidad):
        """ Simula la accion de servir una taza"""
        if self.cantidadActual > cantidad:
            self.cantidadActual -= cantidad
        else:
            print(f'No quedo tanta cantidad, se lleno la taza con {self.cantidadActual} ml de cafe')
            self.vaciarCafetera()
    
    def vaciarCafetera(self):
        """ Pone la cantidad de cafe en cero"""
        self.cantidadActual = 0
    

    def mostrarCafetera(self):
        return f'Cantidad de cafe disponible: {self.cantidadActual} ml'
    

if __name__ == '__main__':
    cafetera1 = Cafetera()
    print(cafetera1.mostrarCafetera())
    cafetera1.llenarCafetera()
    print(cafetera1.mostrarCafetera())
    cafetera1.servirTaza(300)
    print(cafetera1.mostrarCafetera())
    cafetera1.servirTaza(800)
    print(cafetera1.mostrarCafetera())
