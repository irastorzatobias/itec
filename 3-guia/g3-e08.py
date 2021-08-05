cantNumeros = int(input('Ingrese cantidad de numeros a cargar: '))
newList = []
for i in range(cantNumeros):
    newList.append(int(input('Ingrese un numero: ')))
print('Lista normal: ')
print(newList)
print('Lista invertida: ')
newList.reverse()
print(newList)