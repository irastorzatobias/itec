import PySimpleGUI as sg

layout = [
            [sg.Text('Ingrese su nombre: '), sg.Input(key='nombre')],
            [sg.Text(key='output')],
            [sg.Button('OK'), sg.Button('Exit')]
            ]

window = sg.Window('winTitle', layout) # return_keyboard_events=True

while True:
    event, values = window.read()
    if event in [None, 'Exit'] or event == sg.WIN_CLOSED:
        break
    window['output'].update(f'Hola {values["nombre"]}')
    

window.close()