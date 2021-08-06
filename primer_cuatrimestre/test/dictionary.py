'''persona = [{'name' : 'Tobias', 'age' : 21, 'gender' : 'm'},
{'name' : 'Patricia', 'age' : 50, 'gender' : 'f'}
]

female = []

for x in persona:
    print(x)
    if x['gender'] == 'f':
        female.append(x)
print('Females:')
print(female)
# persona.keys()
# persona.values()
# persona.items() key/value pairs tuples
# persona.popitem()  last key
# persona.pop('name') # key selected
# persona['works'] = 'yes' True adding a new key/value pair
# personaCopy = persona.copy() # copiar el diccionario
# print('test')
# print(persona)
# print(personaCopy)
'''
empleados = []
cantEmpleados = int(input('Ingrese cantidad de empleados: '))
nombre = '';
edad = 0;
menor = 9999999
pos = 0
for i in range(cantEmpleados):
    print('Ingrese nombre empleado',i)
    nombre = input()
    print('Ingrese edad: ')
    edad = int(input())
    salario = int(input('Ingrese salario: '))
    empleados.append({'nombre': nombre, 'edad': edad,'salario':salario})

for j in range(len(empleados)):
    if empleados[j]['salario'] < menor:
        menor = empleados[j]['salario']
        pos = j


print('El empleado que gana menos es:',empleados[pos]['nombre'],'. Gana un total de: ',empleados[j]['salario'])
