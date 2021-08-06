frase = input('Ingrese una frase: ')
fraseSplit = [char for char in frase]
a = 0
e = 0 
i = 0
o = 0
u = 0
mayor = 0
pos = 0
for j in range(len(fraseSplit)):
    if fraseSplit[j].lower() == 'a':
        a = a + 1
    elif fraseSplit[j].lower() == 'e':
        e = e + 1
    elif fraseSplit[j].lower() == 'i':
        i = i + 1
    elif fraseSplit[j].lower() == 'o':
        o = o + 1
    elif fraseSplit[j].lower() == 'u':
        u = u + 1

if a > mayor:
        mayor = a
if e > mayor:
        mayor = e
if i > mayor:
        mayor = i
if o > mayor:
        mayor = o
if e > mayor:
        mayor = e



if a == mayor:
    print('A es una de las vocales / es la vocal mas repetida, aparecio',mayor,'veces')
if e == mayor:
    print('E es una de las vocales / es la vocal mas repetida, aparecio',mayor,'veces')
if i == mayor:
    print('I es una de las vocales / es la vocal mas repetida, aparecio',mayor,'veces')
if o == mayor:
    print('O es una de las vocales /  es la vocal mas repetida, aparecio',mayor,'veces')
if u == mayor:
    print('U es una de las vocales / es la vocal mas repetida, aparecio',mayor,'veces')
        