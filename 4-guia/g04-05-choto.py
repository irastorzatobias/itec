n = input('Ingrese el numero: ')
s = ''
i = len(n)
print(i)
while(i != 0):
    s = s + n[len(n) - 1 - i]
    if i % 3 == 0:
        s = s + '.'
    i = i - 1

print(s)
