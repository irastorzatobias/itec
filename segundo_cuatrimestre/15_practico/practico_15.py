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
    jugadores = [Jugador(), Dealer(), Jugador()]
    turnoJugador = True
    jugando = True
    
    def mostrarJugadores(self):
        """ Muestra los jugadores """
        print(f'Cantidad de jugadores: {len(self.jugadores)}')
        for i,j in enumerate(self.jugadores):
            print(f' {i} - {type(j).__name__}')
    
    def repartir_cartas(self):
        """ Reparte 2 cartas para cada uno de los jugadores, ronda inicial"""
        self.mazo.cargar_mazo()
        for i in range(2):
            for j in self.jugadores:
                self.hit(j)
                
    def checkPerdio(self,jugador):
        """ Chequea si el jugador perdio"""
        if jugador.perdio():
             self.turnoJugador = False
             print('Jugador perdio')
        else:
            print('Jugador no perdio')
    

    def hit(self, jugador):
        carta = self.mazo.cartas.pop()
        jugador.mano.append(carta)             
        
    def sigue(self, player):
        respuesta = input("Hit or Stick? H/S: ")
        if respuesta.lower() == "h":
            self.hit(player)
        if respuesta.lower() == "s":
            print(f"Te quedas con {player.puntaje_con_ases()}\n")
            self.turnoJugador = False
    

    
    def play(self):
        """ Determina un crupie, un jugador y comienza el juego, sin apuestas por el momento y solo de un jugador """
        jugador1 = self.jugadores[0] # si pongo mas de un jugador tengo error, se me suman las cartas a todos los jugadores.
        crupie = self.jugadores[1] # en este caso como jugadores[1] es crupie, no me pasa lo mismo, es clase diferente. 
        jugador2 = self.jugadores[2]
        self.repartir_cartas()
        print('Mano jugador 1: ')
        jugador1.mostrar_mano()    
        print('Mano jugador 2: ')
        jugador2.mostrar_mano()
        print('Mano crupie')       
        crupie.mostrar_mano()
        while self.jugando:
            print(f'Su puntaje es de {jugador1.puntaje_con_ases()}')
            c = self.sigue(jugador1)
            if self.checkPerdio(jugador1):
                jugador1.mostrar_mano()
                print(f'Puntaje: {jugador1.puntaje_con_ases()}')
                self.turnoJugador = False
                break
            else:
                print(f'Se quedo con: {jugador1.puntaje_con_ases()}')
                
            






def main():
    juego = Blackjack()
    juego.play()
    

    


    
    
    
    
if __name__ == '__main__':
    main()