letras = []
ingresa = input('Desea ingresar valor a la lista? (s/n): ')
contador = 0
while (ingresa != 'n'):
    value = input('Ingrese el valor a insertar a la lista: ')
    letras.append(value)
    ingresa = input('Desea agregar otra letra?: ')

for i in range(len(letras)):
    if(letras[i].lower() == 'a' or letras[i].lower() == 'e' or letras[i].lower() == 'i' or letras[i].lower() == 'o' or letras[i].lower() == 'u'):
        contador = contador + 1


print('Hay',contador,'vocal/es')

