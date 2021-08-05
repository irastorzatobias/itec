print('LISTAS PARALELAS')
nombreList = []
sexList = []
aux = []

for i in range(8):
    print('Ingrese el nombre de la persona',i)
    nombreList.append(input())
    print('Ingrese el sexo de la persona',i,'(m/f)')
    sexList.append(input())
    if(sexList[i] == 'f'):
        aux.append(nombreList[i])

print('Nombre de mujeres que se le proporcionaron a la lista: ')
for i in range(len(aux)):
    print(aux[i])




    

