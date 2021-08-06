cantPersonas = int(input('Ingrese la cantidad de personas a cargar: '))
nombrePersona = []
diaNacimiento = []
mesNacimiento = []
anioNacimiento = []
aux = []

for i in range(cantPersonas):
    print('Ingrese nombre de persona',i)
    nombrePersona.append(input())
    print('Ingrese dia de nacimiento: ')
    diaNacimiento.append(int(input()))
    print('Ingrese mes de nacimiento: ')
    mesNacimiento.append(int(input()))
    print('Ingrese anio de nacimiento: ')
    anioNacimiento.append(int(input()))

for j in range(cantPersonas):
    if(anioNacimiento[j] < 2003):
        aux.append(nombrePersona[j])
    elif(anioNacimiento[j] == 2003):
        if(mesNacimiento[j] < 4):
            aux.append(nombrePersona[j])


print('Personas mayores de edad:\n',aux)

