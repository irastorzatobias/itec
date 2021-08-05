num = []
auxList = []

for i in range(10):
    print('Ingrese el valor',i)
    aux = int(input())
    num.append(aux)

for r in range(10):
    if num[r] > 23:
        aux = num[r]
        auxList.append(aux)

print("Hay",len(auxList),"numeros mayores que 23")
print("Numeros mayores a 23 de la lista dada: ")
print(auxList)