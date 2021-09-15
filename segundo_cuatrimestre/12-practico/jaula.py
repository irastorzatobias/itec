from animal import Animal
from puma import Puma
from venado import Venado
from validacion_entero import validacionEntero 

class Jaula:
    def __init__(self,cantAnimales):
        self.cantAnimales = cantAnimales    
        self.animales = []
    
    def setAnimal(self, tipoAnimal, peso, identificador,edad=0):
        """ Agrega animal a la jaula"""
        if len(self.animales) < self.cantAnimales:
            if tipoAnimal.lower() == 'venado':
                self.animales.append(Venado(identificador, peso))
                return f'Se agrego con exito el venado'
            elif tipoAnimal.lower() == 'puma':
                self.animales.append(Puma(identificador, edad, peso))
                return f'Se agrego con exito el puma'
            else:
                return f'No existe ese animal en nuestra base de datos'
        else:
            return f'Ya se agrego el maximo de animales posibles'
    
    def getAdultos(self):
        cantAdultos = 0
        for a in self.animales:
            if type(a) == Puma:
                if a.getAdulto():
                    cantAdultos += 1
            else:
                return f'No se puede obtener cantidad de adultos del animal de tipo {type(a).__name__}' # printea venado
        return f'Cantidad de adultos {cantAdultos}'
    
    
    def getAnimalHealth(self):
        """ Printea la salud del animal"""
        for a in self.animales:
            if a.getHealth():
                print(f'# {a.identificador} - sano')
            else:
                print(f'# {a.identificador} - enfermo')
    
    
    
            

            



if __name__ == '__main__':
    jaulaPumas = Jaula(3)
    jaulaVenados = Jaula(3)
    # Instancio venados
    jaulaVenados.setAnimal('venado',80,1)
    jaulaVenados.setAnimal('venado',130,2)
    jaulaVenados.setAnimal('venado',140,3)
    # Instancio pumas
    jaulaPumas.setAnimal('puma',205,1,4)
    jaulaPumas.setAnimal('puma',23,2,23)
    jaulaPumas.setAnimal('puma',192,3,24)
    print(' -- PUMAS -- ')
    jaulaPumas.getAnimalHealth()
    print(jaulaPumas.getAdultos())
    print('\n')
    print(' -- VENADOS -- ')
    jaulaVenados.getAnimalHealth()
    print(jaulaVenados.getAdultos())
    
        




