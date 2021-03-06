import PySimpleGUI as sg

def vocalMasRepetida(str):
    """ Retorna la vocal/es mas repetida en una string|"""
    contVocales = {}
    result = {}
    auxStr = str.lower()
    vocales = ['a','e','i','o','u']
    for i in range(len(vocales)):
        contador = auxStr.count(vocales[i]) # cuento la vocal mas repetida, vocal por vocal
        contVocales[vocales[i]] = contador
    m = max(contVocales.values()) # cuento el valor maximo dentro del diccionario de vocales
    if m > 0:            
        for k,v in contVocales.items():
            if v == m:
                result[k] = v
        return result
    else:
        return 'No se ingreso texto con vocales'
    
    
    

layout = [
            [sg.Stretch(),sg.Text('Ingrese su frase'), sg.Stretch()],
            [sg.Stretch(),sg.Input(key='frase'),sg.Stretch()],
            [sg.Stretch(),sg.Button('OK',size=(15,1)), sg.Button('Exit',size=(15,1)),sg.Stretch()]
            ]

def createGUI(lay):
    window = sg.Window('Vocal mas repetida en una frase', layout) # return_keyboard_events=True
    
    while True:
        event, values = window.read()
        if event in [None, 'Exit']:
            break
        elif event == 'OK':
            vFrecuencia = vocalMasRepetida(values['frase']) # vocal con mas frecuencia
            # Si me devuelve el diccionario correspondiente, hago el popup con las vocales
            if type(vFrecuencia) == dict:
                displayText = 'Vocal/es mas repetida/s:\n'
                for k,v in vFrecuencia.items():
                    displayText += f'Vocal: {k}, apariciones: {v} veces\n'
                sg.popup(displayText)
            else:
                # Si no me devuelve diccionario, significa que no hay vocales, popup con el error
                sg.popup(vFrecuencia)

    window.close()

def main():
    createGUI(layout)
    


if __name__ == '__main__':
    main()