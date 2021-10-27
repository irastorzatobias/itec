
from tkinter.constants import W
import PySimpleGUI as sg
from datetime import datetime
sg.theme('DarkBrown4')

people = [{
    'nombre': 'Tobias Irastorza',
    'turnos': ['Lunes', 'Miercoles', 'Viernes'],
    'pago': '29/08/2021',
    },
    {        
    'nombre': 'Lautaro Irastorza',
    'turnos': ['Lunes', 'Miercoles', 'Viernes'],
    'pago': '29/08/2021',    
    },
    {        
    'nombre': 'Lautaro Martinez',
    'turnos': ['Lunes', 'Jueves','Viernes'],
    'pago': '29/08/2021', 
    },
    ]
routines = ['Dia 1', 'Dia 2', 'Dia 3', 'Dia 4', 'Dia 5'] 
test = [['Tobias','Irastorza'],['Lautaro','Irastorza'],['Lautaro','Martinez']]

peoples_name = [x['nombre'] for x in people]
    

# Funciones utiles no relacionadas al LAYOUT

def date_from_tuple(fecha):
    """ Devuelve una fecha con formato requerido desde la tupla generada por el sg.popup_get_date()"""
    day = int(fecha[1])
    month = int(fecha[0]) 
    year = int(fecha[2])
    return datetime(year, month, day).strftime("%d/%m/%Y")


def get_alumno(valores):
    """ Devuelve el alumno completo segun el nombre pasado"""
    return people[get_alumno_index(valores['alumno'][0])]

def set_alumno(valores, pList,date):
    """ Recibe los valores de la window actual y los appendea a la lista de personas"""
    turnos = [k.title() for k,v in valores.items() if v == True]
    if len(valores['nombre_alumno']) < 1 or len(turnos) < 1:
        sg.popup('Ingrese todos los datos para continuar')
    else:
        if valores['nombre_alumno'] not in peoples_name:    
            pList.append({
                'nombre': valores['nombre_alumno'],
                'turnos': turnos,
                'pago': date,
            })
            peoples_name.append(valores['nombre_alumno'])
            sg.popup('Alumno agregado con exito')
        else:
            sg.popup('El alumno ya existe')

def modify_alumno(valores, alumno, date):
    """ Modifica los datos de un alumno, recibiendo como argumentos un alumno, y los values de la ventana """
    # Nombre anterior del alumno
    peoples_name[get_alumno_index(alumno['nombre'])] = valores['nombre_alumno']
    alumno['nombre'] = valores['nombre_alumno']
    alumno['turnos'] = [k.title() for k,v in valores.items() if v == True]
    alumno['pago'] = date
    sg.popup('Alumno modificado')
    
        

    
def delete_alumno(valores, window):
    """ Elimina un alumno """
    alumnito = get_alumno(valores)
    peoples_name.remove(alumnito['nombre'])
    people.remove(alumnito)
    window['alumno'].update(peoples_name)

    
def distance_between_dates(date1, date2):
    """ Retorna distancia entre dos fechas en dias"""
    return abs(date2 - date1).days

def filter_by_turn(dict, day):
    """ Retorna un diccionario de las personas con las que coincide el turno de un dia """
    return [x['nombre'] for x in dict if day in x['turnos']]


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
    

def update_turns(valores):
    """ Recibe los valores de la ventana correspondiente a los turnos y los actualiza"""
    days = [k.title() for k,v in valores.items() if v == True] # dias seleccionados
    if len(days) == 0 or valores['alumno'] == []:
        sg.popup('Seleccione al menos un dia / alumno', font=('verdana',13, 'bold'), text_color='#c93c36')
    else:
        pos = get_alumno_index(valores['alumno'][0])
        people[pos].update({'turnos':days})
        sg.popup('Turnos actualizados', font=('verdana',13, 'bold'), text_color='#c93c36')


# Layout principal
def principal():
    """ Layout principal """
    columna = [
                [sg.Text('MOTUS',font=('bahnschrift',65,'bold'),pad=(0,(0,50)))],
                [sg.B('TURNOS', size=(20,2), pad=(0,(0,25)),font=('bahnschrift',13,'bold'))],
                [sg.B('ALUMNOS', size=(20,2), pad=(0,(0,25)),font=('bahnschrift',13,'bold'))],
                [sg.B('RUTINAS', size=(20,2), pad=(0,(0,25)),font=('bahnschrift',13,'bold'))],
                [sg.B('GESTION CUOTAS', size=(20,2), pad=(0,(0,25)),font=('bahnschrift',13,'bold'))],
                [sg.B('SALIR', size=(20,2), pad=(0,(0,25)),font=('bahnschrift',13,'bold'))],
                ]
    layout = [
                [sg.Column(columna,element_justification='c',pad=(0,100))],
                ]
    return sg.Window('MOTUS TRAINING', layout,size=(1024,700),finalize=True, element_justification='c',button_color=('#c93c36'),return_keyboard_events=True)

# Layout de los turnos
def turnos():
    columna = [
                [sg.Text('TURNERO',font=('bahnschrift',65,'bold'), pad=(0,(0,50)))],
                [sg.B('Gestionar turnos', size=(20,2), font=('bahnschrift',13,'bold'), pad=(0,(0,25)))],
                [sg.B('Turnos por dia', size=(20,2), font=('bahnschrift',13,'bold'), pad=(0,(0,25)))],
                [sg.B('Ver turnos', size=(20,2), font=('bahnschrift',13,'bold'), pad=(0,(0,25)))],
                [sg.B('Volver', size=(20,2), font=('bahnschrift',13,'bold'), pad=(0,(0,25)))],
                ]
    layout = [
        [sg.Column(columna, element_justification='c', pad=(0,100))]
    ]
    return sg.Window('TURNOS',layout,size=(1024,700),finalize=True, element_justification='c',button_color=('#c93c36'))

def add_turno():
    """ Modifica turnos mediante uso de Listbox"""
    columna = [
        [sg.Checkbox('LUNES', key='lunes', font=('bahnschrift',13,'bold'))],
        [sg.Checkbox('MARTES', key='martes', font=('bahnschrift',13,'bold'))],
        [sg.Checkbox('MIERCOLES',key='miercoles', font=('bahnschrift',13,'bold'))],
        [sg.Checkbox('JUEVES',key='jueves', font=('bahnschrift',13,'bold'))],
        [sg.Checkbox('VIERNES',key='viernes', font=('bahnschrift',13,'bold'))]
        ]
    
    columna2 = [
        [sg.Listbox(peoples_name, size=(20,20), key='alumno',font=('verdana',13,'bold'), pad=(0,(0,25)))],
    ]
    layout = [
        [sg.Text('GESTION TURNOS', font=('bahnschrift',40,'bold'), pad=(0,(50,50)))],
        [sg.Column(columna2,element_justification='c'),sg.Column(columna, element_justification='c',pad=((50,0),100))],
        [sg.B('Actualizar', size=(20,2), font=('bahnschrift',13,'bold')),sg.B('Volver',size=(20,2), font=('bahnschrift',13,'bold'))]
        ]
    return sg.Window('Agregar turno', layout, size=(1024,700), finalize=True, element_justification='c',button_color=('#c93c36'))

def see_turns():
    """ Genera un nuevo layout con los turnos de los alumnos"""
    people_tuple = [(x['nombre'],x['turnos']) for x in people]
    layout = [
        [sg.T('TURNOS', font=('bahnschrift',65,'bold'),pad=(0,(25,0)))],
        [sg.Table(people_tuple, headings=['Nombre', 'Turnos'],font=('verdana',13,'bold'), key='tabla',col_widths=[30,30],row_height=40,justification='l',auto_size_columns=False, pad=(0,(30,25)),text_color='white', 
                  background_color='#c93c36',hide_vertical_scroll=True)],
        [sg.B('Volver',font=('bahnschrift',13,'bold'),size=(20,2), pad=(0,(0,25)))],
    ]
    return sg.Window('Turnos', layout, size=(1024,700), finalize=True,element_justification='c',button_color=('#c93c36'))

def turns_by_day():
    """ Layout para filtrar turnos por dia"""
    columna1 = [
        [sg.Listbox(size=(25,20), key='alumnos',values=[''], no_scrollbar=True,font=('verdana',13,'bold'), pad=(0,(0,25)))],
    ]
    columna2 = [
        [sg.Radio('LUNES', key='Lunes', font=('bahnschrift',13,'bold'),group_id='dia', default=True)],
        [sg.Radio('MARTES', key='Martes', font=('bahnschrift',13,'bold'),group_id='dia')],
        [sg.Radio('MIERCOLES',key='Miercoles', font=('bahnschrift',13,'bold'),group_id='dia')],
        [sg.Radio('JUEVES',key='Jueves', font=('bahnschrift',13,'bold'),group_id='dia')],
        [sg.Radio('VIERNES',key='Viernes', font=('bahnschrift',13,'bold'),group_id='dia')]
        ]
    layout = [
        [sg.T('TURNOS POR DIA', key='turnos_por_dia',font=('bahnschrift',40,'bold'), pad=(0,(50,50)))],
        [sg.Column(columna1, element_justification='c'),sg.Column(columna2, element_justification='c',pad=((50,0),100))],
        [sg.B('Aplicar',size=(20,2),font=('bahnschrift',13,'bold')), sg.B('Volver',size=(20,2), font=('bahnschrift',13,'bold'))]
    ]
    return sg.Window('Filtrado por dias de turnos',layout,size=(1024,700),finalize=True,element_justification='c',button_color=('#c93c36'))


# Layout de los alumnos 
def alumnos(gente):
    columna = [
                [sg.Text('ALUMNOS',font=('bahnschrift',40,'bold'), pad=(0,(25,30)))],
                [sg.Listbox(peoples_name, size=(20,20), key='alumno',font=('verdana',13,'bold'), pad=(0,(0,25)),no_scrollbar=True)],
                [sg.B('Agregar', font=('bahnschrift',13,'bold')), sg.B('Modificar',font=('bahnschrift',13,'bold')), sg.B('Borrar',font=('bahnschrift',13,'bold')),],
                [sg.B('Ver', size=(7,1), font=('bahnschrift',13,'bold'),),sg.B('Volver', size=(7,1), font=('bahnschrift',13,'bold'),)]
                ]
    layout = [
        [sg.Column(columna, element_justification='c')]
    ]
    return sg.Window('TURNOS',layout,size=(1024,700),finalize=True, element_justification='c',button_color=('#c93c36'))

def add_modify_alumno(action):
    columna = [
        [sg.Text(f'{action.upper()} ALUMNOS',font=('bahnschrift',40,'bold'), pad=(0,(25,50)),key='add_modify_text')],
        [sg.Text('Nombre alumno: ',font=('verdana',13,'bold'),text_color='white'), sg.I(key='nombre_alumno',size=(20,1))],
        
    ]
    columna2 = [
        [sg.Text('Dias que asiste:',font=('verdana',13,'bold'))], 
        [sg.Checkbox('Lunes',key='lunes',font=('verdana',13,'bold'),text_color='white')],
        [sg.Checkbox('Martes',key='martes',font=('verdana',13,'bold'),text_color='white')],
        [sg.Checkbox('Miercoles',key='miercoles',font=('verdana',13,'bold'),text_color='white')],
        [sg.Checkbox('Jueves',key='jueves',font=('verdana',13,'bold'),text_color='white')],
        [sg.Checkbox('Viernes',key='viernes',font=('verdana',13,'bold'),text_color='white')],
    ]
    layout = [
        [sg.Column(columna, element_justification='c',pad=(0,(0,25)))],
        [sg.Column(columna2, element_justification='l',pad=(0,(0,25)))],
        [sg.Button('Fecha de pago',font=('bahnschrift',13,'bold'),size=(20,1),pad=(5,(0,25))), sg.I(key='date',pad=(0,(0,25)),size=(15,1),font=('verdana',13,'bold'),text_color='white')],
        [sg.B(f'{action.upper()}',size=(10,1), font=('bahnschrift',13,'bold')), sg.B('Volver atras',size=(15,1), font=('bahnschrift',13,'bold'))]
    ]
    return sg.Window('AGG ALUMNO',layout, size=(1024,700), finalize=True, element_justification='c',button_color=('#c93c36'))

def display_alumno(values):
    """ Genera un layout con los datos del alumno"""
    alumnito = get_alumno(values)
    text = f'Alumno {alumnito["nombre"]}\nTurnos: {alumnito["turnos"]}\nUltima cuota paga: {alumnito["pago"]}'
    sg.popup(text,title='Alumno',font=('verdana',13,'bold'),button_color=('#c93c36'))

# En un principio es para modificar a los alumnos
def crud():
    pass

# Layout de rutinas, display y CRUD tambien en lo posible
def rutinas():
    columna = [
                [sg.Text('RUTINAS',font=('bahnschrift',35,'bold'),pad=(0,(0,25)))],
                [sg.Listbox(routines, size=(20,len(routines)),font=('verdana',13,'bold'), key='rutina', pad=(0,(0,25)))],
                [sg.B('Modificar',font=('bahnschrift',13,'bold'))],
                [sg.B('Ver', size=(7,1), font=('bahnschrift',13,'bold')),sg.B('Volver',font=('bahnschrift',13,'bold'), size=(7,1))]
                ]
    layout = [
        [sg.Column(columna, element_justification='c', pad=(0,150))]
    ]
    return sg.Window('RUTINAS',layout,size=(1024,700),finalize=True, element_justification='c',button_color=('#c93c36'))
    
def display_routine(value):
    columna = [
                [sg.Text(f'RUTINA {value["rutina"][0]}',font=('Arial',40))],
                [sg.B('Volver', font=('bahnschrift',13,'bold'),size=(7,1))]
                ]
    layout = [
        [sg.Column(columna, element_justification='c', pad=(0,150))]
    ]
    return sg.Window('RUTINAS',layout,size=(1024,700),finalize=True, element_justification='c',button_color=('#c93c36'))
    


def main():

    # layouts de control
    principal_layout, turnos_layout, alumnos_layout, rutinas_layout = principal(), None, None, None 
    add_turno_layout, see_turns_layout, filter_turns, add_alumno_layout = None, None, None, None
    #layouts de displayw
    rutina_layout_display= None
    #layouts de modificacion
    crud_layout = None
    while True:
        window,event, values = sg.read_all_windows()
        if event == 'SALIR' or event == sg.WIN_CLOSED or event == 'Escape:27' and window == principal_layout:
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
            update_turns(values)
        if event == 'Turnos por dia' and window == turnos_layout:
            # Filtrando turnos por dia
            filter_turns = turns_by_day()
            turnos_layout.hide()
        if event == 'Aplicar' and window == filter_turns:
            day = [k for k,v in values.items() if v == True]
            window['turnos_por_dia'].update(f'Turnos del dia {day[0].lower()}')
            window['alumnos'].update(filter_by_turn(people,day[0]))
            
        if event == 'Volver' and window == filter_turns:
            hide_unhide(filter_turns, turnos_layout)
        if event == 'Volver' and window == add_turno_layout:
            # Volviendo desde agregar turnos, al layout de turnos
            hide_unhide(add_turno_layout, turnos_layout)
        if event == 'Ver turnos' and window == turnos_layout:
            # Ver los turnos de las personas
            see_turns_layout = see_turns()
            hide_unhide(turnos_layout, see_turns_layout)
        if event == 'Volver' and window == see_turns_layout:
            hide_unhide(see_turns_layout, turnos_layout)
        # Alumnos
        if event == 'ALUMNOS' and window == principal_layout:
            alumnos_layout = alumnos(people)
            principal_layout.hide()
        if event == 'Agregar' and window == alumnos_layout:
            # Agregando un alumno
            add_alumno_layout = add_modify_alumno('agregar')
            alumnos_layout.hide() 
        if event == 'Fecha de pago' and window == add_alumno_layout:
            fecha = sg.popup_get_date()
            fecha = date_from_tuple(fecha)
            add_alumno_layout['date'].update(fecha)
        if event == 'AGREGAR' and window == add_alumno_layout:
            # En el layout, ya agregando el alumno
            set_alumno(values, people, fecha)
        if event == 'Modificar' and window == alumnos_layout:
            # Modificando un alumno
            try:
                student = get_alumno(values)
            except:
                sg.popup('No selecciono alumno para modificar')
            else:
                add_alumno_layout = add_modify_alumno('modificar')
                add_alumno_layout['add_modify_text'].Update(f'Modificando a {student["nombre"]}')
                alumnos_layout.hide()
        if event == 'MODIFICAR' and window == add_alumno_layout:
            # Ya en el layout de modificacion de alumno
            try:
                modify_alumno(values, student, fecha)
            except:
                sg.popup('Faltan datos que completar')
        if event == 'Borrar' and window == alumnos_layout:
            # Borrando un alumno
            print(values)
            if len(values['alumno']) < 1:
                sg.popup('No selecciono ningun alumno',font=('verdana',13),text_color='white')
            elif len(peoples_name) >= 1:
                delete_alumno(values, alumnos_layout)
            else:
                sg.popup('No hay mas alumnos para borrar',font=('verdana',13),text_color='white')
        if event == 'Volver atras' and window == add_alumno_layout:
            hide_unhide(add_alumno_layout, principal_layout)
        if event == 'Ver' and window == alumnos_layout:
            # Popup de alumno seleccionado
            try:
                display_alumno(values)
            except IndexError:
                sg.popup('No selecciono ningun alumno',font=('verdana',13),text_color='white')
        if event == 'Volver' and window == alumnos_layout:
            # Volviendo de layout de alumnos al layout principal
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
    # print(datetime.today().strftime("%d/%m/%Y"))