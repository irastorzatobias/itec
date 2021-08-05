cantPersonas = int(input('Ingrese la cantidad de personas: '))
nombrePersona = []
sexoPersona = [] 
totalMujeres = 0
nombreMujeres = []
for i in range(cantPersonas):
    print('Ingrese el nombre de la persona',i)
    nombrePersona.append(input())
    print('Ingrese el sexo de la persona',i,'(m/f)')
    sexoPersona.append(input())
    if(sexoPersona[i] == "f"):
        totalMujeres += 1
        nombreMujeres.append(nombrePersona[i])
    

print('Hay',totalMujeres,'mujer/es')
for j in range(totalMujeres):
    print('La mujer',j,'se llama',nombreMujeres[j])

