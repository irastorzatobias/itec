pasajeCordoba = 1700
name = input("Ingrese su nombre: ")
edad = float(input("Ingrese su edad: "))

if (edad > 4 and edad < 11) or (edad > 65):
    print("Obtuvo una bonificacion en el pasaje")
    print("Tiene que abonar", pasajeCordoba - pasajeCordoba * 0.40)
else:
    print("Tiene que abonar", pasajeCordoba)

