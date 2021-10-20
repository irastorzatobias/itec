import PySimpleGUI as sg

choices = [['Tobias', 21]]

layout = [  [sg.Text('What is your favorite color?')],
            [sg.Stretch(),sg.Listbox(choices, size=(15, len(choices)), key='-COLOR-', enable_events=True), sg.Stretch()]
        ]

window = sg.Window('Pick a color', layout)

while True:                  # the event loop
    event, values = window.read()
    print(values)
    if event == sg.WIN_CLOSED:
        break
    if values['-COLOR-']:    # if something is highlighted in the list
        sg.popup(f"Your favorite color is {values['-COLOR-'][0]}")
window.close()