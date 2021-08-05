import sys
import os
from os import system
from datetime import datetime

from validacion_entero import validacionEntero
from input_string import inputString

#def addCategories(categorias):
#    """ Hace los archivos necesarios para las categorias especificadas por el usuario"""
#    for category in categorias:
#        try: 
#            with open(f'{category.lower()}.csv','r') as f: # chequea si ya esta la categoria en los csv
#                print(f'La categoria {category.lower()} ya existe.')
#        except:
#            with open(f'{category.lower()}.csv','w') as f:
#                f.write('tarea,categoria,fecha,dias restantes')


def addCategory(category):
    """ agrega una categoria mas a la lista de archivos """
    try:
       with open(f'{category}.csv','r') as f:
            return 'Categoria existente'
    except: 
        with open(f'{category}.csv','w') as f:
          f.write('tarea,categoria,fecha,dias restantes')

def getCategories(): 
    """ A partir de los archivos csv creados, obtiene las categorias de las tareas """
    files = os.listdir('.')
    files = list(filter(lambda x: ('.csv' in x), files)) 
    files = list(map(lambda x: x[0:-4], files))
    print('-- CATEGORIAS -- ')
    for e in files:
        print(f'{e.title()}')


def addTask():
    """ Agrega tarea al archivo de categoria correspondiente"""
    categories = getCategories()
    try:
        with open(f'{categories}.csv') as f:
            pass
    except:
        return 'La categoria no existe, intente nuevamente'
    else:
        with open(f'{categories}.csv','a') as f:
            task = {}
            task['description'] = inputString('Ingrese la tarea: ')
            task['fecha'] = validarFecha('Fecha a cumplir: ')
            
    

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

def validarFecha():
    """ Validar fecha especifico para este programa, chequea que la fecha sea mayor al dia de hoy"""
    val = False
    today = datetime.today()
    while val == False:
        try:
            fecha = input('Ingrese fecha a cumplir: ')
            fecha = datetime.strptime(fecha, '%d-%m-%Y')
            if fecha < today:
                system('cls')
                print('Fecha anterior al dia de hoy, intente nuevamente')
            else:
                val = True
        except:
            print('El formato no coincide con dd-mm-aaaa')     
    print(fecha.strftime('%d-%m-%Y'))
    print(datetime.today().strftime('%d-%m-%Y'))

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
            opc_user = validacionEntero('Ingrese su opcion: ', max=len(opc_menu.keys()))
            if opc_user == 1:
                cant = validacionEntero('Cuantas categorias desea agregar: ', max = 10)
                for i in range(cant):
                    system('cls')
                    categoria = inputString(f'Ingrese la categoria numero {i + 1}: ')
                    addCategory(categoria)
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
    #menu()
    validarFecha()
    pass

if __name__ == '__main__':
    main()