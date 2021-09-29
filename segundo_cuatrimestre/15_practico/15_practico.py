from dataclasses import dataclass
import random

@dataclass
class Carta:
    palo:str
    valor:str

    def puntaje_carta(self):
        """ Retorna el valor de la carta"""
        if self.valor in ['J', 'Q','K']:
            return 10
        if self.valor in (2, 3, 4, 5, 6, 7, 8, 9, 10):
            return self.valor  
        if self.valor == "A":
            return 1




@dataclass
class Mazo:
    palos = ("Pique", "Corazón", "Diamante", "Trébol")
    valores = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")
    cartas = []


    def shuffle(self):
        """ Mezcla las cartas """
        random.shuffle(self.cartas)
        
    def dar_carta(self):
        """ Da una carta"""
        carta = self.cartas.pop()
        return carta
        
    def cargar_mazo(self):
        """ Carga mazo con todas las cartas y ya lo mezcla por defecto"""
        self.cartas = [Carta(p,v) for p in self.palos for v in self.valores]
        self.shuffle()
        
        

@dataclass
class Jugador:
    mano = []
    puntos = 0
    def mostrar_mano(self):
        """ Muestra las cartas del jugador """
        for c in self.mano:
            print(c)

    def aces(self):
        """ Cuenta los aces del jugador"""
        return len([a for a in self.mano if a.valor == 'A']) # retorna cantidad de aces del jugador

    def puntaje(self):
        """ Determina el puntaje """
        return sum([c.puntaje_carta() for c in self.mano])

    def puntaje_con_ases(self):
        """ Ajusta el puntaje en caso de que el usuario tenga ases"""
        self.puntos = self.puntaje()
        print(self.aces())
        for i in range(self.aces()):
            if self.puntos < 12:
                self.puntos += 10 # sumo 10 porque anteriormente ya le sume 1 si es que habia una A
        return self.puntos
    
    def setCarta(self, carta):
        self.mano.append(carta)
    
    def perdio(self):
        return self.puntaje_con_ases > 21


@dataclass
class Dealer(Jugador):
    # si no inicializo mano nuevamente, se me repite el append, desconozco el motivo
    mano = []
    # Redefino el metodo mostrar mano
    
    def mostrar_mano(self,mostrar=False):
        """ Muestra la mano, en caso de que mostrar sea falso, muestra solo una carta, caso contrario, muestra ambas cartas"""
        if mostrar: 
            for c in self.mano:
                print(c)
        else:
            print(self.mano[0])
            print('???')
    




@dataclass
class Blackjack:  
    mazo = Mazo()
    mazo.cargar_mazo()
    jugadores = [Jugador(), Dealer()]
    turnoJugador = True
    
    def mostrarJugadores(self):
        """ Muestra los jugadores """
        print(f'Cantidad de jugadores: {len(self.jugadores)}')
        for i,j in enumerate(self.jugadores):
            print(f' {i} - {type(j).__name__}')
    
    def repartir_cartas(self):
        """ Reparte 2 cartas para cada uno de los jugadores, ronda inicial"""
        for j in self.jugadores:
            for i in range(2):
                j.setCarta(self.mazo.dar_carta())
                
    def checkPerdio(self,jugador):
        """ Chequea si el jugador perdio"""
        if jugador.perdio():
             self.turnoJugador = False
             
        
            
        





def main():
    juego = Blackjack()



    
    
    
    
if __name__ == '__main__':
    main()
           