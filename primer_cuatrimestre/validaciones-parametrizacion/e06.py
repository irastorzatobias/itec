from e04 import input_con_opciones

def es_bisiesto(anio):
    return (anio % 400 == 0 and anio % 100 == 0) or (anio % 4 == 0 and anio % 100 != 0)


def fecha_valida():
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31,30, 31, 30, 31]
    mes = [1,2,3,4,5,6,7,8,9,10,11,12]
    validado = False
    while not validado:
        fecha = input_con_opciones('Ingrese una fecha','dd','mm','aaaa')
        if len(fecha) != 10: # chequeo largo string
            print('Valor invalido')
            validado = False 
        elif fecha[2] != '/' and fecha[5] != '/': # chequeo de formato de fecha.
            validado = False
            print('Valor invalido')
        else:
            try: 
                fechaSplit = fecha.split('/')
                dia = int(fechaSplit[0])
                mes = int(fechaSplit[1])
                anio = int(fechaSplit[2])
                if es_bisiesto(anio): # sumo uno a febrero si el anio es bisiesto
                    dias_mes[1] = dias_mes[1] + 1
                if dia > dias_mes[mes] + 1 or dia < 0 or mes < 0 or anio < 0: # chequeo mes, si es bisiesto le agrego un dia al mes correspondiente
                    validado = False
                else:
                    validado = True
                if validado: # si se cumple todo lo anterior, retorno lo pedido por la consigna
                    return anio, mes, dia
            except:
                validado = False
                print('Intente nuevamente')            


    
        

if __name__ == '__main__':
    print(fecha_valida())





