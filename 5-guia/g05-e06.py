def countingVowels(vowelList):
    aux = vowelList
    total = 0
    for i in range(len(vowelList)):
        if vowelList[i] in ('a','e','i','o','u'):
            total = total + 1
    return total

# chars = ['a','b','c','d','e','f','g','h','j','k']
chars = []
for i in range(10):
    print('Ingrese la letra en la posicion',i)
    chars.append(input())

result = countingVowels(chars)

print('La lista brindada contiene',result,'vocales')