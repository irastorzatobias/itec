dias = ['domingo', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado']
cantLluvia = []
lluviaTotal = 0
maxLluvia = 0
pos = 0
for i in range(len(dias)):
    print('Ingrese la lluvia en mm para el dia',dias[i])
    cantLluvia.append(int(input()))
    lluviaTotal = lluviaTotal + cantLluvia[i]
    if(cantLluvia[i] > maxLluvia):
        maxLluvia = cantLluvia[i]
        pos = i

print('Lluvia total:',lluviaTotal)
print('Dia que mas llovio fue el',dias[pos],'con un total de',cantLluvia[pos],'mm')
