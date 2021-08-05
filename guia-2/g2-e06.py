cantidadPersonas = int(input("Ingrese la cantidad de personas a cargar: "))
personas = []
acum = 0
for i in range(cantidadPersonas):
    print("Ingrese la edad de la persona",i)
    aux = int(input())
    personas.append(aux)
    acum = acum + personas[i]


promedio = acum / cantidadPersonas
print("El promedio de edad es:",promedio)

