import PySimpleGUI as sg

layout = [[sg.Text('Hi')],
          [sg.Button('OK'),sg.Button('Exit')]
          ]

window = sg.Window('Titulo', layout)

while True:
    event, values = window.read()
    if event in 'Exit':
        break

window.close()

