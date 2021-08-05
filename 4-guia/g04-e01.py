
frase = 'River vuelve a las copas'
letraAReemplazar = input('Ingrese la letra a reemplazar: ')
reemplazador = input('por que letra desea reemplazarlo?: ')
fraseSplit = [char for char in frase]
aux = ''
for i in range(len(fraseSplit)):
    if(fraseSplit[i].lower() == letraAReemplazar.lower()):
        fraseSplit[i] = reemplazador
aux = aux.join(fraseSplit)
print('Frase sin:',letraAReemplazar,'y con',reemplazador)
print(aux)





