
nombres = []
edades = []
diferencia = 0
for i in range(2):
    print('Ingrese el nombre de la persona:',i+1)
    nombres.append(input())
    edades.append(int(input('Ingrese la edad: ')))

if edades[0] > edades[1]:
    diferencia = edades[0] - edades[1]
    print(nombres[0],'le lleva',diferencia,'año/s a',nombres[1])
elif edades[1] > edades[0]:
    diferencia = edades[1] - edades[0]
    print(nombres[1],'le lleva',diferencia,'año/s a',nombres[0])
elif edades[0] == edades[1]:
    print('Tienen la misma edad')
else:
    print('Datos incorrectos')