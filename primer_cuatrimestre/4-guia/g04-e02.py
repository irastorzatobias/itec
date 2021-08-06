frase = 'Curso de Python'
posicionPython = frase.find('Python')
beforePython = frase[0:posicionPython]
afterPython = frase[posicionPython:]

print(beforePython)
print(afterPython)
aux = beforePython + 'Programacion en ' + afterPython
print(aux)


