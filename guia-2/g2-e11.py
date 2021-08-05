nums = []

for i in range(7):
    print('Ingrese el numero',i)
    nums.append(int(input()))

for j in range(len(nums)):
    if(type(nums[j]) == int and nums[j] < 10):
        print(nums[j], 'es un numero natural de una cifra')



        