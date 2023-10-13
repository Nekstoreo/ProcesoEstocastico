import Monopoly


#inicializamos el tablero, y un jugador
tablero = Monopoly.Tablero()
jugador = Monopoly.Jugador("Jugador 1", tablero)

a=0
for i in tablero.casillas:
    print(f"{a}. {i}")
    a = a + 1





