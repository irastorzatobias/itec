def cargarNombres(cant, lista):
    for i in range(cant):
        print('Ingrese el nombre:',i)
        lista.append(input())

def buscarNombre(nombre,lista):
    pos = 999
    result = ''
    for i in range(len(lista)):
        if lista[i].lower() == nombre.lower():
            pos = i
    if pos == 999:
        result = 'El nombre no se encontro'
    else:
        result = 'El nombre se encontro en la posicion ' + str(pos)
    return result

nombres = [] 
cargarNombres(3,nombres)
nombreABuscar = input('Ingrese el nombre a buscar: ')
print(buscarNombre(nombreABuscar, nombres))
print(nombres)

