nombres = ['Tobias', 'Lautaro', 'Marcelo', 'Patricia']
boke = open('boca.txt','w')
for i in range(20):
    boke.write('Lorem\n')
boke.writelines(nombres + '\n')
boke.close

