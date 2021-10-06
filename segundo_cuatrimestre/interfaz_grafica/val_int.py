import math
def validacionEntero(message, max=math.inf, min = 0):
    while True :
        try:
            num = int(input(message))
        except:
                print('No ingreso entero, intente nuevamente')
        else:
            if (num >= max or num <= min):
                print(f'El numero debe ser menor a {max} y mayor a {min}')
            else:
                return num



if __name__ == '__main__':
    numerito = validacionEntero('Ingresa un entero: ',10,5)