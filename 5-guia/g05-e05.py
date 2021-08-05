def listOfWords(frase):
    fraseSplit = frase.split()
    aux = ''
    result = []
    for i in range(len(fraseSplit)):
        if ',' in fraseSplit[i] or '.' in fraseSplit[i]:
            aux = fraseSplit[i]
            aux = aux[0:len(aux)-1]
            result.append(aux)
        else:
            result.append(fraseSplit[i])
    return result
            
def contadorPalabras(fraseList):
    mayor = 0
    aux = 0
    pos = 0
    word = 0
    for x in range(len(fraseList)):
        aux = len(fraseList[x])
        if aux > mayor:
            mayor = aux
            pos = x
    word = fraseList[pos]
    return word

frase = 'Quiero comer manzanas, solo manzanas'
fraseSplit = listOfWords(frase)
fraseMasLarga = contadorPalabras(fraseSplit)
cantLetras = len(fraseMasLarga)
print('La palabra mas larga en la frase es:',fraseMasLarga,'con',cantLetras,'letras')
    
