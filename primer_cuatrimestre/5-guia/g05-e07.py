def carga(cantidad, nombres, sexo):
    for i in range(cantidad):
        print('Ingrese el nombre de la persona',i)
        nombres.append(input())
        print('Ingrese el sexo de la persona',i,'(m/f)')
        sexo.append(input())

def mostrarMujeres(nombres, sexo):
    aux = []
    for i in range(len(nombres)):
        if sexo[i].lower() == 'f':
            aux.append(nombres[i])
    return aux;

names = []
sex = [] 
carga(8,names,sex)

womens = mostrarMujeres(names,sex)
print('-- MUJERES --')
print(womens)
