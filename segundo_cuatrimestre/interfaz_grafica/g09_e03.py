import PySimpleGUI as sg

def valInt(values, key):
    try:
        int(values[key])
    except:
        return False
    else:
        return True
    
def valFloat(values, key):
    try:
        float(values[key])
    except:
        return False
    else:
        return True


def firstLayout():
    " Primer layout con sus acciones correspondientes"
    filas = [
                [sg.Text('Cantidad de personas a cargar')],
                [sg.Input(key='cantP')],
                [sg.Button('OK',  bind_return_key=True), sg.Button('Exit')]
                ]
    return filas

def secondLayout(values):
    """ Segundo layout con sus acciones correspondientes """
    filas = [
        [
            sg.Text(f"Edad de la persona {fila+1}: ", size=(30, 1)),
            sg.Input(key=f"entero_edad_{fila+1}: ", size=(3, 1)),
        ]
        for fila in range(int(values["cantP"]))
    ]
    filas.append([sg.Button('Ok',  bind_return_key=True), sg.T(key=('promedio'))])
    window2 = sg.Window('segunda ventana',filas)
    while True:
        event2,values2 = window2.read()
        " Dejo abierta solo la segunda pestaña"
        if event2 in [sg.WIN_CLOSED, 'Salir']:  
            break
        elif event2 in 'Ok':
            try:
                # obtengo las edades
                edades = [int(x) for x in values2.values()]
            except:
                sg.popup('Falto un dato de ingresar, o no ingreso entero')
            else:
                window2['promedio'].update(f'Promedio de las edades ingresadas: {sum(edades) / len(edades)}')
    
def gui(lay):
    """ Programa en general """
    window = sg.Window('winTitle', firstLayout()) 
    while True:
        event, values = window.read()
        if event in [None, 'Exit']:
            break
        elif event in 'OK':
            if not valInt(values, 'cantP'):
                sg.popup('No ingreso entero')
            else:
                secondLayout(values)
    window.close()
                        
                        

def main():
    gui(firstLayout())

if __name__ == '__main__':
    main()
