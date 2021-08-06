def promedioNum(lista):
    resultado = 0
    prom = 0
    for i in range(len(lista)):
        resultado = resultado + lista[i]
    prom = resultado / len(lista)
    return prom

def mayorQue(prom, lista):
    aux = []
    for i in range(len(lista)):
        if lista[i] > prom:
            aux.append(lista[i])
    return aux


numbersList = [1,2,3,4,5,6,7]
promedio = promedioNum(numbersList)
print('Promedio:',promedio)
print('Numeros mayores al promedio:')
print(mayorQue(promedio,numbersList))