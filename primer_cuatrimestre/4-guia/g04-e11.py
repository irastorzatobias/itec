frase = input('Ingrese su frase: ')
fraseSplit = frase.split(' ')
pos = 0
lengthWord = 0
mayor = 0

for i in range(len(fraseSplit)):
    for char in fraseSplit[i]:
        if char.lower() >= 'a' and char.lower() <= 'z':
            lengthWord = lengthWord + 1
if lengthWord > mayor:
    mayor = lengthWord
    pos = i

print('La palabra mas larga es:',fraseSplit[pos])


