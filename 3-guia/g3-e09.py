cantPersonas = int(input('Ingrese cantidad de personas a cargar: '))
names = []
salary = []
aux = []

for i in range(cantPersonas):
    print('Nombre de la persona',i)
    names.append(input())
    print('Salario de la persona',i)
    salary.append(int(input()))

for j in range(cantPersonas):
    if salary[j] > 85000:
        aux.append(names[j])

print('Nombre de las personas que ganan mas de $85000')
print(aux) 