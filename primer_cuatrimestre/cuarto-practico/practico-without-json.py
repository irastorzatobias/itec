# Solucion sin libreria JSON
# Tobias Irastorza
# Crear el archivo txt con las peliculas


# Se puede usar import para importar las funciones directamente desde practico.py, pero la consigna no permite import.

def create_movies_file(dic, file):  # Recibe un diccionario y el file donde ponerlo
    with open(file, 'w') as writer:
        for i in range(len(dic)):
            # Separo recaudacion final ya que contiene $ y comas
            recaudacionAux = dic[i]['recaudacion'].split(',')
            recaudacionFinal = ''
            for e in recaudacionAux:  # Recorro la recaudacion y la almaceno en una string
                recaudacionFinal = recaudacionFinal + e
            writer.write(dic[i]['titulo'] + ',' + dic[i]['actor-principal'] +
                         ',' + dic[i]['rating'][0:2] + ',' + recaudacionFinal[1:] + '\n')
            # Rating obtenego solo los dos primeros numeros y no el simbolo, lo mismo con recaudacion final

# Recaudacion total


def recaudacion_total(dic):
    acum = 0
    for i in range(len(dic)):
        # Separo recaudacion final ya que contiene $ y comas
        recaudacionAux = dic[i]['recaudacion'].split(',')
        recaudacionFinal = ''
        for j in range(len(recaudacionAux)):
            if j == 0: # Si j es igual a 0, que es la posicion del array donde se encuentra el $, arranco desde la primer posicion en adelante en appendear
                aux = recaudacionAux[j][1:]
                recaudacionFinal = recaudacionFinal + aux
            else: # Cuando J se diferente a 0, agrego los digitos restantes 
                recaudacionFinal = recaudacionFinal + recaudacionAux[j]
            acum = acum + int(recaudacionFinal) # Convierto la recaudacion en int para poder sumar en el acumulador
    return acum


def rating_promedio(dic):
    acum = 0
    aux = 0
    prom = 0
    for i in range(len(dic)): # Recorro los rating 
        aux = int(dic[i]['rating'][0:2])  # Convierto el valor de rating en promedio, de [0:2] para evitar el %
        acum = acum + aux
    prom = acum / (len(dic)) # Calculo promedio
    return prom


def imprimir():
    print("________________________")
    print("MENU")
    print("________________________")
    print()
    print("Opciones disponibles:")
    print("1. Imprimir todas las peliculas")
    print("2. Ver recaudacion total")
    print("3. Ver ranking promedio")
    print("0. Salir del programa")


def movies_data_propio(file):  # Recibe
    pelisDict = []
    titles = []
    actors = []
    rating = []
    boxOffice = []
    with open(file, 'r') as reader:
        aux = reader.readlines()
        posTitle = 0 
        for i in range(len(aux)):
            posTitle = aux[i].find('"Title": ') # Posicion titulo en el índice i
            posActors = aux[i].find('"Actors": ') # Posicion actores en el indice i
            posRating = aux[i].find('"Rotten Tomatoes"') # Idem
            posBoxOffice = aux[i].find('"BoxOffice": ') # Idem
            if posTitle != -1:
                titles.append(aux[i][posTitle:].split(': ')) # Split de la linea con el titulo encontrado
            if posActors != -1:
                actors.append(aux[i][posActors:].split(': ')) # Split de la linea con los actores
            if posRating != -1:
                rating.append(aux[i + 1].split(': ')) # Split de la linea con el rating, i + 1 para hacer referencia al espacio Value y no al Source que dice Rotten Tomatoes
            if posBoxOffice != -1: 
                boxOffice.append(aux[i][posBoxOffice:].split(': ')) # Split de la linea con el boxoffice

    for i in range(len(titles)): # Recorro titulos
        titles[i][1] = titles[i][1].replace('"','') # Quito comillas
        titles[i][1] = titles[i][1].replace(',\n','') # Quito salto de linea y comas asi queda el titulo limpio
        pelisDict.append({
            'titulo': titles[i][1]
        }) # Append del titulo en la lista
 
    finalActor = [] # Array de actores
    for i in range(len(actors)): 
        aux = actors[i][1].split(',') # Spliteo la linea de actores correspondiente a la posicion i con una coma
        finalActor.append(aux[0][1:]) # Primer nombre de actor sin el "" del principio
    for i in range(len(pelisDict)):
        pelisDict[i]['actor-principal'] = finalActor[i] # Appendeo el actor principal
        pelisDict[i]['rating'] = rating[i][1][1:4]  # Rating con el %, evitando la primer posicion (0) que corresponde a una comilla
        boxOffice[i][1] = boxOffice[i][1].replace(',\n','')  # Reemplazo en cada una de las recaudaciones el salto de linea al final de cada numero
        pelisDict[i]['recaudacion'] = boxOffice[i][1][1:-1] # Append en la recaudacion del presupuesto desde la posicion 1, evitando la comilla inicial, hasta la penultima posicion, evitando el espacio
    return pelisDict # Devuelvo diccionario que me sirve p utilizacion de las mismas funciones
        

if __name__ == '__main__':
    # Diccionario de pelis
    moviesDic = movies_data_propio('pelis.json')
    print(moviesDic)
    opcion = 5
    again = 's'
    imprimir()
    # Creado de archivo 
    create_movies_file(moviesDic, 'peliculas.csv')
    opcion = int(input('Ingrese su opcion:\n'))
    if opcion != 0: 
        while (opcion < 0 or opcion > 3):
            print('Valor inválido, ingrese nuevamente')
            opcion = int(input('Ingrese su opcion: '))
        while again.lower() != 'n':  
            if (opcion == 1):
                print('Peliculas: ')
                for e in moviesDic:
                    for key, value in e.items():
                        print(key, value)
                    print('\n')
            elif (opcion == 2):
                # Recaudacion Total
                print('Recaudacion total')
                print(recaudacion_total(moviesDic))
            elif (opcion == 3):
            # Rating promedio
                print('Rating promedio: ')    
                print(rating_promedio(moviesDic))
            again = input('Desea realizar otra accion?(s/n): ')
            if again.lower() == 'n':   
                print('Programada finalizado')
                opcion = 0
            else: 
                imprimir()
                opcion = int(input('Ingrese la opcion:\n'))
    else:
        print('Programa finalizado')

    
