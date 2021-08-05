frase = 'River vuelve a las copas'
withoutS = ''

for i in range(len(frase)):
    if frase[i] != 's':
        withoutS = withoutS + frase[i]

print(withoutS)