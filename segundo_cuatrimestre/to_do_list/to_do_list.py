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
          f.write('tarea,categoria,fecha')

def getCategories(): 
    """ A partir de los archivos csv creados, obtiene las categorias de las tareas """
    categories = os.listdir('.')
    categories = list(filter(lambda x: ('.csv' in x), categories)) 
    categories = list(map(lambda x: x[0:-4], categories))
    return categories


def getTasks(file):
    """" Obtiene las tareas del archivo especificado """
    lineas = []      
    tasks = []
    final = []
    try:
        with open(file) as f:
            content = f.readlines() # lista con valores csv
            for i in range(1,len(content)):
                tasks.append(content[i].strip())
            for e in tasks:
                aux = e.split(',')
                final.append({
                    'tarea' : aux[0],
                    'categoria': aux[1],
                    'fecha': aux[2]
                })
    except:
        return 'No se encontro el archivo'
    else:
        return final
    
def getAllTasks():
    """ Obtiene todas las tareas de las categorias especificadas por el usuario """
    categories = getCategories()
    all_tasks = []
    for category in categories:
        aux = getTasks(f'{category}.csv')
        all_tasks += aux
    return all_tasks
     
def addTask():
    """ Agrega tarea al archivo de categoria correspondiente"""
    categories = getCategories()
    chosen_category = ''
    task = {}
    if len(categories) > 1:
        print('-- CATEGORIAS DISPONIBLES --')
        for category in categories:
            print(f'{category.title()}')
        while chosen_category.lower() not in categories:
            chosen_category = input('A que categoria corresponde su tarea?: ')
        if chosen_category.lower() not in categories:
            system('cls')
            print('La categoria no existe, intente nuevamente')
        else:
            system('cls')
            print('-- AGREGANDO CATEGORIA --')
            task['tarea'] = inputString('Descripcion de la tarea: ')
            task['categoria'] = chosen_category
            task['fecha'] = validarFecha() # fecha formato datetime con hora incluida
            # task['horas restantes'] = 
            task['fecha'] = task['fecha'].strftime('%d-%m-%Y %H:%M') # le doy el formato correcto a la fecha 
            with open(f'{chosen_category}.csv','a') as f:
                f.write('\n') # printeo salto de lineas
                for k,v in task.items():
                    if k == 'fecha': # si la key es dias restantes, no le agrego coma, ya que es la ultima
                        f.write(str(v))
                    else:
                        f.write(f'{v},')
        return task
    else:
        return 'NO EXISTEN CATEGORIAS, VUELVA AL MENU PARA AGREGAR ALGUNA'

def getDeadlines():
    tasks = getAllTasks()
    deadlines = []
    for task in tasks:
        aux = datetime.strptime(task['fecha'],"%d-%m-%Y %H:%M") - datetime.today()
        deadlines.append(aux.days)
        print(f'TAREA: {task["tarea"]}')
        print(f'CATEGORIA: {task["categoria"]}')
        print(f'Tiempo restante: {aux}\n')
    



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
            fecha = datetime.strptime(fecha, '%d-%m-%Y %H:%M')
            if fecha < today:
                system('cls')
                print('Fecha anterior al dia de hoy, intente nuevamente')
            else:
                val = True
        except:
            print('El formato no coincide con dd-mm-aaaa hh:mm')     
    return fecha



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
    while sigue:
        try:
            system('cls')
            printMenu(opc_menu)
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
                addTask()
                sigue = seguir()
                if sigue:
                    printMenu(opc_menu)
            elif opc_user == 3:
                sigue = False
        except:
            print('Valor invalido')
    system('cls')
    print('Fin del programa')
    

                                    


def main():
    getDeadlines()


    

if __name__ == '__main__':
    main()