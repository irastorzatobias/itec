cantPersonas = int(input('Ingrese la cantidad de personas a cargar al sistema: '))
nombrePersona = []
sexoPersona = []
mujeres = []
totalMujeres = 0
for i in range(cantPersonas):
    print('Ingrese nombre persona',i)
    nombrePersona.append(input())
    print('Ingrese sexo (m/f)')
    sexoPersona.append(input())
    if(sexoPersona[i] == 'f'):
        mujeres.append(nombrePersona[i])
        totalMujeres = totalMujeres + 1

print('Total mujeres:',totalMujeres)
print(mujeres)

