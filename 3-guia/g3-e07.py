notas = []
acum = 0
promedio = 0
for i in range(8):
    notas.append(int(input('Ingrese un numero: ')))
    acum = acum + notas[i]

promedio = acum / 7

for j in range(len(notas)):
    if notas[j] > promedio:
        print(notas[j],'es mayor que el promedio que es:',promedio)


