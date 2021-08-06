def cargarPersonas(file): # Recibe como parametros el directorio donde guardar los datos
    nombres = []
    nacimientos = []
    formatoNacimientos = False
    cantPersonas = int(input('Ingrese la cantidad de personas que desea cargar: '))
    for i in range(cantPersonas):
        print(f'Ingrese el nombre de la persona {i + 1}')
        nombres.append(input())
        print(f'Ingrese la fecha de nacimiento de la persona {i + 1} (dd/mm/aaaa)')
        nacimientos.append(input())
        while('/' not in nacimientos[i] or len(nacimientos[i]) < 10):
            print('Formato incorrecto, ingrese de nuevo el valor: ')
            nacimientos[i] = input()
    f = open(file,'w')
    for i in range(len(nombres)): # Recorro nombres y nacimientos
        f.write(nombres[i] + ', ' + nacimientos[i] + '\n') # 
    f.close()



if __name__ == "__main__":
    cargarPersonas('alumnos-itec.txt')



