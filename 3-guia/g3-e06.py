cantNombres = int(input('Ingrese cantidad de nombres: '))
pos = 99
names = []

for i in range(cantNombres):
    names.append(input('Ingrese nombre: '))

nombreABuscar = input('Ingrese nombre a buscar: ')
for j in range(len(names)):
    if nombreABuscar.lower() == names[j].lower():
        pos = j

if pos == 99:
    print('El nombre no se encontro')
else:
    print('El nombre se encontro en la posicion',pos)
    print(names[pos])