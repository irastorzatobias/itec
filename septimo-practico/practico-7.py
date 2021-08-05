from json import loads
from os import system



def read_json(file):
    with open(file, encoding='utf8') as reader:
        result = loads(reader.read())
    return result # devuelve diccionario a partir del json


def not_dot_com(dict):
    result = []
    for i in range(len(dict)): # recorre diccionario
        if dict[i]['email'].find('com') == -1: #si en la key email no esta com, appendeo al resultado
            result.append(dict[i])
    return result


def get_countries(dict):
    result = []
    for e in dict: # recorro diccionario 
        if e['location']['country'] not in result: # si el pais no esta en mi lista de resultados, lo appendeo
            result.append(e['location']['country'])
    return result # lista con paises


def get_languages(dict):
    result = []
    for e in dict:  # element
        for l in e['languages']:  # recorro lenguajes
            if l not in result: # si el lenguaje no esta en resultado, lo agrego a la lista
                result.append(l)
    return result


def quantity_per_country(dict):
    countries = get_countries(dict)
    result = []
    for c in countries: # recorro paises
        aux = 0
        for e in dict: # recorro diccionario entero
            if c == e['location']['country']: # si el pais de la lista, coincide con el pais del diccionario, appendeo a resultado a un nuevo diccionario
                aux = aux + 1 # si el pais aparece, sumo uno a mi variable auxiliar
        result.append({
            'country': c,
            'quantity': aux
        })
    return result


def most_talked_language(dict):
    languages = get_languages(dict)
    aux = 0
    result = []
    for l in languages: # recorro lenguajes
        aux = 0
        for e in dict: # recorro diccionario 
            if l in e['languages']: # comparo lenguaje con elemento del diccionario donde esta el lenguaje
                aux = aux + 1 # si el lenguaje aparece, sumo 1 a mi variable auxiliar
        result.append({ # diccionario result con campos lenguaje y cantidad de personas que hablan ese lenguaje
            'language': l,
            'quantity': aux
        })
    mayor = 0
    masHablado = ''
    for m in result: # para cada elemento del resultado obtenido anteriormente
        if m['quantity'] > mayor: # comparo la cantidad con mayor
            mayor = m['quantity']
            masHablado = m['language']
    return { # retorno el nombre del lenguaje mas hablado y la cantidad de personas
        'nombre-lenguaje': masHablado,
        'cantidad': mayor
    }


def imprimir():

    print("Opciones disponibles:")
    print('1. Personas cuyo mail no termina en .com')
    print('2. Cantidad de personas por pais')
    print('3. Idioma mas hablado')
    print('0. Salir del programa\n')

if __name__ == '__main__':
    people = read_json('practico7.json')
    imprimir()
    sigue = ''
    opcion = input('Ingrese la opcion: ')
    while opcion != '0':
        if opcion == '1':
            sinDotCom = not_dot_com(people)
            for e in sinDotCom:
                for k, v in e.items():
                    print(k, v)
                    print('\n')
            sigue = input('Desea realizar otra operacion?(s/n): ')
        elif opcion == '2':
            porPais = quantity_per_country(people)
            for e in porPais:
                print(f'Pais: {e["country"]}\nCantidad: {e["quantity"]}\n')
            sigue = input('Desea realizar otra operacion?(s/n): ')
        elif opcion == '3':
            lenguajeMasHablado = most_talked_language(people)
            print('Lenguaje mas hablado:', lenguajeMasHablado['nombre-lenguaje'])
            print('Cantidad de personas que lo hablan:', lenguajeMasHablado['cantidad'])
            sigue = input('Desea realizar otra operacion?(s/n): ')
        else:
            system('cls')
            print('Opcion inválida, intente nuevamente') 
            imprimir()
            opcion = input('Ingrese la opcion: ')
    
        if sigue.lower() == 's':
            imprimir()
            opcion = input('Ingrese la opcion: ')
        elif sigue.lower() == 'n':
            opcion = '0'
print('-- FIN DEL PROGRAMA --')
        

    
