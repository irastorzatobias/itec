# Crear una aplicacion para gestionar un videoclub

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
    
    
    
    