
autos = []
precio = 999
contador = 0
i = 0
while precio != 0:
    print("Valor de auto numero",i)
    precio = int(input())
    autos.append(precio)
    i+=1

for i in range(len(autos)):
    if(autos[i] > 1460000 and autos[i] < 2850000):
        contador = contador + 1

print("La cantidad de autos que oscilan su precio entre 1.460.000 y 2.850.000 es:", contador)