import PySimpleGUI as sg

layout = [
            [sg.Text('Ingreso de 10 numeros: ')],
            [sg.Text('Numero: ', key='-NUM-'), sg.Input(key='-IN-')],
            [sg.Text('Numero ingresado'),sg.Text(key='-OUT-')],
            [sg.Text('Cantida de numeros ingresados: ', key='-CANT-')],
            [sg.Button('ENTER'), sg.Button('Exit')],
            [sg.Button('Submit', visible=False, bind_return_key=True)]
            ]

window = sg.Window('winTitle', layout) # return_keyboard_events=True

nums = []

while True:
    event, values = window.read()
    print(values['-IN-'])
    if event in [None, 'Exit']:
        break
    elif event == 'ENTER' or event == 'Submit':
        try:
            num = int(values['-IN-'])
            window['-OUT-'].update(num)
            nums.append(num)
            window['-CANT-'].update(f'Cantidad numeros ingresados: {len(nums)}')
        except:
            window['-OUT-'].update('No ingreso un numero')
    if len(nums) == 10:
        sg.popup(f'Numeros mayores a 23 ingresados: {[n for n in nums if n > 23]}')


    

window.close()