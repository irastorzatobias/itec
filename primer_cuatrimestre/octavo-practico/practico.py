from os import system
def born_in_summer(dict):
    year = input('Ingrese un año entre 1980 y 1999: ') 
    result = []
    while year < '1980' or year > '1999':
        year = input(('Ingreso un año invalido, intente nuevamente: '))    
    for e in dict:
        bornSplit = e['nacimiento'].split('-')
        anio = bornSplit[0] # año de la persona
        dia = bornSplit[2] # dia en que nacio
        mes = bornSplit[1] # mes en que nacio
        if anio == year and (mes >= '01' and mes <= '02'):         # si es enero o febrero 
            result.append(e['nombre']) 
        elif mes == '03' and dia <= '20' and anio == year: # si es marzo del anio actual y menor al dia 20
            result.append(e['nombre'])
        elif ((int(year) - 1) == int(anio)) and mes == '12' and dia >= '21': # si es el año pasado en diciembre y el dia es mayor a 21
            result.append(e['nombre'])
    return result, year
        



def get_csv(file):
    result = []
    with open(file, 'r') as reader:
        reader = reader.readlines()
        for e in reader:
            if 'nombre' not in e: # si nombre no esta en la linea leida
                e = e.split(',') # spliteo nombre y fecha 
                space = e[1].find(' ') # encuentro el espacio tras la fecha que indica la hora
                fechaNacimiento = e[1][0:space] # hago un slice de la fecha, desde el año hasta el espacio que lo separa de la hora
                result.append({
                    'nombre': e[0],
                    'nacimiento': fechaNacimiento 
                })
    return result
                
if __name__ == '__main__':  
    people = get_csv('nacidos.csv')
    nacieronEnVerano, anio = born_in_summer(people)
    print(f'Nombre de las personas nacidas en verano en el año {anio}')
    if len(nacieronEnVerano) < 1:
        system('cls')
        print('No se encontraron personas en ese año que hayan nacido en verano')
    else:
        for e in nacieronEnVerano:
            print(e)