# Crear una aplicacion para gestionar un videoclub
from os import system
from validacion_entero import validacionEntero



def seguirPrograma():
    sigue = input('Ingrese cualquier tecla para continuar, "Q" para finalizar: ')
    if sigue.lower() == 'q':
        return False  
    else:
        return True


class Pelicula:
    def __init__(self, titulo, precioAlquiler,genero, anio, director, protagonista):
        self.titulo = titulo
        self.precioAlquiler = precioAlquiler
        self.diasAlquiler = 0
        self.alquilado = False
        self.genero = genero
        self.anio = anio
        self.director = director
        self.protagonista = protagonista
        
    
    def setDiasAlquiler(self, diasAlquiler):
        """ Establece los dias de alquiler de la pelicula"""
        self.diasAlquiler = diasAlquiler
        self.alquilado = True
    
    
    
    def getAlquilado(self):
        """ Chequea si la pelicula esta alquilada o no"""
        return self.alquilado
    
    def getMovie(self):
        print(f'Nombre: {self.titulo}')
        print(f'Genero: {self.genero}')
        print(f'Director: {self.director}')
        print(f'Protagonista: {self.protagonista}')
        print(f'Año: {self.anio}')
        print(f'Costo alquiler: {self.precioAlquiler}')
        if self.getAlquilado():
            print(f'Pelicula ya alquilada, dias restantes de alquiler {self.diasAlquiler}')
        print('\n')
        
    def getMovieName(self):
        return self.titulo
    


class Cliente:
    def __init__(self,nombre:str, direccion:str, telefono: int):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.alquiladas = []
        pass

    def setMovie(self, movie:Pelicula):
        if type(movie) == Pelicula:
            self.alquiladas.append(movie)
        else:
            print('No se agrego la pelicula, no es del tipo pelicula.')
        pass
    
    def getCliente(self):
        print(f'Nombre: {self.nombre} ')
        print(f'Direccion: {self.direccion} ')
        print(f'Telefono: {self.telefono} ')
        if len(self.alquiladas) >= 1:
            print('\nPeliculas alquiladas: ')
            for p in self.alquiladas:
                print(p.getMovie())
        print('\n')

    

class Videoclub:
    def __init__(self):
        self.clientes = [Cliente('Cliente0', 'Direccion', 12345),
        Cliente('Cliente1', 'Direccion1', 12345),
        Cliente('Cliente2', 'Direccion2', 12345),
        Cliente('Cliente3', 'Direccion3', 12345)]
        self.peliculas = [Pelicula('Pelicula0',200,'Genero',1999,'Director','Protagonista'),
        Pelicula('Pelicula1',200,'Genero1',1999,'Director1','Protagonista1'),
        Pelicula('Pelicula2',200,'Genero2',1999,'Director2','Protagonista2'),
        Pelicula('Pelicula3',200,'Genero3',1999,'Director3','Protagonista3')]
    
    def setCliente(self,cliente:Cliente):
        if type(cliente) == Cliente:
            self.clientes.append(cliente)
        else:
            print('No se agrego el cliente, no es del tipo Cliente, intente nuevamente')

    def printMovies(self):
        """ Printea todas las peliculas disponibles"""
        for i in range(len(self.peliculas)):
            print(f'Pelicula {i + 1}')
            self.peliculas[i].getMovie()
    
    def addMovies(self):
        """ Agrega una pelicula a la lista de peliculas"""
        titulosPeliculas = list(map(lambda x: x.getMovieName().lower(),self.peliculas))
        print(titulosPeliculas)
        titulo = input('Ingrese el titulo de la pelicula: ')
        if titulo.lower() not in titulosPeliculas:
            precio = validacionEntero('Precio alquiler de la pelicula: ')
            genero = input('Ingrese el genero de la pelicula: ')
            anio = validacionEntero('Anio de la pelicula: ')
            director = input('Director de la pelicula: ')
            protagonista = input('Protagonista de la pelicula: ')
        else:
            print('La pelicula ya existe, no se agrego')
    
    def printMoviesName(self):
        titulosPeliculas = list(map(lambda x: x.getMovieName().lower(),self.peliculas))
        print('Peliculas disponibles: ')
        for i in range(len(titulosPeliculas)):
            print(f'{i} - {titulosPeliculas[i]}')
    
    def chooseMovie(self, num:int):
        """" Retorna la pelicula correspondiente en la lista."""
        try:
            return self.peliculas[num]
        except:
            return f'No existe la pelicula'
    
    def printClients(self):
        """ Printea los clientes"""
        for i in range(len(self.clientes)):
            print(f'Cliente {i + 1}')
            self.clientes[i].getCliente()

    def rentMovie(self, num, cliente):
        pass

        
    def menu(self):
        menu = {}
        sigue = True

        menu['1'] = 'Lista peliculas'
        menu['2'] = 'Añadir pelicula'
        menu['3'] = 'Ficha producto'
        menu['4'] = 'Lista clientes'
        menu['5'] = 'Añadir cliente'
        menu['6'] = 'Ficha cliente'
        menu['7'] = 'Alquiler producto'
        menu['8'] = 'Salir'
        while sigue:
            system('clscd ')
            for k,v in menu.items():
                print(f'{k} - {v}')
            opcion = validacionEntero('Ingrese una opcion: ')
            if opcion == 1:
                system('cls')
                self.printMovies()
                sigue = seguirPrograma()
            elif opcion == 2:
                system('cls')
                self.addMovies()
                sigue = seguirPrograma()
            elif opcion == 3:
                system('cls')
                self.printMoviesName()
                numPeli = validacionEntero('Ingrese el numero correspondiente a la pelicula: ')
                peliElegida = self.chooseMovie(numPeli)
                if type(peliElegida) == Pelicula:
                    system('cls')
                    peliElegida.getMovie()
                else:
                    system('cls')
                    print(peliElegida)
                sigue = seguirPrograma()
                
            elif opcion == 8:
                sigue = False   
                



if __name__ == '__main__':
    videoclub = Videoclub()
    pelicula = Pelicula('Peliculita',200,'None',1999,'none','None') 
    videoclub.menu()
    print('Salio del menu')

    
    