textoDado = input('ingrese un texto cualquiera: ')
repite = input('ingrese una letra para saber cuantas veces se repite: ')
contador = 0
for i in range(len(textoDado)):
    if textoDado[i].lower() == repite.lower():
        contador = contador + 1

print(repite,'se repite:',contador,'veces')