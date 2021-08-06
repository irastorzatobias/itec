num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

if num1 > num2:
    print(num2, num1)
elif num2 > num1:
    print(num1, num2)
else: 
    print("Son iguales")
    print(num1, num2)

