num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 > num2:
    print(num1, "es mayor que", num2)
elif num1 < num2:
    print(num2, "es mayor que", num1)
elif num1 == num2:
    print("Los numeros son iguales")
else:
    print("Valor inválido")