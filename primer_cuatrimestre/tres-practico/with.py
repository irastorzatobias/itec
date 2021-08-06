file = open('alumnos-itec.txt','r')

with file as reader:
    for e in reader.readlines():
        print(e[:-1])
    


    
    