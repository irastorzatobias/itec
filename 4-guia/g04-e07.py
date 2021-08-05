frase = input('Ingrese la frase: ')
print(frase)
palabra = input('Ingrese la palabra a buscar: ')
reemplazo = input('Por cual palabra desea reemplazarla?: ')
fraseSplit = frase.split(' ')
for i in range(len(fraseSplit)):
    if(fraseSplit[i].lower() == palabra.lower()):
        fraseSplit[i] = reemplazo 
    elif fraseSplit[i].lower() == palabra.lower() + '.':
        fraseSplit[i] = reemplazo + '.'
    elif fraseSplit[i].lower() == palabra.lower() + ',':
        fraseSplit[i] = reemplazo + ',' 
aux = ''
aux = ' '.join(fraseSplit)
print(palabra,'reemplazada por:',reemplazo)
print(aux)


    


