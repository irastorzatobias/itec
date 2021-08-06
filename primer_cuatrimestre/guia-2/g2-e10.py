cantEmpleados= int(input('Ingrese cantidad de empleados: ')) 
empleadoNombre = []
empleadoSalario = []
min = 9999999
pos = 0


for i in range(cantEmpleados):
    print("Ingrese nombre de empleado", i)
    empleadoNombre.append(input())
    print("Ingrese el salario del empleado",i)
    empleadoSalario.append(int(input()))

for j in range(cantEmpleados):
    if(empleadoSalario[j] < min):
        min = empleadoSalario[j]
        pos = j;

print('La persona que menos cobra es', empleadoNombre[pos],'recibe un total de:',empleadoSalario[pos])