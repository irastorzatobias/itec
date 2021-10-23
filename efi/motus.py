from tkinter.font import BOLD
import PySimpleGUI as sg
from datetime import datetime
sg.theme('DarkBrown4')

people = [{
    'nombre': 'Tobias Irastorza',
    'turnos': ['Hoy', 'Mañana', 'Pasado'],
    'pago': '29/08/2021',
    'cuota':False
},
{        
    'nombre': 'Lautaro Irastorza',
    'turnos': ['Lunes', 'Miercoles', 'Viernes'],
    'pago': '29/08/2021',
    'cuota':False
    
},
{        
    'nombre': 'Lautaro Martinez',
    'turnos': ['Lunes', 'Jueves','Viernes'],
    'pago': '29/08/2021', 
    'cuota':False  
},
]
routines = ['Dia 1', 'Dia 2', 'Dia 3', 'Dia 4', 'Dia 5'] 

peoples_name = [x['nombre'] for x in people]

# Funciones utiles no relacionadas al LAYOUT
def distance_between_dates(date1, date2):
    """ Retorna distancia entre dos fechas en dias"""
    return abs(date2 - date1).days

def filter_by_turn(dict, day):
    """ Retorna un diccionario de las personas con las que coincide el turno de un dia """
    return [x for x in dict if day in x['turnos']]


def get_day_name(date):
    """ Retorna el nombre del dia pasandole una fecha como parametro """
    day_name = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes','Sabado','Domingo']
    return day_name[date.weekday()]

def hide_unhide(actual, target):
    """ Esconde la ventana actual y muestra la ventana pasada como target"""
    target.un_hide()
    actual.hide()
    
def ver_turno(persona):
    """ Printea los turnos de las personas """
    text = ''
    for k,v in persona.items():
        # Exceptuo los items cuota y pago
        if k in 'turnos':
            text += f'{v}\n'
        elif k in 'nombre':
            text += f'{v} -- '
    return text

def get_alumno_index(name):
    """ Retorna el index del alumno """
    for i,x in enumerate(peoples_name):
        if x == name:
            return i
    

# Layout principal
def principal():
    """ Layout principal """
    columna = [
                [sg.Text('MOTUS',font=('webhostinghub-glyphs',40,'bold'),pad=(0,(0,25)))],
                [sg.B('TURNOS', size=(15,2), font=('webhostinghub-glyphs',10,'bold'), pad=(0,(0,25)))],
                [sg.B('ALUMNOS', size=(15,2), font=('webhostinghub-glyphs',10,'bold'), pad=(0,(0,25)))],
                [sg.B('RUTINAS', size=(15,2), font=('webhostinghub-glyphs',10,'bold'), pad=(0,(0,25)))],
                [sg.B('GESTION CUOTAS', size=(15,2), font=('webhostinghub-glyphs',10,'bold'), pad=(0,(0,25)))],
                [sg.B('SALIR', size=(15,2), font=('webhostinghub-glyphs',10,'bold'),pad=(0,(0,25)))],
                ]
    layout = [
                [sg.Column(columna,element_justification='c',pad=(0,100))],
                ]
    return sg.Window('MOTUS TRAINING', layout,size=(800,600),finalize=True, element_justification='c',button_color=('#c93c36'))

# Layout de los turnos
def turnos():
    columna = [
                [sg.Text('TURNERO',font=('Courier New',40,'bold'), pad=(0,(0,25)))],
                [sg.B('Gestionar turnos', size=(15,2), font=('webhostinghub-glyphs',10,'bold'), pad=(0,(0,25)))],
                [sg.B('Turnos del dia', size=(15,2), font=('webhostinghub-glyphs',10,'bold'), pad=(0,(0,25)))],
                [sg.B('Ver turnos', size=(15,2), font=('webhostinghub-glyphs',10,'bold'), pad=(0,(0,25)))],
                [sg.B('Volver', size=(15,2), font=('webhostinghub-glyphs',10,'bold'), pad=(0,(0,25)))],
                ]
    layout = [
        [sg.Column(columna, element_justification='c', pad=(0,100))]
    ]
    return sg.Window('TURNOS',layout,size=(800,600),finalize=True, element_justification='c',button_color=('#c93c36'))

def add_turno():
    columna = [
        [sg.Checkbox('LUNES', key='lunes', font=(''))],
        [sg.Checkbox('MARTES', key='martes')],
        [sg.Checkbox('MIERCOLES',key='miercoles')],
        [sg.Checkbox('JUEVES',key='jueves')],
        [sg.Checkbox('VIERNES',key='viernes')],
        ]
    
    columna2 = [
        [sg.Listbox(peoples_name, size=(20,20), key='alumno', pad=(0,(0,25)))],
    ]
    layout = [
        [sg.Text('AGREGANDO TURNO', font=('Arial',30))],
        [sg.Column(columna2,element_justification='c'),sg.Column(columna, element_justification='c', pad=((50,0),100))],
        [sg.B('Actualizar', size=(15,2), font=('webhostinghub-glyphs',10,'bold')),sg.B('Volver',size=(15,2))]
        ]
    return sg.Window('Agregar turno', layout, size=(800,600), finalize=True, element_justification='c',button_color=('#c93c36'))


# Layout de los alumnos 
def alumnos():
    columna = [
                [sg.Text('ALUMNOS',font=('Arial',40), pad=(0,(0,25)))],
                [sg.Listbox(peoples_name, size=(20,20), key='alumno', pad=(0,(0,25)))],
                [sg.B('Agregar', font=('webhostinghub-glyphs',10,'bold')), sg.B('Modificar',font=('webhostinghub-glyphs',10,'bold')), sg.B('Borrar',font=('webhostinghub-glyphs',10,'bold')),],
                [sg.B('Ver', size=(7,1), font=('webhostinghub-glyphs',10,'bold'),),sg.B('Volver', size=(7,1), font=('webhostinghub-glyphs',10,'bold'),)]
                ]
    layout = [
        [sg.Column(columna, element_justification='c')]
    ]
    return sg.Window('TURNOS',layout,size=(800,600),finalize=True, element_justification='c',button_color=('#c93c36'))
    

# En un principio es para modificar a los alumnos
def crud():
    pass

# Layout de rutinas, display y CRUD tambien en lo posible
def rutinas():
    columna = [
                [sg.Text('RUTINAS',font=('Arial',40))],
                [sg.Listbox(routines, size=(20,len(routines)), key='rutina', pad=(0,(0,25)))],
                [sg.B('Agregar', font=('webhostinghub-glyphs',10,'bold')), sg.B('Modificar',font=('webhostinghub-glyphs',10,'bold')), sg.B('Borrar',font=('webhostinghub-glyphs',10,'bold'))],
                [sg.B('Ver', size=(7,1), font=('webhostinghub-glyphs',10,'bold')),sg.B('Volver',font=('webhostinghub-glyphs',10,'bold'), size=(7,1))]
                ]
    layout = [
        [sg.Column(columna, element_justification='c', pad=(0,150))]
    ]
    return sg.Window('RUTINAS',layout,size=(800,600),finalize=True, element_justification='c',button_color=('#c93c36'))
    
def display_routine(value):
    columna = [
                [sg.Text(f'RUTINA {value["rutina"][0]}',font=('Arial',40))],
                [sg.B('Volver', font=('webhostinghub-glyphs',10,'bold'),size=(7,1))]
                ]
    layout = [
        [sg.Column(columna, element_justification='c', pad=(0,150))]
    ]
    return sg.Window('RUTINAS',layout,size=(800,600),finalize=True, element_justification='c',button_color=('#c93c36'))
    


def main():
    add = False
    modify = False
    # layouts de control
    principal_layout, turnos_layout, alumnos_layout, rutinas_layout, add_turno_layout = principal(), None, None, None, None
    #layouts de display
    rutina_layout_display = None
    #layouts de modificacion
    crud_layout = None
    while True:
        window,event, values = sg.read_all_windows()
        if event == 'SALIR' or event == sg.WIN_CLOSED:
            break
        # Turnos
        if event == 'TURNOS' and window == principal_layout:
            # Ventana principal turnos
            turnos_layout = turnos()
            principal_layout.hide()
        if event == 'Volver' and window == turnos_layout:
            # Volviendo desde turnos a la ventana principal
            hide_unhide(turnos_layout, principal_layout)
        if event == 'Gestionar turnos' and window == turnos_layout:
            # Anotando turnos
            add_turno_layout = add_turno()
            turnos_layout.hide()
        if event == 'Actualizar' and window == add_turno_layout:
            # Actualizando turnos del alumno
            pos = get_alumno_index(values['alumno'][0])
            print(pos)
            days = [k.title() for k,v in values.items() if v == True] # dias seleccionados
            print(days)
            if len(days) == 0 or values['alumno'] == []:
                sg.popup('Seleccione al menos un dia / alumno', font=(20))
            else:
                people[pos].update({'turnos':days})
                sg.popup('Turnos actualizados', font=(20))
        if event == 'Turnos del dia' and window == turnos_layout:
            # Chequeando turnos del dia
            dia = get_day_name(datetime.today())
            day_turns = filter_by_turn(people, dia) 
            if len(day_turns) == 0:
                sg.popup(f'No hay turnos para el dia {dia}',font=(20))
            else:
                texto = f'Personas que asisten el dia de la fecha:\n'
                for p in day_turns:
                    texto += f'{p["nombre"]}\n'
                sg.popup(texto,font=(20))
        if event == 'Volver' and window == add_turno_layout:
            # Volviendo desde agregar turnos, al layout de turnos
            hide_unhide(add_turno_layout, turnos_layout)
        if event == 'Ver turnos' and window == turnos_layout:
            # Ver los turnos de las personas
            texto = ''
            for p in people:
                texto += ver_turno(p)
            sg.popup(texto, font=(20))
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
    # print(distance_between_dates(datetime.today(), datetime.strptime(people[0]['cuota'],'%d/%m/%Y')))