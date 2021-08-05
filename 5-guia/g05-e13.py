def invertirNombre(nombre):
    aux = nombre.split()
    result = aux[1] + ', ' + aux[0]
    return result

nombre = 'Tobias Irastorza'
nombreInvertido = invertirNombre(nombre)
print(nombreInvertido)

