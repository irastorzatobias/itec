cantEmpleados = int(input("Ingrese cantidad de empleados: "))
sueldo = []
sumaTotal = 0

for i in range(cantEmpleados):
    print("Ingrese el sueldo del empleado",i)
    aux = int(input())
    sueldo.append(aux)

for j in sueldo:
    sumaTotal = sumaTotal + j

print('El monto total de todos los sueldos es de:',sumaTotal)
