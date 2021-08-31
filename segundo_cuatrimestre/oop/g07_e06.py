from os import system

class Persona:
    def __init__(self, nombre:str, edad:int,sexo:str):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def getNombre(self):
        """ metodo para retornar el nombre de la persona"""
        return self.nombre
    
    
    def esMayor(self):
        """" Metodo para saber si la persona es mayor o menor de edad """
        if self.edad >= 18:
            return 'mayor'
        else:
            return 'menor'

    def getSexo(self):
        """ Metodo para saber si la persona es masculina o femenina"""
        if self.sexo.lower() == 'masculino':
            return 'masculino'
        elif self.sexo.lower() == 'femenino':
            return 'femenino'
        else:
            return 'no se puede determinar su sexo, error en el argumento' 


if __name__ == '__main__':
    persona1 = Persona('Tobias',22,'masculino')
    print(f'{persona1.getNombre()} es {persona1.esMayor()} y es {persona1.getSexo()}')


