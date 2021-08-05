# Tobias Irastorza

# Los diccionarios fueron utilizados a modo de practica, probablemente no eran necesarios pero era mas organizado asi.
from datetime import date

today = date.today()


def deudoresGeneral(file):
    deudores = []
    with open(file,'r') as reader: # Probando with as. 
        aux = reader.readlines()
        result = []
        resultSplit = []
        for e in aux:
            result.append(e[:-1]) #Almaceno lista de elementos sin el salto de linea
        for i in range(1,len(result)):
        # print(result[])
            resultSplit = result[i].split(',') # Result split contiene cada valor de la linea, separada por coma
            deudores.append({ # Append a deudores, probando diccionarios
                    'id': resultSplit[0],
                    'name': resultSplit[1],
                    'email': resultSplit[2],
                    'gender': resultSplit[3],
                    'debt': float(resultSplit[4][1:]), # Saco el signo $$$
                    'date': resultSplit[5],
                    'city': resultSplit[6]
            })
    return deudores


def morosos(file, deudores):
    morosos = []
    f = open(file, 'w')
    f.write('name'+ ',' + 'email' + ',' + 'debt' + '\n') # Escribo encabezado requerido por la consigna
    f.close
    for i in range(len(deudores)): # Recorro mi diccionario deudores
        deudoresDebtYear = deudores[i]['date'].split('/') # Spliteo fecha 
        deudoresDebtYear = int(deudoresDebtYear[2]) # Obtengo el año y lo convierto en entero para poder comparar
        if float(deudores[i]['debt']) > 200000 and deudoresDebtYear < today.year: # Si el debito es mayor a 200000 y el año de la deuda es menor al año actual, appendeo eso a morosos
            morosos.append({
                'name': deudores[i]['name'],
                'email': deudores[i]['email'],
                'debt': str(deudores[i]['debt']) # Convierto en str para poder modificarlo despues
            })
    for i in range(len(morosos)):
        dotPosition = morosos[i]['debt'].find('.') # Encuentro la posicion del punto en la deuda, para eliminar los centimos
        f = open(file,'a') #Abro el archivo, con la instriuccion 'a' correspondiente a append
        f.write(morosos[i]['name'] + ',' + morosos[i]['email'] + ',' + morosos[i]['debt'][:dotPosition] + '\n')

dicDeudores = deudoresGeneral('deudores.txt') # Guardo el diccionario con la informacion
morosos('morosos.txt', dicDeudores) # Genero el archivo morosos, pasando como parametro tambien mi diccionario dicDeudores

