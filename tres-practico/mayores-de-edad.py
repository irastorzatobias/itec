from datetime import date
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




def mayores_de_edad(file):
    f = open(file,'r') # Leo archivo
    aux = f.readlines() # Almaceno en aux las lineas
    result = []
    names = []
    births = []
    edades = []
    edadesMayores = []
    mayores = []
    for i in aux:
        result.append(i[:-1]) # Almaceno en result un array con las lineas sin el salto de linea \n
    for i in range(len(result)): 
        resultSplit = result[i].split(',') # Spliteo nombre y fecha y lo guardo en listas paralelas
        names.append(resultSplit[0])
        births.append(resultSplit[1])
    for i in range(len(names)):
        edades.append(edad(births[i],'/'))
        if edades[i] >= 18:
            mayores.append(names[i])
            edadesMayores.append(edades[i])
    f.close()
    return mayores, edadesMayores # Devuelve una tupla con listas paralelas, una con los nombres y otra con las edades  

if __name__ == '__main__':
    print('-- MAYORES DE EDAD --')
    print(mayores_de_edad('alumnos-itec.txt'))
