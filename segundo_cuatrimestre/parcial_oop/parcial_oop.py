# Tobias Irastorza

from validacion_entero import validacionEntero as vInt

class Mueble:
    def __init__(self, tipo, formato, precio):
        self.tipo = tipo
        self.formato = formato
        self.precio = precio

    def getTipo(self):
        return self.tipo
    
    def getFormato(self):
        return self.formato

    def getPrecio(self):
        return int(self.precio)


class Silla(Mueble):
    def __init__(self,pesoLimite,formato,precio, tipo = 'silla'):
        super().__init__(tipo,formato,precio)
        self.pesoLimite = pesoLimite

    def getPesoLimite(self):
        """ Devuelve el peso limite de la silla"""
        return self.pesoLimite

class Mesa(Mueble):
    def __init__(self, cantLugares,formato,precio, tipo = 'mesa'):
        super().__init__(tipo,formato,precio)
        self.tipo = 'mesa'
        self.cantLugares = cantLugares

    def getCantLugares(self):
        """ Retorna la cantidad de lugares disponibles de la silla"""
        return self.cantLugares

class Banqueta(Mueble):
    def __init__(self,respaldo,formato,precio, tipo = 'banqueta'):
        super().__init__(tipo,formato,precio)
        self.tipo = 'banqueta'
        self.respaldo = respaldo

    def getFija(self):
        """ Retorna si la banqueta es fija o si no lo es"""
        return self.formato
    
    def getRegulable(self):
        """ IDEM anterior, pero si es regulable o no"""
        return self.respaldo


class Fabrica:
    def __init__(self):
       self.sillas = []
       self.mesas = [] 
       self.banquetas = []  
       # Cargo muebles de antemano, no es lo correcto por que si no existe el archivo puede causar problema
       self.loadStock('stock_muebles.csv')
    
    def loadStock(self, file):
        """ Carga stock con el file csv brindado por profesor"""
        try:
            with open(file, 'r') as f:
                aux = f.readlines()
                final = []
                for i in range(1,len(aux)):
                    final.append(aux[i].strip())
            for mueble in final:
                muebleAux = mueble.split(',')
                if 'mesa' in muebleAux:
                    self.mesas.append(Mesa(muebleAux[4],muebleAux[1],muebleAux[2]))
                elif 'banqueta' in muebleAux:
                    self.banquetas.append(Banqueta(muebleAux[5],muebleAux[1],muebleAux[2]))
                elif 'silla' in muebleAux:
                    self.sillas.append(Silla(muebleAux[3],muebleAux[1],muebleAux[2]))
        except:
            print('No existe el archivo')

    
    def setMueble(self):
        """ Agrega mueble con inputs a la lista actual de la fabrica"""
        tipoMueble = input('Ingrese el tipo de mueble que quiere agregar: (silla, banqueta, mesa)\n')
        while tipoMueble.lower() not in ['silla','mesa','banqueta']:
            tipoMueble = input('El mueble no existe, intente nuevamente:\n')
        if tipoMueble.lower() == 'silla':
            pesoLimite = vInt('Peso limite silla: ')
            formatoSilla = input('Formato silla (alta,baja): ')
            while formatoSilla not in ['alta','baja']:
                formatoSilla = input('Formato no coincide, intente nuevamente (alta,baja): ')
            precio = vInt('Precio silla: ')
            self.sillas.append(Silla(pesoLimite, formatoSilla, precio))
        elif tipoMueble.lower() == 'mesa':
            cLugaresMesa = vInt('Cantidad de lugares mesa: ')
            formatoMesa = input('Formato mesa (rectangular, cuadrado): ')
            while formatoMesa not in ['rectangular', 'cuadrado']:
                formatoMesa = input('Formato mesa incorrecto, intente nuevamente (rectangular, cuadrado): ')
            precio = vInt('Precio mesa: ')
            self.mesas.append(Mesa(cLugaresMesa, formatoMesa, precio))
        elif tipoMueble.lower() == 'banqueta':
            pRespaldo = input('Posee respaldo (s/n)?: ')
            formatoBanqueta = input('Formato banqueta (fija, regulable): ')
            while pRespaldo not in ['s','n'] or formatoBanqueta not in ['fija', 'regulable']:
                print('Ingreso mal el formato, intente nuevamente: ')
                pRespaldo = input('Posee respaldo (s/n)?: ')
                formatoBanqueta = input('Formato banqueta (fija, regulable): ')
            precio = vInt('Precio banqueta: ')
            self.banquetas.append(Banqueta(pRespaldo, formatoBanqueta, precio))

    def filterByPrice(self, price:int):
        """ Filtra los muebles por precio"""
        tMuebles = self.banquetas + self.sillas + self.mesas
        filteredMuebles = [m for m in tMuebles if m.getPrecio() > price]
        print(f'Muebles con un precio mayor a {price}: ')
        for m in filteredMuebles:
            print(f'Mueble: {m.getTipo()}. Tipo: {m.getFormato()}. Precio: {m.getPrecio()}')

    def filterByMueble(self, mueble, formato):
        """ Filtra por mueble, pasandole como argumento un mueble y su formato determinado"""
        tMuebles = self.banquetas + self.sillas + self.mesas
        filteredMuebles = [m for m in tMuebles if type(m).__name__ == mueble.title() and m.getFormato() == formato.lower()]
        if len(filteredMuebles) >= 1:
            print(f'Mueble: {mueble}. Tipo: {formato}. Stock: {len(filteredMuebles)}')
        else:
            print(f'No existen muebles {mueble}. Del tipo {formato}')




if __name__ == '__main__':     
    muebleria = Fabrica()   
    print('Agregando producto...')
    muebleria.setMueble()
    print('\nFiltrando por precio: ')
    muebleria.filterByPrice(12000)
    print('\nFiltrando por mueble: ')
    muebleria.filterByMueble('banqueta','fija')
    

        