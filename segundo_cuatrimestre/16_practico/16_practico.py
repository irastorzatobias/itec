import PySimpleGUI as sg

def principal_layout():
    filas = [
                [sg.Text('Ventana principal')],
                [sg.Button('OK'), sg.Button('Exit')]
                ]
    return sg.Window('Layout principal', filas, finalize=True)

def secondary_layout():
    filas = [
                [sg.T('Layout secundario')],
                [sg.Button('Salir')]
                ]
    return sg.Window('Layout secundario', filas, finalize=True)



def main():
    principal, secundario = principal_layout(), None
    while True:
        window, event, values = sg.read_all_windows()
        print(event)
        if window == principal and (event == 'Exit' or event == sg.WIN_CLOSED):
            break
        if window == principal and event == 'OK':
            secundario = secondary_layout()
            principal.hide()
        if window == secundario and (event == 'Salir' or event == sg.WIN_CLOSED):
            secundario.hide()
            principal.un_hide()  
    

if __name__ == '__main__':
    main()