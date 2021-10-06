import PySimpleGUI as sg

def suma(a,b):
    """ Suma dos numeros"""
    return a + b


layout = [ [sg.Text('Sumar dos numeros y mostrar resultado: ')],
           [sg.Text('Numero 1: '),sg.InputText(key='-N1-')],
           [sg.Text('Numero 2: '),sg.InputText(key='-N2-')],
           [sg.Text('RESULTADO:'),sg.Text(key='-RESULTADO-')],
           [sg.Button('OK'),sg.Button('Exit')]
           ]

window = sg.Window('Suma dos numeros', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    try:
        window['-RESULTADO-'].Update(suma(int(values['-N1-']),int(values['-N2-'])))
    except:
        window['-RESULTADO-'].Update('No ingreso numeros')
window.close()

