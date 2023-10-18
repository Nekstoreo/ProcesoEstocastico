import random
import matplotlib.pyplot as plt
import Monopoly

# Inicializamos el tablero y un jugador
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
casillas_visitadas = []  # Lista para rastrear las casillas visitadas

while not jugador.encarcelado:
    casilla_actual = jugador.posicion_actual.nombre
    casillas_visitadas.append(casilla_actual)  # Registra la casilla actual
    jugador.mover()
    print(jugador)

# Crear un gráfico para mostrar el recorrido del jugador
plt.figure(figsize=(12, 6))
plt.plot(casillas_visitadas, marker='o')
plt.xlabel("Turnos")
plt.ylabel("Casilla del Monopoly")
plt.title("Recorrido del jugador en el Monopoly")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
