num = float(input("Ingrese un numero: "))


if num > 0 and num < 10:
    print("Numero de un dígito")
elif num > 9 and num < 100:
    print("Numero de dos dígitos")
else:
    print("Numero de tres digitos o mas") 