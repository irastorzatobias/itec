# Tobias Irastorza 

from datetime import date

def iniciales_y_apellido(listaPersonas):
    nuevosNombres = [] # Lista de nuevos nombres
    for i in range(len(listaPersonas)):
        nameSplit = listaPersonas[i].split(',') # Separo en nombre y apellido en cada vuelta
        inicial = nameSplit[1][1] # En indice 1 está el nombre, e indice 1 esta la primer letra, ya que hay un espacio
        new = inicial + '.' + nameSplit[0] # variable new que guarda el nombre con el nuevo formato
        nuevosNombres.append(new) # Adjunto a la lista el nuevo nombre
    return nuevosNombres
        
def nombre_mas_largo(listaNombres):
    longest = 0 # Determino variable para comparar
    name = '' 
    for i in range(len(listaNombres)):
        nameSplit = listaNombres[i].split(' ') # Separo en nombre y apellido en cada vuelta
        largoNombre = len(nameSplit[1]) # Almaceno en la variable el largo del nombre
        if largoNombre > longest: # Comparo largo nombre con longest
            longest = largoNombre
            name = nameSplit[1] # Almaceno en variable name el nombre mas largo
    return name

def edad(fn, separador): # Agregado parametro separador para adaptarse al formato del practico
    hoy = date.today()
    dn, mn, an = fn.split(separador)
    dn = int(dn)
    mn = int(mn)
    an = int(an)
    dh = hoy.day
    mh = hoy.month
    ah = hoy.year
    e = ah - an
    if (mn > mh) or (mn == mh and dn > dh):
        e -= 1
    return e

def promedio_edad_mujeres(nombres, generos, nacimientos): 
    listaMujeres = []
    edades = []
    acum = 0
    promedio = 0
    for i in range(len(generos)): # Recorro los generos
        if generos[i] == 'f':
            listaMujeres.append(nombres[i]) # Si el genero es femenino, lo adjunto a mi listaMujeres
            edades.append(edad(nacimientos[i],'/')) # Adjunto a edades la edad de la persona en la posicion, haciendo uso de la funcion edad
    for e in edades: # Recorro edades y las acumulo en una variable
        acum = e + acum  
    promedio = acum / len(edades)  # promedio en base a el acumulador, y el largo de la lista de edades.
    return promedio


if __name__ == '__main__':
    names = ['Torres, Ana', 'Hudson, Kate','Quesada, Benicio', 'Campoamores, Susana',
    'Santamaria, Carlos', 'Skarsgard, Azul','Catalejos, Walter','Irastorza Rossia, Tobias']
    genders = ['f','f','m','f','m','f','m','m']
    births = ['02/05/1943','07/09/1984','10/02/1971','21/12/1967','30/01/1982','30/08/1995',
    '18/07/1959','11/08/1999']
    inicialMasApellido = iniciales_y_apellido(names)
    longestName = nombre_mas_largo(names)
    averageAge = promedio_edad_mujeres(names, genders, births)
    # Inicial y apellidos
    print('Iniciales y apellidos de las personas: ')
    for i in range(len(names)):
        print(inicialMasApellido[i])
    # Nombre mas largo
    print(f'El nombre mas largo es: {longestName}')
    # Promedio edad mujeres
    print(f'El promedio de edad de las mujeres es: {averageAge}')