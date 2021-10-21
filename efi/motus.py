import PySimpleGUI as sg


people = ['Tobias Irastorza', 'Lautaro Irastorza', 'Pepito Irastorza']

# Layout principal
def principal():
    """ Layout principal """
    columna = [
                [sg.Text('MOTUS',font=('Arial',26))],
                [sg.B('TURNOS', size=(20,1))],
                [sg.B('TURNOS DEL DIA', size=(20,1))],
                [sg.B('ALUMNOS', size=(20,1))],
                ]
    layout = [
                [sg.Column(columna,element_justification='c',p=(0,150))],
                ]
    return sg.Window('MOTUS TRAINING', layout,size=(800,600),finalize=True, element_justification='c')

# Layout de los turnos
def turnos():
    columna = [
                [sg.Text('TURNERO',font=('Arial',26))],
                [sg.B('Anotar turno', size=(20,1))],
                [sg.B('Ver disponibilidad de turnos', size=(20,1))],
                [sg.B('Borrar turnos', size=(20,1))],
                [sg.B('Volver', size=(20,1))],
                ]
    layout = [
        [sg.Column(columna, element_justification='c', p=(0,150))]
    ]
    return sg.Window('TURNOS',layout,size=(800,600),finalize=True, element_justification='c' )


# Layout de los alumnos 
def alumnos():
    columna = [
                [sg.Text('ALUMNOS',font=('Arial',40))],
                [sg.Listbox(people, size=(20,len(people)), key='alumno')],
                [sg.B('Agregar'), sg.B('Modificar'), sg.B('Borrar')],
                [sg.B('Ver', size=(7,1)),sg.B('Volver', size=(7,1))]
                ]
    layout = [
        [sg.Column(columna, element_justification='c', p=(0,150))]
    ]
    return sg.Window('TURNOS',layout,size=(800,600),finalize=True, element_justification='c')
    pass

# En un principio es para modificar a los alumnos
def crud():
    pass

# Layout de rutinas, display y CRUD tambien en lo posible
def rutinas():
    pass
    

sg.theme('DarkBrown4')

def main():
    add = False
    modify = False

    principal_layout, turnos_layout, alumnos_layout, crud_layout, rutinas_layout = principal(), None, None, None, None
    while True:
        window,event, values = sg.read_all_windows()
        if event == 'Exit' or event == sg.WIN_CLOSED:
            break
        # Turnos
        print(event, values)
        if event == 'TURNOS' and window == principal_layout:
            turnos_layout = turnos()
            principal_layout.hide()
        if event == 'Volver' and window == turnos_layout:
            principal_layout.un_hide()
            turnos_layout.hide()
        # Alumnos
        if event == 'ALUMNOS' and window == principal_layout:
            alumnos_layout = alumnos()
            principal_layout.hide()
        if event == 'Volver' and window == alumnos_layout:
            principal_layout.un_hide()
            alumnos_layout.hide()
            
        
            
        

if __name__ == '__main__':
    main()