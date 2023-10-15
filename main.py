import Monopoly

# inicializamos el tablero, y un jugador
tablero = Monopoly.Tablero()


# Define a function to print the game board
def print_monopoly_board(tablero):
    board = [casilla.nombre for casilla in tablero.casillas]
    board_size = len(board)

    for i in range(board_size):
        square = board[i]
        if i % 5 == 0:
            print("\n" + "=" * 120)
        print(f"| {square.center(20)} ", end="")

    print("\n" + "=" * 70)


# Print the game board
print_monopoly_board(tablero)

jugador = Monopoly.Jugador("Jugador 1", tablero)

# Empezamos a jugar
casillasvisitadas = 0
while not jugador.encarcelado:
    jugador.mover()
    print(jugador)
    casillasvisitadas += 1
print(f"El jugador ha sido encarcelado después de visitar {casillasvisitadas} casillas")
