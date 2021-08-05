
def reemplazar(palabraAReemplazar,reemplazadora, cadena):
    cadenaSplit = cadena.split()
    aux = ' '
    for i in range(len(cadenaSplit)):
        if cadenaSplit[i] == palabraAReemplazar:
            cadenaSplit[i] = reemplazadora
        elif cadenaSplit[i] == palabraAReemplazar + ',':
            cadenaSplit[i] = reemplazadora + ','
        elif cadenaSplit[i] == palabraAReemplazar + '.':
            cadenaSplit[i] = reemplazadora + '.'
    aux = aux.join(cadenaSplit)
    return aux
frase = 'Quiero comer manzanas, solamente manzanas.'
word = 'peras'

print(reemplazar('manzanas',word,frase))