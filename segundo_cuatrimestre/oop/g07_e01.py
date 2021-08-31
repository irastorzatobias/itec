class Telefono:
    def __init__(self, marca:str, modelo:str, costoMensual:int):
        self.marca = marca
        self.modelo = modelo
        self.costoMensual = costoMensual
    
    def getCostoAnual(self):
        return self.costoMensual * 12
    
if __name__ == '__main__':
    lg = Telefono('lg','k2017',500)
    print(lg.getCostoAnual())
    


    