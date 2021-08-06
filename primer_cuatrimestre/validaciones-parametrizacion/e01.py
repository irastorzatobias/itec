def concatenar_strings(separador=' '):
    """" Concatena numero indeterminado de strings con un caracter determinado"""
    frase = input('Ingrese frase a concatenar (ñ para terminar): ')
    result = ''
    while frase.lower() != 'ñ':
        result = result + frase + separador
        frase = input('Ingrese frase a concatenar: ')
    # Devuelve la frase con el separador, menos el ultimo caracter.
    return result[0:-1]



def conca(*args,separador=' '): # solucion clase, solucion correcta, no usar input
    result = ''
    for e in args:
        result = result + e + separador
    return result[:-1]


if __name__ == '__main__':
    print(conca('hola','como','estas',separador='-'))
        
    
    

