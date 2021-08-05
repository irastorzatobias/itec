def input_con_opciones(mensaje, *opciones):
    """" recibe un mensaje y opciones, funciona como un input de opciones """
    final = '('
    for i in range(len(opciones)):
        # primer if, representa el ultimo elemento, el cual no contiene luego una barra /
        if i != (len(opciones) - 1):
            final = final + opciones[i] + '/'
        else: # en caso de que sea el ultimo elemento, no agregar la barra, sino un parentesis al final
            final = final + opciones[i] + '):\n'
        # Devuelvo el mensaje : y el conjunto de opciones 
    return input(mensaje + ' ' + final)

        


if __name__ == '__main__':
    print(input_con_opciones('Ingrese una opcion ','a','b','c'))