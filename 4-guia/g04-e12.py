frase = input('Ingrese su frase con numero: ')
fraseSplit = frase.split()
doble = 0


for i in range(len(fraseSplit)):
    aux = ord(fraseSplit[i][0])
    if aux >= 48 and aux <= 57:
        tonumber = int(fraseSplit[i])
        doble = tonumber * 2

print('El numero que se encontro en el array es', tonumber)
print('El doble de ese numero es:',doble)