def invertirLista(lista):
    aux = []
    for i in range(len(lista)):
        aux.append(lista[len(lista) - i - 1])
    return aux

numbers = [1,2,3,4,5,6,7,8,9,10]
invertedNumbers = invertirLista(numbers)
print(invertedNumbers)