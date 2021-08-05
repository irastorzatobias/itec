import sys

def inputNumber(tipo, mensaje):
    validado = False
    while not validado:
        numero = input(mensaje)
        try:
            if tipo == "entero":
                numero = int(numero)
            elif tipo == "real":
                numero = float(numero)
            else:
                print("Check! entero o real. Ctrl C!")
            validado = True
        except:
            print("Error. Debe ingresar un número", tipo)
    return numero



def validacion_entero(message='Imgrese un numero entero: ', min=0,max=sys.maxsize):
    """" Recibe un mensaje, minimo y maximo para el ingreso de un entero"""
    try:  
        numero = inputNumber('entero',message)
        while numero <= min or numero >= max:
            print(f'Numero entero mayor que {min} y menor que {max}')
            numero = inputNumber('entero', message)
        return numero
    except:
        return 'Error, argumento invalido'



if __name__ == '__main__':
    print(validacion_entero())
    print(validacion_entero('numero entero menor que 1000 y mayor que 500: ',max=1000,min=500))
    print(validacion_entero('numero entero menor que 10: ',max=10))
    print(validacion_entero('numero entero mayor que 10: ',min=10))
    
        
    