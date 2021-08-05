llovio = []
lluviaPorDia = []
dias = ['domingo', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado']
noLlovio = 0
aux = 0
lluviaTotal = 0
for i in range(7):
    print('Ingrese si llovio o no el dia',dias[i],'(s/n)')
    llovio.append(input())
    if(llovio[i] == 's'):
        print('Ingrese cantidad de lluvia en el dia: ')
        lluviaPorDia.append(int(input()))
        aux = aux + lluviaPorDia[i]
        lluviaTotal = aux
    else:
        noLlovio += 1

print('Lluvia total:', lluviaTotal)
print('Dias que no llovio: ', noLlovio)





