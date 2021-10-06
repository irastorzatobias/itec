import PySimpleGUI as sg

layout = [
            [sg.Text('label1')],
            [sg.Text('Ingresa algo'), sg.Input(key='label3')],
            [sg.Text('Output aca: ',size=(30,1), key = '-OUT-')],
            [sg.Button('OK'), sg.Button('Exit')]
            ]

window = sg.Window('winTitle', layout, location=(2500, 500)) # return_keyboard_events=True

while True:
    event, values = window.read()
    if event in [None, 'Exit']:
        break
    window['OUT'].update(values['-OUT-'])
    

window.close()