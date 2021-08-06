
# Tobias Irastorza.
# Convierte las peliculas dadas en diccionario, solo funciona para el formato brindado por la variable movies y genre

from os import system # para hacer uso de system('cls') y limpiar la terminal cuando el input sea incorrecto


def movies_to_dict(peliculas):
    result = []
    for i in range(len(peliculas)):
        firstParenthesis = peliculas[i].find('(')
        secondParenthesis = peliculas[i].find(')')
        name = peliculas[i][:firstParenthesis]  # got name
        yearResult = peliculas[i][firstParenthesis +
                                  1: secondParenthesis]  # got year
        genero = peliculas[i][secondParenthesis + 1:]
        generoResult = ''
        # got genre
        if genero.lower() == 'act':
            generoResult = 'Acción'
        elif genero.lower() == 'sf':
            generoResult = 'Ciencia Ficción'
        elif genero.lower() == 'com':
            generoResult = 'comedia'
        result.append({
            'name': name,
            'year': yearResult,
            'genre': generoResult
        })
    return result


def get_by_gender(peliculas, genero):  # recibe n dict de peliculas
    result = []
    for i in range(len(peliculas)):
        if peliculas[i]['genre'].lower() == genero.lower():

            result.append(peliculas[i]['name'])
    return result


def released_before_year(peliculas, anio):  # recibe dict de peliculas y año.
    cant = 0
    for i in range(len(peliculas)):
        if int(peliculas[i]['year']) < anio:  # Si el añoo
            cant = cant + 1

    return cant


def starts_with(peliculas, letra):
    result = []
    for i in range(len(peliculas)):
        # Si el nombre en la primer letra empieza con letra, appendeo
        if peliculas[i]['name'][0].lower() == letra.lower():
            result.append(peliculas[i])
    return result


if __name__ == '__main__':
    movies = ["Das boot(1981)act", "Blade Runner(1982)sf", "Arrival(2016)sf",
              "Dumb & Dumber(1994)com", "Blade Runner 2049(2015)sf",
              "Three Kings(1999)act", "The green hornet(2011)com"
              ]
    genre = {'act': 'Acción', 'sf': 'Ciencia Ficción', 'com': 'Comedia'}
    # se pueden cambiar estas variables y hacer que las pida el usuario
    anio = int(input('Ingrese un año: '))

    letra = input('Ingrese una letra: ')

    while len(letra) > 1:
        system('cls')
        print('Ingreso mas de una letra: ')
        letra = input('Ingrese nuevamente la letra: ')

    generoElegido = input(
        'Ingrese un genero: (sf para ciencia ficcion, act para accion, com para comedia): ')
    while generoElegido.lower() != 'sf' and generoElegido.lower() != 'com' and generoElegido.lower() != 'act':
        system('cls')
        print('Genero incorrecto, intente nuevamente')
        generoElegido = input(
            'Ingrese un genero: (sf para ciencia ficcion, act para accion, com para comedia): ')

    # diccionario guardado en dictPeliculas
    dictPeliculas = movies_to_dict(movies)
    # paso parametro dictPeliculas, y comedia
    peliculaPorGenero = get_by_gender(dictPeliculas, genre[generoElegido])
    peliculaPorAnio = released_before_year(dictPeliculas, anio)  # devuelve int
    peliculaPorLetra = starts_with(dictPeliculas, letra)
    print('Peliculas de', genre[generoElegido])
    for i in range(len(peliculaPorGenero)):
        print('- ' + peliculaPorGenero[i])
    print('\nCantidad de peliculas estrenadas antes del año ' +
          str(anio) + ': ' + str(peliculaPorAnio))
    print('\nPeliculas cuyo nombre empieza con la letra ' + letra)
    for i in range(len(peliculaPorLetra)):
        print(peliculaPorLetra[i]['name'] + '.' + ' Año: ' + peliculaPorLetra[i]
              ['year'] + '. Genero: ' + peliculaPorLetra[i]['genre'])
