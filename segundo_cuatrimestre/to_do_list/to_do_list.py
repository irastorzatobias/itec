import sys
from os import system

from validacion_entero import validacionEntero
from input_string import inputString

def addCategories(categorias):
    """ Hace los archivos necesarios para las categorias especificadas por el usuario"""
    for category in categorias:
        try: 
            with open(f'{category.lower()}.csv','r') as f: # chequea si ya esta la categoria en los csv
                print(f'La categoria {category.lower()} ya existe.')
        except:
            with open(f'{category.lower()}.csv','w') as f:
                f.write('tarea,categoria,fecha,dias restantes')


#def addCategory(categoria):
#    """ agrega una categoria mas a la lista de archivos """
#    try:
#        with open(f'{categoria}.csv','r') as f:
#            return 'Categoria existente'
#    except: 
#        with open(f'{categoria}.csv','w') as f:
#           f.write('tarea,categoria,fecha,dias restantes')


def seguir():
    """ Funcion para determinar si sigue realizando acciones"""
    sigue = ''
    val = False
    while val == False:
        try:
            sigue = input('Desea realizar otra accion? (s/n): ')
            if sigue.lower() == 's':
                val = True
            elif sigue.lower() == 'n':
                print('Salio del programa')
                return val
            else:
                print('Valor invalido, intente nuevamente')
        except:
            print('Error en el input')
    print('Salio del programa')
    return val

def printMenu(opciones):
    for k,v in opciones.items():
        print(f'{k}. {v}')
    pass
            
def menu():
    """ Menu interactivo to_do_list"""
    sigue = True
    opc_user = '' # opcion usuario
    opc_menu = {}
    opc_menu['1'] = 'Agregar categoria/s'
    opc_menu['2'] = 'Agregar TAREA'
    opc_menu['3'] = 'Salir'
    printMenu(opc_menu)
    while sigue:
        try:
            opc_user = validacionEntero('Ingrese su opcion: ', max=4, min=0)
            if opc_user == 1:
                cant = validacionEntero('Cuantas categorias desea agregar: ', max = 10)
                categorias = []
                for i in range(cant):
                    system('cls')
                    categorias.append(inputString(f'Ingrese la categoria numero {i + 1}: '))
                    addCategories(categorias)
                sigue = seguir()
                if sigue:
                    printMenu(opc_menu)
            elif opc_user == 2:
                pass
            elif opc_user == 3:
                sigue = False
        except:
            print('Valor invalido')
    system('cls')
    print('Fin del programa')
    

                                    


def main():
    pass

if __name__ == '__main__':
    
    menu()