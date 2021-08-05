def validacion(tipo, mensaje):
    validacion = False
    while not validacion:
        e = input(mensaje)
        try:
            if tipo == 'real':
                n = float(e)
                validacion = True
            elif tipo == 'entero':
                n = int(e)
                validacion = True
        except: 
            print('Error, debe ingresar un numero',tipo)
    return n

nombre = input('Ingrese su nombre: ')
edad = validacion('entero','Ingrese su edad: ')
altura = validacion('real','Ingrese su altura: ')
print(nombre)
print('Edad',edad)
print('Altura',altura)

