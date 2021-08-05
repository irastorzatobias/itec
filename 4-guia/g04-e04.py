palabra = input('Ingrese la palabra: ')
palabraSplit = [char for char in palabra]
aux = ''
for i in range(len(palabraSplit)):
    if(palabraSplit[i] >= 'a' or palabraSplit[i] <= 'z'): 
        asciiValue = ord(palabraSplit[i])
        aux = aux + chr(asciiValue - 32)
    else:
        asciiValue = ord(palabraSplit[i])
        aux = aux + chr(asciiValue)
print('Palabra ingresada:',palabra)
print('Palabra en mayuscula:',aux)