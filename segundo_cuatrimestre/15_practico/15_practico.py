from dataclasses import dataclass
import random

@dataclass
class Carta:
    palo:str
    valor:str

    def puntajeCarta(self):
        """ Retorna el valor de la carta"""
        if self.valor in ['J', 'Q','K']:
            return 10
        if self.valor in (2, 3, 4, 5, 6, 7, 8, 9, 10):
            return self.valor  
        if self.palo == 'A':
            return 1




@dataclass
class Mazo:
    cartas = []
    palos = ("Pique", "Corazón", "Diamante", "Trébol")
    valores = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")

    def llenar_mazo(self):
        """ Llena el maso"""
        mazo = [Carta(p,v) for p in self.palos for v in self.valores]
        return mazo


@dataclass 
class Jugador:
    cartas = []

    def getCartas(self):
        """ Retorna las cartas del jugador"""
        return self.cartas

    def setCarta(self,carta:Carta):
        """ Agrega carta al jugador"""
        self.cartas.append(carta)

    def calcularMano(self):
        total = 0
        for c in self.cartas:
            print(c)
            total += c.puntajeCarta()
        return total
            

@dataclass
class Dealer(Jugador):
    mazo = Mazo()
    mazo = mazo.llenar_mazo()

    def repartirCartasIniciales(self, jugador:Jugador):
        """ Reparte dos cartas iniciales a cada jugador"""
        random.shuffle(self.mazo) # "Mezclo", cartas        
        self.setCarta(self.mazo.pop())
        self.setCarta(self.mazo.pop())
        jugador.setCarta(self.mazo.pop())
        jugador.setCarta(self.mazo.pop())
        print('Cartas iniciales cargadas')

    def darCarta(self, jugador:Jugador):
            cartaJugador = random.choice(self.mazo) # cartas iniciales jugador
            jugador.setCarta(cartaJugador)
            self.mazo.remove(cartaJugador)



@dataclass
class Blackjack:
    pass




def main():
    diler = Dealer()
    tobias = Jugador()
    diler.repartirCartasIniciales(tobias)
    print(tobias.getCartas())
    print(diler.getCartas())
    
if __name__ == '__main__':
    main()
           