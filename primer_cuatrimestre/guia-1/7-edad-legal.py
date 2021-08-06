name = input("Ingrese el nombre: ")
operacion = input("Ingrese el simbolo: ")

if operacion == "<":
    print(name, "es menor")
elif operacion == ">":
    print(name, "es mayor")
else:
    print("Operación inválida")