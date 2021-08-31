from os import system

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def getName(self):
        return self.nombre.title()
    
    def getAge(self):
        return self.edad

if __name__ == '__main__':
    personas = []
    sigue = ''
    while True:
        try:
            name = input('Ingrese un nombre: ')
            edad = int(input('Ingrese una edad: '))
        except:
            system('cls')
            print('No ingreso un valor, numerico, intente nuevamente')
        else:
            personas.append(Persona(name,edad))
            sigue = input('Desea agregar otro nombre? (s/n): ')
            if sigue == 'n':
                break
    i = 1
    for p in personas:
        print(f'Persona {i}: {p.getName()} {p.getAge()} años')