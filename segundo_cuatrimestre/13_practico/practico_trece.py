from dataclasses import dataclass
import numpy


@dataclass
class PeliSerie:
    nombre:str
    visualizaciones:int
    actores:list
    duracion:int

    def getActors(self):
        actors = [a.strip() for a in self.actores.split(',')]
        return actors
    
    def getName(self):
        return self.nombre
    
    def getDuration(self):
        return self.duracion 

    def getVisualizations(self):
        return self.visualizaciones


@dataclass
class App: 
    pelis = [PeliSerie("Inception", 4760183, 'Leonardo DiCaprio, Ellen Page, Joseph Gordon-Levitt', 148),
                    PeliSerie("Batman Begins", 17319533, 'Christian Bale, Cillian Murphy, Michael Caine', 140),       
                    PeliSerie("Inmortales", 35, 'Mirtha Legrand, Leonardo DiCaprio, Elizabeth The Second', 30)]
    
    series = [PeliSerie("Peaky Blinders", 1234567, 'Cillian Murphy, Paul Anderson, Helen McCrory', 5),
    PeliSerie("The Umbrella Academy", 2434908, 'Tom Hopper, Emmy Raver-Lampman, Ellen Page, David Castañeda', 2)]


    def getMostViewedMovieSerie(self,tipo):
        """ Pelicula / serie mas vista/o """ 
        if tipo.lower() == 'pelicula':
            maxVisualizaciones = max([m.getVisualizations() for m in self.pelis]) 
            return [p for p in self.pelis if p.getVisualizations() == maxVisualizaciones ]
        elif tipo.lower() == 'serie':
            maxVisualizaciones = max([m.getVisualizations() for m in self.series]) 
            return [p for p in self.pelis if p.getVisualizations() == maxVisualizaciones]
        else:
            return f'No existe el tipo {tipo}'
        
        
    def getAverageDuration(self, tipo):
        """ Duracion promedio de la pelicula o serie"""
        if tipo.lower() == 'pelicula':
            pDuration = [d.getDuration() for d in self.pelis] 
            return numpy.sum(pDuration) / len(pDuration)
        elif tipo.lower() == 'serie':
            sDuration = [s.getDuration() for s in self.series]
            return numpy.sum(sDuration) / len(sDuration)   
        else:
            return f'No existe el tipo {tipo}'

    def worksInMoviesAndSeries(self):
        pActors = []
        sActors = []
        bothActors = []
        result = []
        for p in self.pelis:
            for a in p.getActors():
                pActors.append(a)
        for s in self.series:
                for a in s.getActors():
                    sActors.append(a)
        bothActors = pActors + sActors
        result = [a for a in bothActors if (a in pActors and a in sActors)]
        return set(result)

    def seriesBySeasons(self,qSeason):
        """ Filtra series por cantidad de temporadas"""
        result = [s for s in self.series if s.getDuration() >= 3]
        return result
    
    def printMovieSerie(self, l):
        for p in l:
            print(f'Nombres: {p.getName()}')
            print(f'Actores: {p.getActors()}')
            print(f'Duracion / Temporadas: {p.getDuration()}')
            print(f'Visualizaciones: {p.getVisualizations()}')


if __name__ == '__main__':
    flix = App()
    print(f'Pelicula mas vista: {flix.getMostViewedMovieSerie("pelicula")[0].getName()}')
    print(f'Promedio duracion de las peliculas: {flix.getAverageDuration("pelicula")}')
    print(f'Actores que trabajan en series y peliculas: {flix.worksInMoviesAndSeries()}')
    print('Series que tienen mas de tres temporadas: ')
    for s in flix.seriesBySeasons(3):
        print(s.getName())

        