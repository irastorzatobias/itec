from json import loads

people ='[{"name": "Lautaro", "age" : "25"}, {"name": "Tobias", "age" : "21"}]' 


k = loads(people)
print(k[0])

with open('pelis.json','r') as reader:
    lines = eval(reader.read().replace('\n',''))

print(lines[0]['Title'])
     

