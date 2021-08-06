peticionDatos = input("Posee datos para ingresar? (s/n): ")

while(peticionDatos == "s"):
    valor = int(input("Ingrese el valor entero que desea agregar: "))
    if(valor > 0):
        print("El valor es positivo")
    else:
        print("El valor es negativo")
    peticionDatos = input("Desea ingresar otro valor?: ")

print("Fin")


    