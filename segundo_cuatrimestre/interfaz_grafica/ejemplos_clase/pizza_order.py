import PySimpleGUI as sg


# Crear layout
def login():
    col1 = [[sg.T('Hola amigos')]]
    col2 = [
        [sg.T('None')],
        [sg.I(key='Usuario')],
        [sg.Button('Continuar'), sg.Button('Salir')]
    ]
    layout = [[sg.Stretch(),sg.Column(col1, element_justification='l'),sg.Column(col2, element_justification='r'), sg.Stretch(),]]
    
    return sg.Window('Login', layout, finalize=True, size=(640,480))
# Loop lectura eventos
# Logica al clickear los botones

def layout_pedido():
    sg.theme('Reddit')
    layout = [
        [sg.T('Hacer pedido')],
        [sg.Checkbox('Pizza pepperoni', key='pizza1'), sg.Checkbox('Pizza mozzarella', key='pizza2')],
        [sg.Button('Volver')]
    ]
    return sg.Window('Pedido',layout, finalize=True)

def main():
    nombre, pedido = login(), None
    while True:
        window, event, values = sg.read_all_windows()
        # Primer layout
        if window == nombre and event == 'Salir' or event == sg.WIN_CLOSED:
            break
        # Ir al segundo layout
        if window == nombre and event == 'Continuar':
            pedido = layout_pedido()
            nombre.hide()
        if window == pedido and event == 'Volver':
            pedido.hide()
            nombre.un_hide()
        
            
    


if __name__ == '__main__':
    main()
    

