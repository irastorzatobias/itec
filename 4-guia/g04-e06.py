contador = 0
frase = 'Quiero comer manzanas, solamente manzanas.'
palabra = input('Ingrese la palabra a buscar: ')
fraseSplit = frase.split(' ')
for i in range(len(fraseSplit)):
    if(fraseSplit[i] == palabra or fraseSplit[i] == palabra + '.'  or fraseSplit[i] == palabra + ','):
        contador = contador + 1

print('Veces que aparecio la palabra',palabra,':',contador)

