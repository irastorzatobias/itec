def contadorPalabras(word):
    aux = word.split()
    cantPalabras = len(aux)
    return cantPalabras

frase = 'Quiero comer manzanas, solo manzanas.'
print('La frase ingresada tiene',contadorPalabras(frase),'palabras')
