def conversion_cadena(cadena):    
    auxMale = []
    auxFemale = []
    cadenaSplit = cadena.split(',')
    for i in range(0,len(cadenaSplit),3):
        if cadenaSplit[i + 2] == 'f':
            auxFemale.append(cadenaSplit[i:i+2])
        else:
            auxMale.append(cadenaSplit[i:i+2])
    maleNameBefore = []
    maleNumberBefore = []
    femaleNameBefore = []
    femaleNumberBefore = []
    for i in range(len(auxMale)):
        maleNameBefore.append(auxMale[i][0])
        maleNumberBefore.append(auxMale[i][1])
        femaleNameBefore.append(auxFemale[i][0])
        femaleNumberBefore.append(auxFemale[i][1])
    return maleNameBefore, maleNumberBefore, femaleNumberBefore, femaleNameBefore

    
maleNameNow = ['Liam', 'Noah', 'Michael', 'James', 'Oliver']
maleNumberNow = [19837, 18267, 14516, 13525, 13389,]

femaleNameNow = ['Emma', 'Olivia', 'Ava', 'Isabella', 'Sophia']
femaleNumberNow = [18688, 17921, 14924, 14464, 13928]

datosViejos = "Eva,17039,f,Daniel,19005,m,Emily,17434,f,Emma,18813,f,Ethan,20216,m,Julia,18616,f,Jacob,22594,m,Joshua,19205,m,Michael,20626,m,Olivia,17081,f"

hNombresAntes,hCantidadAntes,fNombresAntes, fCantidadAntes = conversion_cadena(datosViejos)


def busqueda_nombre(year, position, gender):
    conversionCadena, 
    if year == 2018 and gender == 'm':
        return maleNameNow[position], maleNumberNow[position]
    elif year == 2018 and gender == 'f':
        return femaleNameNow[position], femaleNumberNow[position]
    elif year == 2008 and gender == 'm':
        return hNombresAntes[position], hCantidadAntes[position]
    elif year == 2008 and gender == 'm':
        return fNombresAntes[position], hCantidadAntes[position]
    else:
        return 'Argumentos incorrectos'

def busqueda_nombre_anio(name, year, datosViejos, datosNuevos):
    