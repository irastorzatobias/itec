from tkinter.font import BOLD
import PySimpleGUI as sg


people = [{
    'nombre': 'Tobias Irastorza',
    'turnos': ['Hoy', 'Mañana', 'Pasado']
},
{        
    'nombre': 'Lautaro Irastorza',
    'turnos': ['Lunes', 'Miercoles', 'Viernes']
},
{        
    'nombre': 'Lautaro Martinez',
    'turnos': ['Lunes', 'Jueves','Viernes']
},
]
routines = ['Dia 1', 'Dia 2', 'Dia 3', 'Dia 4', 'Dia 5'] 

peoples_name = [x['nombre'] for x in people]

# Funciones utiles no relacionadas al LAYOUT
def hide_unhide(actual, previous):
    """ Esconde la ventana actual y muestra la ventana anterior pasada como"""
    previous.un_hide()
    actual.hide()
    
def ver_turno(persona):
    text = ''
    for k,v in persona.items():
        if k in 'turnos':
            text += f'{v}\n'
        else:
            text += f'{v} -- '
    return text

# Layout principal
def principal():
    """ Layout principal """
    columna = [
                [sg.Text('MOTUS',font=('Arial',40,BOLD),pad=(0,(0,25)))],
                [sg.B('TURNOS', size=(20,1), pad=(0,(0,25)))],
                [sg.B('RUTINAS', size=(20,1), pad=(0,(0,25)))],
                [sg.B('ALUMNOS', size=(20,1), pad=(0,(0,25)))],
                [sg.B('GESTION CUOTAS', size=(20,1), pad=(0,(0,25)))],
                ]
    layout = [
                [sg.Column(columna,element_justification='c',pad=(0,100))],
                ]
    return sg.Window('MOTUS TRAINING', layout,size=(800,600),finalize=True, element_justification='c')

# Layout de los turnos
def turnos():
    columna = [
                [sg.Text('TURNERO',font=('Arial',40,BOLD), pad=(0,(0,25)))],
                [sg.B('Anotar turno', size=(20,1), pad=(0,(0,25)))],
                [sg.B('Turnos del dia', size=(20,1), pad=(0,(0,25)))],
                [sg.B('Ver turnos', size=(20,1), pad=(0,(0,25)))],
                [sg.B('Borrar turnos', size=(20,1), pad=(0,(0,25)))],
                [sg.B('Volver', size=(20,1), pad=(0,(0,25)))],
                ]
    layout = [
        [sg.Column(columna, element_justification='c', pad=(0,100))]
    ]
    return sg.Window('TURNOS',layout,size=(800,600),finalize=True, element_justification='c' )


# Layout de los alumnos 
def alumnos():
    columna = [
                [sg.Text('ALUMNOS',font=('Arial',40), pad=(0,(0,25)))],
                [sg.Listbox(peoples_name, size=(20,20), key='alumno', pad=(0,(0,25)))],
                [sg.B('Agregar'), sg.B('Modificar'), sg.B('Borrar'),],
                [sg.B('Ver', size=(7,1)),sg.B('Volver', size=(7,1))]
                ]
    layout = [
        [sg.Column(columna, element_justification='c')]
    ]
    return sg.Window('TURNOS',layout,size=(800,600),finalize=True, element_justification='c')
    

# En un principio es para modificar a los alumnos
def crud():
    pass

# Layout de rutinas, display y CRUD tambien en lo posible
def rutinas():
    columna = [
                [sg.Text('RUTINAS',font=('Arial',40))],
                [sg.Listbox(routines, size=(20,len(routines)), key='rutina', pad=(0,(0,25)))],
                [sg.B('Agregar'), sg.B('Modificar'), sg.B('Borrar')],
                [sg.B('Ver', size=(7,1)),sg.B('Volver', size=(7,1))]
                ]
    layout = [
        [sg.Column(columna, element_justification='c', pad=(0,150))]
    ]
    return sg.Window('RUTINAS',layout,size=(800,600),finalize=True, element_justification='c')
    
def display_routine(value):
    columna = [
                [sg.Text(f'RUTINA {value["rutina"][0]}',font=('Arial',40))],
                [sg.B('Volver', size=(7,1))]
                ]
    layout = [
        [sg.Column(columna, element_justification='c', pad=(0,150))]
    ]
    return sg.Window('RUTINAS',layout,size=(800,600),finalize=True, element_justification='c')
    pass

sg.theme('DarkBrown4')

def main():
    add = False
    modify = False
    # layouts de control
    principal_layout, turnos_layout, alumnos_layout, rutinas_layout = principal(), None, None, None
    #layouts de display
    rutina_layout_display = None
    #layouts de modificacion
    crud_layout = None
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
            hide_unhide(turnos_layout, principal_layout)
        if event == 'TURNOS DEL DIA':
            sg.popup('No hay turnos para hoy')
        if event == 'Anotar turno' and window == turnos_layout:
            pass
        if event == 'Ver turnos' and window == turnos_layout:
            texto = ''
            for p in people:
                texto += ver_turno(p)
            sg.popup(texto)
            pass
        # Alumnos
        if event == 'ALUMNOS' and window == principal_layout:
            alumnos_layout = alumnos()
            principal_layout.hide()
        if event == 'Volver' and window == alumnos_layout:
            hide_unhide(alumnos_layout, principal_layout)
        # Rutinas
        if event == 'RUTINAS':
            rutinas_layout = rutinas()
            principal_layout.hide()
        if event == 'Volver' and window == rutinas_layout:
            hide_unhide(rutinas_layout, principal_layout)
        # Viendo rutina
        if event == 'Ver' and window == rutinas_layout:
            rutina_layout_display = display_routine(values)
            rutinas_layout.hide()
        if event == 'Volver' and window == rutina_layout_display:
            hide_unhide(rutina_layout_display, rutinas_layout)
            
        
                

if __name__ == '__main__':
    main()
    # print(peoples_name)