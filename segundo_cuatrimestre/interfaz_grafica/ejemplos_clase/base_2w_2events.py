# Base para dos ventanas, ambas abiertas y con eventos.

import PySimpleGUI as sg


def firstLayout():
    filas = [
        [
            sg.Text("Cuántas personas se van a cargar: ", size=(30, 1)),
            sg.Input(key="entero_cantidad", size=(3, 1)),
        ], # primer fila
        [sg.Button("Ok", bind_return_key=True), sg.T("", key="msg", size=(30, 1))], # segunda fila
    ]
    return filas


def secondLayout(values):
    filas = [
        [
            sg.Text(f"Edad de la persona {fila+1}: ", size=(30, 1)),
            sg.Input(key=f"entero_edad_{fila+1}: ", size=(3, 1)),
        ]
        for fila in range(int(values["entero_cantidad"]))
    ]
    # Acá si hace falta el append porque es un boton que va al final y no se repite
    filas.append(
        [sg.Button("Ok", bind_return_key=True), sg.T("", key="salida", size=(30, 1))]
    )
    return filas


def validate_input(window, values, msg):  # Define la validacion de los datos ingresados
    vD = {"entero": int, "real": float}
    for k, v in values.items():
        tipo = k.split("_")[0]
        if tipo in vD:
            try:
                vD[tipo](v)
                window[msg].update(value="")
            except:
                window[msg].update(value=f"Error: Debe ser un {tipo}")
                window[k].set_focus()
                return False
    return True


def main(firstWindow):
    def wLoop(window, fAction, msg):
        while True:
            event, values = window.read()
            if event in (sg.WIN_CLOSED, "Exit"):
                break
            if validate_input(window, values, msg):
                # fAction le pasa a la ventana siguiente los values de esta
                fAction(window, values)
                
    def action2(secondWindow, values2):
        """ Saco promedio, secondWindow es la segunda ventana, values2 los valores de la segunda ventana"""
        lista = [int(x) for x in values2.values()]
        promedio = f"El promedio es {sum(lista) / len(lista)}"
        secondWindow["salida"].update(str(promedio))

    def action1(firstWindow, values1):
        """ Updateo msg primer ventana, abro la segunda."""
        firstWindow["msg"].update("Abrí la segunda ventana")
        secondWindow = sg.Window(
            "Edades", layout=secondLayout(values1))
        wLoop(secondWindow, action2, "salida")

    wLoop(firstWindow, action1, "msg")


if __name__ == "__main__":
    firstWindow = sg.Window("Promediar edades", firstLayout())
    main(firstWindow)
    firstWindow.close()
