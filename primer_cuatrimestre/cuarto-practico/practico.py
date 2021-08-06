from json import loads, load
# Tobias Irastorza

# Solucion con libreria JSON

def movies_data(file):  # Recibe directorio.
    with open(file,'r') as reader:
        aux = reader.read()
        pelisJson = loads(aux)     
        pelis = []
        titulo = []
        actor = []
        rottenRating = []
        recaudacion = []
        for i in range(len(pelisJson)): # Recorro dic
            for j in range(len(pelisJson[i]['Ratings'])): # i hace referencia a la posicion de la pelicula
                if pelisJson[i]['Ratings'][j]['Source'] == 'Rotten Tomatoes': # j hace referencia a la posicion del rating
                    rottenRating.append(pelisJson[i]['Ratings'][j]['Value'])
            actorAux = pelisJson[i]['Actors'].split(',') # Spliteo nombres para obtener el primero
            recaudacionAux = pelisJson[i]['BoxOffice']
            titulo.append(pelisJson[i]['Title']) 
            actor.append(actorAux[0])
            recaudacion.append(pelisJson[i]['BoxOffice'])
            pelis.append({
                'titulo': titulo[i],
                'actor-principal': actor[i],
                'rating': rottenRating[i],
                'recaudacion': recaudacion[i]
            })
    
    return pelis


# Crear el archivo txt con las peliculas

def create_movies_file(dic, file): # Recibe un diccionario y el file donde ponerlo.
    with open(file,'w') as writer:
        for i in range(len(dic)):        
            recaudacionAux = dic[i]['recaudacion'].split(',') # Separo recaudacion final ya que contiene $ y comas
            recaudacionFinal = '' 
            for e in recaudacionAux: # Recorro la recaudacion y la almaceno en una string
                recaudacionFinal = recaudacionFinal + e
            writer.write(dic[i]['titulo'] + ',' + dic[i]['actor-principal'] + ',' + dic[i]['rating'][0:2] + ',' + recaudacionFinal[1:] + '\n')
            # Rating obtenego solo los dos primeros numeros y no el simbolo, lo mismo con recaudacion final
            
# Recaudacion total            
def recaudacion_total(dic):
    acum = 0
    for i in range(len(dic)):
        recaudacionAux = dic[i]['recaudacion'].split(',') # Separo recaudacion final ya que contiene $ y comas
        recaudacionFinal = ''
        for j in range(len(recaudacionAux)):
            if j == 0:
                aux = recaudacionAux[j][1:]
                recaudacionFinal = recaudacionFinal + aux
            else: 
                recaudacionFinal = recaudacionFinal + recaudacionAux[j]
            acum = acum + int(recaudacionFinal)
    return acum

def rating_promedio(dic):
    acum = 0
    aux = 0
    prom = 0
    for i in range(len(dic)):
        aux = int(dic[i]['rating'][0:2])
        acum = acum + aux
    prom = acum / (len(dic))
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
    print("0. Salir")

if __name__ == '__main__':
    print(load('./pelis.json'))
    # Diccionario de pelis
    moviesDic = movies_data('pelis.json')
    opcion = 5
    again = 's'
    imprimir()
    # Creado de archivo 
    create_movies_file(moviesDic, 'pelis.csv')
    opcion = int(input('Ingrese su opcion:\n'))
    if opcion != 0:
        while (opcion < 0 or opcion > 3):
            print('Valor inválido, ingrese nuevamente')
            opcion = int(input('Ingrese su opcion: '))
        while again.lower() != 'n':
            # Muestra peliculas  
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

            
            

    
