from os import system

from random import choice

from validacion_entero import validacion_entero

from input_string import input_string

def computer_number():
    result = ''
    available_numbers = ['0','1','2','3','4','5','6','7','8','9'] # numeros disponibles
    aux_available = [] # lista auxiliar para ser utilizada, se van removiendo los valores ya existentes de la lista
    for i in range(0,4): 
        if i == 0: # en la primer posicion,
            aux_available = available_numbers[1:] # representa a los valores disponibles, excepto el 0, ya que no puede comenzar por cero
            aux = choice(aux_available) # choice, elige un valor aleatorio entre los disponibles en available_numbers
            result = result + aux # concateno el numero elegido a la string
            available_numbers.remove(aux) # remuevo el valor obtenido de la lista original
        else:
            aux = choice(available_numbers) # aca se trabaja con la lista completa
            result = result + aux
            available_numbers.remove(aux) # idem que lo anterior, se remueve el valor ya asignado
    return result


def play(file): # recibe un archivo.txt donde guardar los registros de los jugadoresA
    pc_number = computer_number()    
    win = False
    lose = False
    intentos = 1
    while win == False:
        player = str(validacion_entero('Numero de 4 digitos: ',min = 1000, max=9999))
        bien = 0
        regular = 0
        for i in range(len(player)):
            if player[i] == pc_number[i]:
                bien +=1
            elif player[i] in pc_number and player[i] != pc_number[i]:
                regular +=1
        if bien == 4 and intentos <= 25: # con 4 digitos bien ganas
            win = True
            print('Ganaste!')
        elif intentos > 25:
            return 'Superaste el maximo de intentos'              
        else: # de lo contrario se imprimen cuantos digitos bien y cuantos regular tuviste
            print(f'Tus digitos: {bien} bien, {regular} regular. Intenta nuevamente')
            intentos += 1
    if win: # si la persona gano, tomo su nombre
        with open(file,'a') as f:          
            name = input_string('Escribi tu nombre! (Hasta 4 caracteres): ', max=4)
            f.writelines(f'{name},{intentos}\n') 
            update_ranking(file) # organizo el ranking    
            return (f'Felitaciones {name}, ganaste con un total de {intentos} intentos')

def update_ranking(file):
    """" Funcion que organiza el archivo de texto que contiene los intentos de los jugadores de menor a mayor"""
    parsed_result = []
    with open(file) as f: 
        result = f.readlines() # lista con el archivo
    for i in range(len(result)):
        result[i] = result[i].strip() # saco los espacios, tabulaciones o lo que hubiere en la lista
        aux = result[i].split(',') # spliteo, por un lado me queda el nombre y por otro lado el numero
        aux_name = aux[0] # nombre de la persona
        aux_score = aux[1] # intentos de la persona
        parsed_result.append({
            'jugador':aux_name,
            'intentos': int(aux_score)
        })
    return sorted(parsed_result, key = lambda x: x['intentos']) # organiza el diccionario por la key intentos. de menor a mayor
            
            
def print_ranking(file):
    """" Funcion para printear el ranking del juego """
    result = update_ranking(file) # por las dudas se organiza antes de printearlo.
    print('-- RANKING --')
    for i in range(len(result)):
        print(f'{i + 1} - {result[i]["jugador"]} INTENTOS: {result[i]["intentos"]}\n')
 
def seguir_jugando():
    sigue = ''
    val = False
    while val == False and (sigue != 'n' and sigue != 's'):
        try:
            sigue = input('Desea seguir jugando? (s/n): ')
            if sigue.lower() == 's':
                val = True
            elif sigue.lower() == 'n':
                val = False
            else:
                print('Valor invalido, intente nuevamente')
                sigue = input('Desea seguir jugando? (s/n): ')
        except:
            print('Error en el input')
    return sigue
    
            
def menu_miles():
    """ Menu interactivo para el juego miles, controla entradas tambien"""
    file = 'jugadores.txt'
    seguir = ''
    opcion = ''
    while seguir.lower() != 'n':
        try:
            system('cls')
            print('-- ELEGI UNA OPCION --')
            print('1 - JUGAR' )
            print('2 - VER RANKING' )
            print('3 - SALIR')
            opcion = validacion_entero('Ingresa tu opcion: ',min = 1, max = 3)
            if opcion == 1:
                system('cls')
                print(play(file))
                seguir = seguir_jugando()

            elif opcion == 2:
                system('cls')
                print_ranking(file)
                seguir = seguir_jugando()

            elif opcion == 3:
                seguir = 'n'
                
        except:
            print('Argumento invalido')
            
            
                
if __name__ == '__main__':
    menu_miles()
    
    
    
        