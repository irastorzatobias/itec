class Telefono:
    def __init__(self,marca:str,modelo:str,os:str,costoPlan:int,ram:int):
        self.marca = marca
        self.modelo = modelo
        self.os = os
        self.costoPlan = costoPlan
        self.ram = ram
    

    def getCostoAnual(self):
        """ Retorna el costo anual del telefono"""
        return self.costoPlan * 12
    

    def getOS(self):
        """ Retorna el sistema operativo del telefono"""
        return self.os
    
    def checkHighEnd(self):
        """ Retorna si el  telefono es de alta gana o no"""
        if self.ram >= 6:
            return f'El modelo es gama alta, posee {self.ram} gb de RAM'
        else:
            return f'El modelo no es gama alta, posee {self.ram} gb de RAM'

if __name__ == '__main__':
    myPhone = Telefono('Samsung','A7','Android',300,3) 
    print('Costo anual: ')
    print(myPhone.getCostoAnual())
    print(f'Sistema operativo del telefono: {myPhone.getOS()}')
    print(myPhone.checkHighEnd())