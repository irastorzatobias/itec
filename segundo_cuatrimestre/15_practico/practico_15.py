from dataclasses import dataclass
import random
from os import system
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
        
    def cargar_mazo(self):
        """ Carga mazo con todas las cartas y ya lo mezcla por defecto"""
        self.cartas = [Carta(p,v) for p in self.palos for v in self.valores]
        self.shuffle()
        
    

class Jugador:
    def __init__(self):
        self.mano = []
        self.puntos = 0
    
    
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
        for i in range(self.aces()):
            if self.puntos < 12:
                self.puntos += 10 # sumo 10 porque anteriormente ya le sume 1 si es que habia una A
        return self.puntos
    
    def setCarta(self, carta):
        self.mano.append(carta)
    
    def perdio(self):
        return self.puntaje_con_ases() > 21
            

class Dealer(Jugador):
    # si no inicializo mano nuevamente, se me repite el append, desconozco el motivo
    def __init__(self):
        super().__init__()
        self.mano = []
    
    # Redefino el metodo mostrar mano
    def mostrar_mano(self,mostrar=False):
        """ Muestra la mano, en caso de que mostrar sea falso, muestra solo una carta, caso contrario, muestra ambas cartas"""
        if mostrar: 
            for c in self.mano:
                print(c)
        else:
            print(self.mano[0])
            print('???')
    





class Blackjack:
    def __init__(self):  
        self.mazo = []
        self.jugadores = [Jugador(), Dealer()]
        self.turnoJugador = True
        
    def mostrarJugadores(self):
        """ Muestra los jugadores """
        print(f'Cantidad de jugadores: {len(self.jugadores)}')
        for i,j in enumerate(self.jugadores):
            print(f' {i} - {type(j).__name__}')
    
    def repartir_cartas(self):
        """ Reparte 2 cartas para cada uno de los jugadores, ronda inicial"""
        for i in range(2):
            for j in self.jugadores:
                card = self.mazo.cartas.pop()
                j.mano.append(card)
                 

                
    def checkPerdio(self, jugador):
        if jugador.perdio():
            if isinstance(jugador, Jugador):
                self.turnoJugador = False
                print('\nJugador perdio')
            if isinstance(jugador, Dealer):
                print("\nDealer perdio!")        
        
    def hit(self, jugador):
        carta = self.mazo.cartas.pop()
        jugador.mano.append(carta)
        if isinstance(jugador, Dealer):
            print('Dealer: ')
            jugador.mostrar_mano(True)
        else:
            print('Jugador: ')
            jugador.mostrar_mano()
        self.checkPerdio(jugador)
        print(f"Puntaje de {type(jugador).__name__}: {jugador.puntaje_con_ases()}")
    
        
    def sigue(self, player):
        respuesta = input("Te quedas o pedis otra carta? (q/p -- q para quedarse, p para pedir): ")
        if respuesta.lower() == "p":
            self.hit(player)
        if respuesta.lower() == "q":
            print(f"Te quedas con {player.puntaje_con_ases()}\n")
            self.turnoJugador = False
    
    def comparar_puntaje(self, jugador, dealer):
        """ Compara los puntajes y en base a eso, lanza mensaje sobre quien gano o si hubo empate"""
        if jugador.puntaje_con_ases() > dealer.puntaje_con_ases():
            print('Jugador gano')
        if jugador.puntaje_con_ases() == dealer.puntaje_con_ases():
            print('Empate')
        if (jugador.puntaje_con_ases() < dealer.puntaje_con_ases()) and dealer.puntaje_con_ases() <= 21:
            print('Dealer gano!')


    
    def play(self):
        """ Determina un crupie, un jugador y comienza el juego, sin apuestas por el momento y solo de un jugador """
        self.mazo = Mazo()
        jugador1 = self.jugadores[0] 
        crupie = self.jugadores[1]
        jugando = True
        self.mazo.cargar_mazo()  
        self.repartir_cartas() 
        print('Mano crupie: ')
        crupie.mostrar_mano()
        print('Mano jugador: ')
        jugador1.mostrar_mano()
        print(f'Puntaje actual: {jugador1.puntaje_con_ases()}')
        while jugando:
            # Comienza el juego
            while self.turnoJugador:
                self.sigue(jugador1)
            if not jugador1.perdio():
                print('-- DEALER --')
                crupie.mostrar_mano(True)
                while not self.turnoJugador:
                    if crupie.puntaje_con_ases() < 17:
                        # Si crupie tiene menos de 17, juega
                        print('Juega dealer: ')
                        self.hit(crupie)
                    if crupie.puntaje_con_ases() >= 17 and not crupie.perdio():
                        # Si crupie tiene mas de 17 y no perdio, se queda ahi.
                        print(f'Puntaje final: {crupie.puntaje_con_ases()} ')
                        break
                    if crupie.perdio():
                        # Si crupie perdio, el jugador gana
                        print('Jugador gana')
                        break 
                if not crupie.perdio():
                    # Si luego de lo anterior, el crupie no perdio, se comparan los puntajes
                    self.comparar_puntaje(jugador1, crupie)
            jugando = False # Se deja de
    
    
                    
    
def main():
    juego = Blackjack()
    juego.play()



    


    
    
    
    
if __name__ == '__main__':
    main()