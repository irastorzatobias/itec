def verano(fecha):
    a, m, d = list(map(int,fecha.split('-')))
    return a, m, d

print(verano('2020-10-12'))