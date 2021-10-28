
import PySimpleGUI as sg
from datetime import datetime

import controller as sql

sg.theme('DarkBrown4')

# Trabajando con BD     
def get_data_from_db(dbName, tableName):
    """ Recibe los datos de la BD y los devuelve como un diccionario para mejor representacion de los datos"""
    data = sql.readRows(dbName, tableName)
    people = []
    for x in data:
        nombre = x[0]   
        turnos = x[1].split(',')
        turnos = [t.title() for t in turnos]
        pago = x[2]    
        people.append({
            'nombre':nombre,
            'turnos':turnos,
            'pago':pago
        })
    return people

def get_people_name(dbName, tableName):
    """ Retorna el nombre de las personas """
    data = get_data_from_db(dbName, tableName)
    return [x['nombre'] for x in data]

def format_data_from_db(tuplaList):

    if len(tuplaList) == 1: # En caso de que sea una sola persona
        persona = {}
        nombre = tuplaList[0][0]   
        turnos = tuplaList[0][1].split(',')
        turnos = [t.title() for t in turnos]
        pago = tuplaList[0][2]    
        persona = {
                'nombre':nombre,
                'turnos':turnos,
                'pago':pago
                }
        return persona
    elif len(tuplaList) > 1: # En caso de que sea mas de una persona
        persona = []
        for p in tuplaList:
                nombre = p[0]   
                turnos = p[1].split(',')
                turnos = [t.title() for t in turnos]
                pago = p[2]    
                persona.append({
                    'nombre':nombre,
                    'turnos':turnos,
                    'pago':pago
                })
        return persona


def get_alumno(nombre):
    """ Devuelve el alumno completo segun el nombre pasado"""
    data = sql.search('motus','alumnos',f'name = "{nombre}"')
    data = format_data_from_db(data)
    return data

# Funciones utiles no relacionadas al LAYOUT
    
def date_from_tuple(fecha):
    """ Devuelve una fecha con formato requerido desde la tupla generada por el sg.popup_get_date()"""
    day = int(fecha[1])
    month = int(fecha[0]) 
    year = int(fecha[2])
    return datetime(year, month, day).strftime("%d/%m/%Y")

def reset_listbox(window,pagos=False):
    """ Resetea la listbox o tabla de alumnos, con nombres. O con pagos, en caso de que sea la tabla correspondiente al apartado ESTADO CUOTAS"""
    personas =  get_data_from_db('motus','alumnos')
    if pagos:
        people_tuple = [(x['nombre'],x['pago']) for x in personas]
        window['alumno'].update(people_tuple)
    else:
        people_name = [x['nombre'] for x in personas]
        window['alumno'].update(people_name)



def set_alumno(valores,date):
    """ Recibe los valores de la window actual y los appendea a la lista de personas"""
    turnos = [k.title() for k,v in valores.items() if v == True]
    turnos_text = ','.join(turnos)
    if len(valores['alumno']) < 1 or len(turnos) < 1:
        sg.popup('Ingrese todos los datos para continuar')
    else:
        try:
            sg.popup(sql.insertRow('motus','alumnos',valores['alumno'],turnos_text,date))
        except:
            sg.popup('Error al cargar usuario')
            
            
def modify_alumno(valores, nombre, date):
    """ Modifica los datos de un alumno, recibiendo como argumentos un alumno, y los values de la ventana """
    nName = valores['alumno']
    turnos = [k.title() for k,v in valores.items() if v == True]
    turnos_text = ','.join(turnos)
    sql.updateFields(nombre,nName,turnos_text,date)
    
def filter_by_name(name):
    """ Recibe un nombre y filtra los que coincidan con ese nombre u parte de ese nombre"""
    data = sql.search('motus','alumnos',f'name LIKE "%{name}%"')
    result = format_data_from_db(data)
    if type(result).__name__ == 'dict':
        return [result["nombre"]]
    elif type(result).__name__ == 'list':
        return [x['nombre'] for x in result]
    else:
        return 0
    
def delete_alumno(valores):
    """ Elimina un alumno """
    nombre = valores['alumno'][0]
    sql.deleteRow(f'name = "{nombre}"')
    sg.popup('Alumno eliminado')
    

def filter_by_turn(day):
    """ Retorna un diccionario de las personas con las que coincide el turno de un dia """
    data = get_data_from_db('motus','alumnos')
    return [x['nombre'] for x in data if day in x['turnos']]

def hide_unhide(actual, target):
    """ Esconde la ventana actual y muestra la ventana pasada como target"""
    target.un_hide()
    actual.hide()

    

def update_turns(valores):
    """ Recibe los valores de la ventana correspondiente a los turnos y los actualiza"""
    days = [k.title() for k,v in valores.items() if v == True] # dias seleccionados
    if len(days) == 0 or valores['alumno'] == []:
        sg.popup('Seleccione al menos un dia / alumno', font=('arial',13, 'bold'), text_color='#c93c36')
    else:
        days_text = ','.join(days)
        alumno = get_alumno(valores['alumno'][0])
        sql.updateTurns(alumno['nombre'], days_text)
        sg.popup('Turnos actualizados', font=('arial',13, 'bold'), text_color='#c93c36')


# Layout principal
def principal():
    """ Layout principal """
    columna = [
                [sg.Text('MOTUS',font=('arial',65,'bold'),pad=(0,(0,50)))],
                [sg.B('TURNOS', size=(20,2), pad=(0,(0,25)),font=('arial',13,'bold'))],
                [sg.B('ALUMNOS', size=(20,2), pad=(0,(0,25)),font=('arial',13,'bold'))],
                [sg.B('RUTINAS', size=(20,2), pad=(0,(0,25)),font=('arial',13,'bold'))],
                [sg.B('ESTADO CUOTAS', size=(20,2), pad=(0,(0,25)),font=('arial',13,'bold'))],
                [sg.B('SALIR', size=(20,2), pad=(0,(0,25)),font=('arial',13,'bold'))],
                ]
    layout = [
                [sg.Column(columna,element_justification='c',pad=(0,50))],
                ]
    return sg.Window('MOTUS TRAINING', layout,size=(1024,700),finalize=True, element_justification='c',button_color=('#c93c36'),return_keyboard_events=True)

# Layout de los turnos
def turnos():
    columna = [
                [sg.Text('TURNERO',font=('arial',65,'bold'), pad=(0,(0,50)))],
                [sg.B('Gestionar turnos', size=(20,2), font=('arial',13,'bold'), pad=(0,(0,25)))],
                [sg.B('Turnos por dia', size=(20,2), font=('arial',13,'bold'), pad=(0,(0,25)))],
                [sg.B('Ver turnos', size=(20,2), font=('arial',13,'bold'), pad=(0,(0,25)))],
                [sg.B('Volver', size=(20,2), font=('arial',13,'bold'), pad=(0,(0,25)))],
                ]
    layout = [
        [sg.Column(columna, element_justification='c', pad=(0,100))]
    ]
    return sg.Window('TURNOS',layout,size=(1024,700),finalize=True, element_justification='c',button_color=('#c93c36'))

def add_turno():
    """ Modifica turnos mediante uso de Listbox"""
    data = get_data_from_db('motus','alumnos')
    names = [x['nombre'] for x in data]
    columna = [
        [sg.Checkbox('LUNES', key='lunes', font=('arial',13,'bold'))],
        [sg.Checkbox('MARTES', key='martes', font=('arial',13,'bold'))],
        [sg.Checkbox('MIERCOLES',key='miercoles', font=('arial',13,'bold'))],
        [sg.Checkbox('JUEVES',key='jueves', font=('arial',13,'bold'))],
        [sg.Checkbox('VIERNES',key='viernes', font=('arial',13,'bold'))]
        ]
    
    columna2 = [
        [sg.Listbox(names, size=(20,20), key='alumno',font=('arial',13,'bold'), pad=(0,(0,25)))],
    ]
    layout = [
        [sg.Text('GESTION TURNOS', font=('arial',40,'bold'), pad=(0,(0,50)))],
        [sg.Column(columna2,element_justification='c'),sg.Column(columna, element_justification='c',pad=((50,0),100))],
        [sg.B('Filtrar', size=(20,1), font=('arial',13,'bold')),sg.B('Resetear', size=(20,1), font=('arial',13,'bold'))],
        [sg.B('Actualizar', size=(20,1), font=('arial',13,'bold')),sg.B('Volver',size=(20,1), font=('arial',13,'bold'))]
        ]
    return sg.Window('Agregar turno', layout, size=(1024,700), finalize=True, element_justification='c',button_color=('#c93c36'))

def see_turns(db, table):
    """ Genera un nuevo layout con los turnos de los alumnos"""
    data = get_data_from_db(db,table)
    people_tuple = [(x['nombre'],x['turnos']) for x in data]
    layout = [
        [sg.T('TURNOS', font=('arial',65,'bold'),pad=(0,(25,0)))],
        [sg.Table(people_tuple, headings=['Nombre', 'Turnos'],font=('arial',13,'bold'), key='tabla',col_widths=[30,30],row_height=40,justification='l',auto_size_columns=False, pad=(0,(30,25)),text_color='white', 
                  background_color='#c93c36',hide_vertical_scroll=True)],
        [sg.B('Volver',font=('arial',13,'bold'),size=(20,1), pad=(0,(0,25)))],
    ]
    return sg.Window('Turnos', layout, size=(1024,700), finalize=True,element_justification='c',button_color=('#c93c36'))

def turns_by_day():
    """ Layout para filtrar turnos por dia"""
    columna1 = [
        [sg.Listbox(size=(25,20), key='alumnos',values=[''], no_scrollbar=True,font=('arial',13,'bold'), pad=(0,(0,25)))],
    ]
    columna2 = [
        [sg.Radio('LUNES', key='Lunes', font=('arial',13,'bold'),group_id='dia', default=True)],
        [sg.Radio('MARTES', key='Martes', font=('arial',13,'bold'),group_id='dia')],
        [sg.Radio('MIERCOLES',key='Miercoles', font=('arial',13,'bold'),group_id='dia')],
        [sg.Radio('JUEVES',key='Jueves', font=('arial',13,'bold'),group_id='dia')],
        [sg.Radio('VIERNES',key='Viernes', font=('arial',13,'bold'),group_id='dia')]
        ]
    layout = [
        [sg.T('TURNOS POR DIA', key='turnos_por_dia',font=('arial',40,'bold'), pad=(0,(50,50)))],
        [sg.Column(columna1, element_justification='c'),sg.Column(columna2, element_justification='c',pad=((50,0),100))],
        [sg.B('Aplicar',size=(20,2),font=('arial',13,'bold')), sg.B('Volver',size=(20,2), font=('arial',13,'bold'))]
    ]
    return sg.Window('Filtrado por dias de turnos',layout,size=(1024,700),finalize=True,element_justification='c',button_color=('#c93c36'))


# Layout de los alumnos 
def alumnos(db,table):
    data = get_data_from_db(db,table)
    peoples_name = [x['nombre'] for x in data]
    columna = [
                [sg.Text('ALUMNOS',font=('arial',40,'bold'), pad=(0,(25,30)))],
                [sg.Listbox(peoples_name, size=(20,20), key='alumno',font=('arial',13,'bold'), pad=(0,(0,25)),no_scrollbar=True)],
                [sg.B('Agregar', font=('arial',13,'bold')), sg.B('Modificar',font=('arial',13,'bold')), sg.B('Borrar',font=('arial',13,'bold')),sg.B('Filtrar', size=(7,1), font=('arial',13,'bold')),
                 sg.B('Resetear', size=(7,1), font=('arial',13,'bold'))],
                [sg.B('Ver', size=(7,1), font=('arial',13,'bold'),),sg.B('Volver', size=(7,1), font=('arial',13,'bold'),)]
                ]
    layout = [
        [sg.Column(columna, element_justification='c')]
    ]
    return sg.Window('TURNOS',layout,size=(1024,700),finalize=True, element_justification='c',button_color=('#c93c36'))

def add_modify_alumno(action):
    columna = [
        [sg.Text(f'{action.upper()} ALUMNOS',font=('arial',40,'bold'), pad=(0,(25,50)),key='add_modify_text')],
        [sg.Text('Nombre alumno: ',font=('arial',13,'bold'),text_color='white'), sg.I(key='alumno',size=(20,1))],
        
    ]
    columna2 = [
        [sg.Text('Dias que asiste:',font=('arial',13,'bold'))], 
        [sg.Checkbox('Lunes',key='lunes',font=('arial',13,'bold'),text_color='white')],
        [sg.Checkbox('Martes',key='martes',font=('arial',13,'bold'),text_color='white')],
        [sg.Checkbox('Miercoles',key='miercoles',font=('arial',13,'bold'),text_color='white')],
        [sg.Checkbox('Jueves',key='jueves',font=('arial',13,'bold'),text_color='white')],
        [sg.Checkbox('Viernes',key='viernes',font=('arial',13,'bold'),text_color='white')],
    ]
    layout = [
        [sg.Column(columna, element_justification='c',pad=(0,(0,25)))],
        [sg.Column(columna2, element_justification='l',pad=(0,(0,25)))],
        [sg.Button('Fecha de pago',font=('arial',13,'bold'),size=(20,1),pad=(5,(0,25))), sg.I(key='date',pad=(0,(0,25)),size=(15,1),font=('arial',13,'bold'),text_color='white')],
        [sg.B(f'{action.upper()}',size=(10,1), font=('arial',13,'bold')), sg.B('Volver atras',size=(15,1), font=('arial',13,'bold'))]
    ]
    return sg.Window('AGG ALUMNO',layout, size=(1024,700), finalize=True, element_justification='c',button_color=('#c93c36'))

def display_alumno(values):
    """ Genera un layout con los datos del alumno"""
    alumnito = get_alumno(values['alumno'][0])
    text = f'Alumno {alumnito["nombre"]}\nTurnos: {alumnito["turnos"]}\nUltima cuota paga: {alumnito["pago"]}'
    sg.popup(text,title='Alumno',font=('arial',13,'bold'),button_color=('#c93c36'))

# Cuotas
def cuotas(db,table):
    """ Genera un nuevo layout con los turnos de los alumnos"""
    data = get_data_from_db(db,table)
    people_tuple = [(x['nombre'],x['pago']) for x in data]
    layout = [
        [sg.T('CUOTAS', font=('arial',65,'bold'),pad=(0,(25,0)))],
        [sg.Table(people_tuple, headings=['Nombre', 'Ultimo pago cuota'],font=('arial',13,'bold'), key='alumno',col_widths=[30,30],row_height=40,justification='c',auto_size_columns=False, pad=(0,(30,25)),text_color='white', 
                  background_color='#c93c36',hide_vertical_scroll=True)],
        [sg.B('Registrar pago',font=('arial',13,'bold'),size=(20,2), pad=(10,(0,25))),sg.B('Volver',font=('arial',13,'bold'),size=(20,2), pad=(0,(0,25)))],
    ]
    return sg.Window('Turnos', layout, size=(1024,700), finalize=True,element_justification='c',button_color=('#c93c36'))
    

# Layout de rutinas
def rutinas(routines):
    columna = [
                [sg.Text('RUTINAS',font=('arial',35,'bold'),pad=(0,(0,25)))],
                [sg.Listbox(routines, size=(20,len(routines)),font=('arial',13,'bold'), key='rutina', pad=(0,(0,25)))],
                [sg.B('Ver', size=(7,1), font=('arial',13,'bold')),sg.B('Volver',font=('arial',13,'bold'), size=(7,1))]
                ]
    layout = [
        [sg.Column(columna, element_justification='c', pad=(0,150))]
    ]
    return sg.Window('RUTINAS',layout,size=(1024,700),finalize=True, element_justification='c',button_color=('#c93c36'))
    
def display_routine(valores):
    """ Genera un layout con la imagen de la rutina"""
    ruta = valores['rutina'][0].lower().split(' ')
    ruta = ''.join(ruta)
    ruta = f'routines/{ruta}.png'
    print(ruta)
    columna = [
                [sg.Text(f'RUTINA {valores["rutina"][0].upper()}',font=('arial',40))],
                [sg.Image(ruta,pad=(0,(0,25)))],
                [sg.B('Volver', font=('arial',13,'bold'),size=(7,1))]
                ]
    layout = [
        [sg.Column(columna, element_justification='c', pad=(0,50))],
        
    ]
    return sg.Window('RUTINAS',layout,size=(1024,700),finalize=True, element_justification='c',button_color=('#c93c36'))
    


def main():
    print(sql.createDB('motus'))
    print(sql.createTable('motus','alumnos'))
    pName = get_people_name('motus','alumnos')
    routines = ['Dia 1', 'Dia 2', 'Dia 3', 'Dia 4', 'Dia 5'] 
    principal_layout, turnos_layout, alumnos_layout, rutinas_layout, cuotas_layout = principal(), None, None, None, None 
    add_turno_layout, see_turns_layout, filter_turns, add_alumno_layout = None, None, None, None
    rutina_layout_display= None

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
            window['alumnos'].update(filter_by_turn(day[0]))
            
        if event == 'Volver' and window == filter_turns:
            hide_unhide(filter_turns, turnos_layout)
        if event == 'Volver' and window == add_turno_layout:
            # Volviendo desde agregar turnos, al layout de turnos
            hide_unhide(add_turno_layout, turnos_layout)
        if event == 'Ver turnos' and window == turnos_layout:
            # Ver los turnos de las personas
            see_turns_layout = see_turns('motus','alumnos')
            hide_unhide(turnos_layout, see_turns_layout)
        if event == 'Volver' and window == see_turns_layout:
            hide_unhide(see_turns_layout, turnos_layout)
        # Alumnos
        if event == 'ALUMNOS' and window == principal_layout:
            alumnos_layout = alumnos('motus','alumnos')
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
            try:
                set_alumno(values,fecha)
                hide_unhide(add_alumno_layout, alumnos_layout)
                reset_listbox(alumnos_layout)
            except:
                sg.popup('Faltan datos') 
        if event == 'Modificar' and window == alumnos_layout:
            #Modificando un alumno
            try:
                student = get_alumno(values['alumno'][0])
            except:
                sg.popup('No selecciono alumno para modificar')
            else:
                add_alumno_layout = add_modify_alumno('modificar')
                add_alumno_layout['add_modify_text'].update(f'Modificando a {student["nombre"]}')
                alumnos_layout.hide()
        if event == 'MODIFICAR' and window == add_alumno_layout:
            # Ya en el layout de modificacion de alumno
            try:
                modify_alumno(values, student["nombre"], fecha)
                sg.popup('Alumno modificado')
                hide_unhide(add_alumno_layout, alumnos_layout)
                reset_listbox(alumnos_layout)
            except:
                sg.popup('Faltan datos que completar / No se pudo modificar el alumno')
        if event == 'Filtrar':
            # Filtrando alumno por nombre
            nombre = sg.popup_get_text('Ingrese nombre a buscar')
            alumnos_filtrados = filter_by_name(nombre)
            if alumnos_filtrados == 0:
                sg.popup('No hay alumnos con ese nombre')
            else:
                window['alumno'].update(alumnos_filtrados)
        if event == 'Resetear':
            reset_listbox(window)
        if event == 'Borrar' and window == alumnos_layout:
            # Borrando un alumno
            if len(values['alumno']) < 1:
                sg.popup('No selecciono ningun alumno',font=('arial',13),text_color='white')
            elif len(pName) >= 1:
                delete_alumno(values)
                reset_listbox(window)
            else:
                sg.popup('No hay mas alumnos para borrar',font=('arial',13),text_color='white')
        if event == 'Volver atras' and window == add_alumno_layout:
            hide_unhide(add_alumno_layout, principal_layout)
        if event == 'Ver' and window == alumnos_layout:
            # Popup de alumno seleccionado
            try:
                display_alumno(values)
            except IndexError:
                sg.popup('No selecciono ningun alumno',font=('arial',13),text_color='white')
        if event == 'Volver' and window == alumnos_layout:
            # Volviendo de layout de alumnos al layout principal
            hide_unhide(alumnos_layout, principal_layout)
        # Rutinas
        if event == 'RUTINAS':
            rutinas_layout = rutinas(routines)
            principal_layout.hide()
        if event == 'Volver' and window == rutinas_layout:
            hide_unhide(rutinas_layout, principal_layout)
            # Viendo rutina
        if event == 'Ver' and window == rutinas_layout:
            try:
                rutina_layout_display = display_routine(values)
                print(values)
                rutinas_layout.hide()
            except IndexError:
                sg.popup('No selecciono ninguna rutina')
        if event == 'Volver' and window == rutina_layout_display:
            hide_unhide(rutina_layout_display, rutinas_layout)
        # Estado cuotas
        if event == 'ESTADO CUOTAS' and window == principal_layout:
            cuotas_layout = cuotas('motus','alumnos')
            principal_layout.hide()
        if event == 'Registrar pago':
            try:
                nombre = pName[values['alumno'][0]]
            except:
                sg.popup('No se registro el pago / No se selecciono un alumno')
            else:
                fecha = sg.popup_get_date()
                fecha = date_from_tuple(fecha)
                sql.updatePay(nombre,fecha)
                sg.popup('Pago registrado con exito')
                reset_listbox(window, pagos=True)
        if event == 'Volver' and window == cuotas_layout:
            hide_unhide(cuotas_layout, principal_layout)

        
            
        
                

if __name__ == '__main__':
    main()