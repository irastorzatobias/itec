from math import pow
cantNumeros = int(input('Cantidad de numeros a ingresar: '))
numberList = []
cuadradoList = []
for i in range(cantNumeros):
    numberList.append(int(input('Ingrese numero: ')))

for j in range(len(numberList)):
    cuadradoList.append(pow(numberList[j],2))

print(cuadradoList)

