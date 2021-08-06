num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
operacion = input("Ingrese la operacion: ")

if operacion == "+":
    resultado = num1 + num2
    print("La operación es suma, el resultado es: ", resultado)
elif operacion == "-":
    if num1 > num2 or num1 == num2:
        resultado = num1 - num2
        print("La operación es resta, el resultado es: ", resultado)
    elif num1 < num2:
        resultado = num2 - num1
        print("La operación es resta, el resultado") 
else:
    print("La operación no es válida")
    