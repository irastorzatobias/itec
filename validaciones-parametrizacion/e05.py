
def creador_de_menu(**kwargs):
    funciones = []
    i = 0
    try:
        for k,v  in kwargs.items():
        # Imprime la lista
            print(i,'-', v)
            i = i + 1 
        # agrega a funciones una string que simula el llamado a la funcion
            funciones.append(k+'()')
        opcion = int(input('Elegi una opcion: '))
        while opcion >= len(funciones):
            
            opcion = int(input(f'Opcion {opcion} no existe, intente de nuevo: '))
            
        return eval(funciones[opcion])
    except:
        return f'Funcion {funciones[opcion]} no disponible por el momento'

    
        


print(creador_de_menu(opcion0='Opcion 0',opcion1 = 'Opcion 1', opcion2 = 'Opcion 2'))