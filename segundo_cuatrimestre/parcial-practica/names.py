def buildPeople(nombres, edades, alturas, sexos):
    """ Construye lista de diccionarios pasandole listas correspondientes a nombres, edades, alturas y sexos"""
    namesLen = len(nombres)
    hombres = []
    mujeres = []
    try:
        if len(edades) == namesLen and len(sexos) == namesLen and len(alturas) == namesLen:
            for i in range(namesLen):
                if sexos[i].lower() == 'm':
                    hombres.append({
                        'nombre': nombres[i],
                        'edad': edades[i],
                        'altura': alturas[i],
                    })
                else:
                    mujeres.append({
                        'nombre': nombres[i],
                        'edad': edades[i],
                        'altura':alturas[i]
                                    })
    except:
        return 'Error en el largo de las listas'
    else:
        return hombres, mujeres

def printDicList(dic):
    """ Printea lista de diccionarios, con key y values"""
    try:    
        for e in dic:
            for k,v in e.items():
                print(f'{k.title()}: {v}')
            print('\n')
    except AttributeError:
        return 'Tipo de dato erroneo'

def filterByHeight(dic,height):
    """ Filtra un diccionario de personas por """
    try:
        if type(height) == float:
            newDict = [d for d in dic if d['altura'] >= height]
        else:
            newDict = []
    except:
        return 'Wrong arguments' 
    else:
        if len(newDict) >= 1:
            return newDict
        else:
            return f'No se encontraron personas con una altura mayor a {height} cm, recuerde que la altura debe estar expresada con punto, ejemplo 1.85 cm'

def filterByAge(dic,age):
    """" Filtra un diccionario por edad"""
    try:
        if type(age) == int:
        
            newDict = [d for d in dic if d['edad'] >= age]
        else:
            newDict = []
    except:
        return 'Wrong arguments'
    else:
        if len(newDict) >= 1:
            return newDict
        else:
            return f'No se encontraron personas con una edad mayor o igual a {age} años'

def main():
    # 
    names = ['Khan', 'Omar', 'Sara', 'Ali', 'Mohammed', 'Sofia', 'Mateo']
    ages = [60, 50, 55, 70, 25, 20, 40]
    heights = [1.75, 1.90, 1.55, 1.80, 1.65, 1.71, 1.88]
    sexs = ['M', 'M', 'F', 'M', 'M', 'F', 'M']
    men, woman = buildPeople(names,ages,heights, sexs) # obtengo tupla con listas de diccionarios de hombres y mujeres
    tallMen = filterByHeight(men,1.85) # obtengo los hombres con altura mayor a 1.85 cm
    olderWomen = filterByAge(woman,55) # obtengo las mujeres mayores a 55 años
    print('Hombres con altura mayor a 1.85 cm: ')
    printDicList(tallMen)
    print('Mujeres mayores a 55 años: ')
    printDicList(olderWomen)
    
    

if __name__ == "__main__":
    main()

    