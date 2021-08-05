cantNums = int(input("Cantidad de numeros a ingresar: "))
nums = []

for i in range(cantNums):
    print("Valor",i)
    aux = float(input())
    nums.append(aux)

continuar = input("Desea agregar un nuevo numero? (s/n): ")
while continuar != "n":
    aux = float(input("Ingrese el nuevo numero: "))
    nums.append(aux)
    continuar = input(("Ya fueron agregados los numeros, desea agregar más?: "))
    
for j in range(len(nums)):
    max = 0
    min = 999
    if(nums[j] > max):
        max = nums[j]
        posicion = j
    elif(nums[j] < min):
        min = nums[j]
        posicion = j

print('El numero de mayor valor que se encontro es:', max)
