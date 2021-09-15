from dataclasses import dataclass
import numpy

@dataclass
class Video:
    nombre:str
    visualizaciones:int
    actores:str

    def getActors(self):
        """ Retorna los actores que participan en el video"""
        actors = [a.strip() for a in self.actores.split(',')]
        return actors
    
    def getName(self):
        """ Titulo/Nombre del video"""
        return self.nombre


    def getVisualizations(self):
        """ visualizaciones del video """
        return self.visualizaciones


@dataclass
class Pelicula(Video):
    duracion:int
    def getDuration(self):
        """" Devuelve la duracion de la pelicula"""
        return self.duracion    


@dataclass
class Serie(Video):
    temporadas:int

    def getTemporadas(self):
        """ Devuelve las cantidad de temporadas de la serie"""
        return self.temporadas

@dataclass
class App: 
    pelis = [Pelicula("Inception", 4760183, 'Leonardo DiCaprio, Ellen Page, Joseph Gordon-Levitt', 148),
                    Pelicula("Batman Begins", 17319533, 'Christian Bale, Cillian Murphy, Michael Caine', 140),       
                    Pelicula("Inmortales", 35, 'Mirtha Legrand, Leonardo DiCaprio, Elizabeth The Second', 30)]
    
    series = [Serie("Peaky Blinders", 1234567, 'Cillian Murphy, Paul Anderson, Helen McCrory', 5),
    Serie("The Umbrella Academy", 2434908, 'Tom Hopper, Emmy Raver-Lampman, Ellen Page, David Castañeda', 2)]


    def setMovie(self, peli:Pelicula):
        mNames = [m.getName() for m in self.pelis]
        """ Agrega pelicula a la lista"""
        if type(peli)  != Pelicula:
            print('No es del tipo pelicula, no se agrego a la lista')
        elif peli.getName() in mNames:
            print('Ya existe esa pelicula en el registro, no se agrego a la lista')
        else:
            self.pelis.append(peli)


    def setSerie(self, serie:Serie):
        sNames = [s.getName() for s in self.series]
        """ Agrega serie a la lista"""
        if type(serie)  != Serie:
            print('No es del tipo serie, no se agrego a la lista')
        elif serie.getName() in sNames:
            print('Ya existe la serie, no se agrego a la lista')
        else:
            self.series.append(serie)

    
    
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
            pDuration = [p.getDuration() for p in self.pelis] 
            return numpy.sum(pDuration) / len(pDuration)
        elif tipo.lower() == 'serie':
            sDuration = [s.getTemporadas() for s in self.series]
            return numpy.sum(sDuration) / len(sDuration)   
        else:
            return f'No existe el tipo {tipo}'

    def worksInMoviesAndSeries(self):
        """ Actores que trabajan en pelis y en series"""
        pActors = sum([p.getActors() for p in self.pelis],[]) # actores peliculas
        sActors = sum([s.getActors() for s in self.series],[]) # actores series
        result = [a for a in (pActors + sActors) if (a in pActors and a in sActors)] # Actores en peliculas y series 
        return set(result) # devuelvo una lista con elementos que no se repitan

    def seriesBySeasons(self,qSeason):
        """ Filtra series por cantidad de temporadas"""
        result = [s for s in self.series if s.getTemporadas() >= qSeason]
        return result


if __name__ == '__main__':
    flix = App()
    print('Pelicula/s mas vista/s: ') 
    for p in flix.getMostViewedMovieSerie("pelicula"):
        print(p.getName()) 
    print(f'Promedio duracion de las peliculas: {flix.getAverageDuration("pelicula")}')
    print(f'Actores que trabajan en series y peliculas: {flix.worksInMoviesAndSeries()}')
    print('Series que tienen mas de tres temporadas: ')
    for s in flix.seriesBySeasons(3):
        print(s.getName())
    