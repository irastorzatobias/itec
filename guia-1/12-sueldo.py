diasNoTrabajados = int(input("Ingrese la cantidad de dias no trabajados: "))
anioIngreso = int(input("Año de ingreso a la empresa: "))
sueldoBasico = 47000
if anioIngreso < 2016 and diasNoTrabajados == 0: 
    print("-- Beneficio por antiguedad y asistencia --")
    print("Sueldo:", sueldoBasico + sueldoBasico * 0.30)
else:
    print("Su sueldo es: ", sueldoBasico)

