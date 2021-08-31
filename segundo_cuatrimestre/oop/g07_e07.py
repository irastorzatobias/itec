from g07_e02 import Auto # el metodo antiguedad fue agregado a la clase en el archivo de la g07_e02 y el ejercicio fue realizado en el programa principal

if __name__ == '__main__':
    autos = []
    autosAntiguos = []
    auto1 = Auto('gol',2003)
    auto2 = Auto('bora',2020)
    auto3 = Auto('clio',2005)
    autos.append(auto1)
    autos.append(auto2)
    autos.append(auto3)
    autosAntiguos = [car for car in autos if car.getAntiguedad() >= 5]
    print('Autos con antiguedad mayor o igual a 5 años: ')
    for e in autosAntiguos:
        print(e.getMarca().title(), e.getAnio())