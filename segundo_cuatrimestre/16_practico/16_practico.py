import PySimpleGUI as sg

def layout():
    filas = [
                [sg.Text('label1')],
                [sg.Text('label2'), sg.Input(key='label3')],
                [sg.Input(key='label4', enable_events=True)],
                [sg.Button('OK'), sg.Button('Exit')]
                ]

def gui(lay):
    window = sg.Window('winTitle', layout) # return_keyboard_events=True

    while True:
        event, values = window.read()
        if event in [None, 'Exit']:
            break
        

    window.close()

def main():
    gui(layout)

if __name__ == '__main__':
    main()