class CargaNombres:
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def cargaNombres(self):
        self.nombres = []
        for i in range(self.cantidad):
            nombre = input(f'Ingrese el nombre {i + 1}: ')
            self.nombres.append(nombre)

    def muestraNombres(self):
        for n in self.nombres:
            print(n)
    

if __name__ == '__main__':
    nombres = CargaNombres(5)
    nombres.cargaNombres()
    nombres.muestraNombres()
    