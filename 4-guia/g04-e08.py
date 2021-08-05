frase = input('Ingrese una frase: ')
fraseSplit = [char for char in frase]
contador = 0

for i in range(len(fraseSplit)):
    if(fraseSplit[i]!= '.' and fraseSplit[i] != ',' and fraseSplit[i] != ' '):
        contador = contador + 1
print('Cantidad de letras en la siguiente frase: ')
print(frase)
print('Cantidad de letras:',contador)

