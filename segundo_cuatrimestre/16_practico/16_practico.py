
import PySimpleGUI as sg
personas = [['Juan',31], ['Ana', 22]]

def principal_layout():
    filas = [
                [sg.Stretch(),sg.Text('Nombre y edad empleados'), sg.Stretch()],
                [sg.Stretch(),sg.Listbox(personas, size=(15, 5), key='persona'), sg.Stretch()],
                [sg.Stretch(),sg.B('AGREGAR'),sg.B('MODIFICAR'), sg.B('BORRAR'),sg.Stretch()]
                ]
    return sg.Window('Layout principal', filas, finalize=True)

def secondary_layout():
    filas = [
                [sg.Stretch(),sg.T('AGREGAR',key='add_modify'), sg.Stretch()],
                [sg.I(key='nameP', size=(20,1)), sg.I(key='ageP', size=(20,1))],
                [sg.B('OK', bind_return_key=True),sg.B('Salir')]
                ]
    return sg.Window('Layout secundario', filas, finalize=True)



def main():
    principal, secundario = principal_layout(), None
    add = False
    modify = False
    while True:
        window, event, values = sg.read_all_windows()
        if window == principal and event == sg.WIN_CLOSED:
            break
        # AGREGAR
        if window == principal and event == 'AGREGAR':
            add = True
            secundario = secondary_layout()
            secundario.un_hide()
        if window == secundario and event == 'OK' and add == True:
            personas.append([values['nameP'].strip(),values['ageP'].strip()])
            principal['persona'].update(personas)
            add = False
            secundario.hide()
        # MODIFICAR
        if window == principal and event == 'MODIFICAR':
            try:
                modify = True
                pos = personas.index(values['persona'][0])
                secundario = secondary_layout()
                secundario.un_hide()    
                secundario['add_modify'].update('MODIFICAR')
                secundario['nameP'].update(values['persona'][0][0]) 
                secundario['ageP'].update(values['persona'][0][1].strip())
            except: 
                sg.popup('No seleccionaste nada')
        if window == secundario and event == 'OK' and modify == True:
            personas[pos] = [values['nameP'],values['ageP']] 
            principal['persona'].update(personas)
            modify = False
            secundario.hide()
        # BORRAR
        if window == principal and event == 'BORRAR':
          try:
            pos = personas.index(values['persona'][0])
            personas.pop(pos)
            window['persona'].update(personas)
          except:
              sg.popup('No hay mas personas cargadas')
        if window == secundario and (event == 'Salir' or event == sg.WIN_CLOSED):
            secundario.hide()
            principal.un_hide()  
    

if __name__ == '__main__':
    main()