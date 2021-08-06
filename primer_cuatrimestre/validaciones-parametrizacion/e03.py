def check_dots(strng):
    """" Check dots, en un texto determinado verifica que los puntos a la izquierda y a la derecha tengan caracteres validos"""
    dot_positions = []
    dot_position = ''
    aux = strng
    cond = True
    # posiciones de los puntos
    j = 0
    while aux.find('.') != -1:
        dot_position = aux.find('.')
        dot_positions.append(dot_position)
        aux = aux[dot_position + 1:]
    #poisiones absolutas de los puntos
    for i in range(1, len(dot_positions)):
        dot_positions[i] = dot_positions[i] + dot_positions[i - 1] + 1

    #comienzo logica principal del programacion
    
    if strng[len(strng) - 1] == '.': # si el mail termina con punto
        cond = False
    else:
        while cond == True and j < len(dot_positions):
            posicion = dot_positions[j]
            anterior = strng[posicion - 1]
            posterior = strng[posicion + 1]
            if anterior not in '@,.":;' and posterior not in '@,.":;': # simbolos elegidos como invalidos, es relativo a cada plataforma de mail
                cond = True
                j = j + 1
            else:
                cond = False
    return cond

# chequea arroba
def check_arroba(letra):
    """ Funcion que chequea que antes y despues del arroba solo haya letras"""
    ascii_letra = ord(letra)
    return (ascii_letra >= 65 and ascii_letra <= 90) or (ascii_letra >= 97 and ascii_letra <= 122)

def correo_electronico():
    """" Valida correo electronico simil gmail, nada mas que si permite caracteres especiales en algunos casos """
    try:
        correo = input('Ingrese su correo electronico: ')
    # rfind, obtiene ultima ocurrencia del arroba
        arroba = correo.rfind('@')
        after_arroba = correo[arroba:] # string despues del arroba
        before_arroba = correo[:arroba] # string antes del arroba
        char_bf_arroba = correo[arroba - 1] # letra antes del arroba
        char_af_arroba = correo[arroba + 1] # letra despues del arroba
        if ('@' not in correo) or ('.' not in after_arroba) or len(before_arroba) < 1 or ' ' in after_arroba or ' ' in before_arroba:
            return ('-- CORREO INVALIDO --')
        elif (check_dots(correo) and '@' not in before_arroba) and check_arroba(char_bf_arroba) and check_arroba(char_af_arroba):
                # Si no hay puntos antes o despues del arroba
            if '.' in after_arroba[(len(after_arroba) - 1)]:
                return ('-- CORREO INVALIDO --')
            else:
                return ('-- CORREO VALIDO --')
        else:
            return ('-- CORREO INVALIDO --')
    except:
        return('Ingreso un valor invalido')
    
    
if __name__ == '__main__':
    print(correo_electronico())

    