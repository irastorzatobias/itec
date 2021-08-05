nums = input('Ingrese el numero: ')
new = ''
for i in reversed(range(len(nums))):
    print(i)
    new = new + nums[len(nums)- 1 - i]
    if i % 3 == 0 and i != 0:
      new = new + '.'

print(new)



    




