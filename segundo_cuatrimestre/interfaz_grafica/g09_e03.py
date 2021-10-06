import PySimpleGUI as sg

layout = [
            [sg.Text('Cantidad de personas a cargar: '), sg.Input(key='-CANT-')],
            [sg.Button('OK'), sg.Button('Exit')]
            ]

window = sg.Window('winTitle', layout) # return_keyboard_events=True

while True:
    event, values = window.read()
    if event in [None, 'Exit']:
        break
    elif event == 'OK':
        cantPersonas = int(values['-CANT-'])
        i = 1
        ePersonas = []
        while int(cantPersonas) > 0:
            edad = int(sg.popup_get_text(f'Edad de la persona {i} : '))
            ePersonas.append(edad)
            i += 1 
            cantPersonas -= 1
        sg.popup(f'Promedio edad personas: {sum(ePersonas) / len(ePersonas)}')   

window.close()