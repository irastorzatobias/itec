def contadorLetras(palabra):
    palabraSplit = [char for char in palabra]
    mayus = 0
    minus = 0
    acentuadas = 0
    enies = 0
    for i in range(len(palabraSplit)):
        aux = ord(palabraSplit[i])
        print(aux)
        if aux >= 65 and aux <= 90:
            mayus = mayus + 1
        elif aux >= 97 and aux <= 122:
            minus = minus + 1
        elif aux == 225 or aux == 233 or aux == 237 or aux == 243 or aux == 250:
            acentuadas = acentuadas + 1
        elif aux == 241 or aux == 209:
            enies = enies + 1
    print('Letras mayusculas:',mayus,'\nLetras minusculas:',minus)
    print('Letras acentuadas:',acentuadas,'\nEñes:',enies)

frase = input('Ingrese la frase: ')
print(contadorLetras(frase))

