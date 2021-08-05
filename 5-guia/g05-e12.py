def cargarPersonas(cant, nombres, nacimientos):
    for i in range(cant):
        print('Ingrese el nombre de la persona',i)
        nombres.append(input())
        print('Ingrese la fecha de nacimiento (dd/mm/aaaa)')
        nacimientos.append(input())
        if ('/' not in nacimientos[i]) or (len(nacimientos[i]) < 10):
            print('Formato incorrecto, intente de nuevo')
            print('Fecha de nacimiento')
            nacimientos[i] = input()
def mayores(nombres, nacimientos):
    mayores = []
    nacimientosSplit = 0
    for i in range(len(nacimientos)):
        nacimientoSplit = nacimientos[i].split("/")
        if int(nacimientoSplit[2]) <= 2003:
            mayores.append(nombres[i])
    return mayores
        
if __name__ == '__main__':
    nombrePersonas = []
    nacimientoPersonas = []
    cargarPersonas(3,nombrePersonas,nacimientoPersonas)
    mayoresDeEdad = mayores(nombrePersonas, nacimientoPersonas)
    print(' -- LISTA DE MAYORES DE EDAD -- ')
    print(mayoresDeEdad)