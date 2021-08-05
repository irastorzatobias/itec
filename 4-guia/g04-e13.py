name = input('Ingrese nombre y apellido separado por espacio: ')
nameSplit = name.split(' ')
invertido = nameSplit[1] + ',' + nameSplit[0]
numeros = [1,2]

invertido = ''
i = len(nameSplit) - 1
if (len(nameSplit) == 2):
    invertido = nameSplit[1] + ',' + nameSplit[0]
else:
    while i != 0:
        invertido = invertido + nameSplit[i]
        i = i - 1
        invertido = invertido + ' '
    invertido = invertido +',' + nameSplit[0]

print(invertido)



