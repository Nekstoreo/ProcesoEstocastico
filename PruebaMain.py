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
visitas_por_casilla = {}  # Diccionario para rastrear las visitas a cada casilla

while not jugador.encarcelado:
    casilla_actual = jugador.posicion_actual.nombre
    casillas_visitadas.append(casilla_actual)  # Registra la casilla actual

    # Registra la visita a la casilla en el diccionario
    if casilla_actual in visitas_por_casilla:
        visitas_por_casilla[casilla_actual] += 1
    else:
        visitas_por_casilla[casilla_actual] = 1

    jugador.mover()
    print(jugador)

# Imprime el número total de visitas a cada casilla
for casilla, visitas in visitas_por_casilla.items():
    print(f"El jugador visitó la casilla {casilla} {visitas} veces")

# Crear un gráfico para mostrar el recorrido del jugador
plt.figure(figsize=(12, 6))
plt.plot(casillas_visitadas, marker='o')
plt.xlabel("Turnos")
plt.ylabel("Casilla del Monopoly")
plt.title("Recorrido del jugador en el Monopoly")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Crear un gráfico de barras para mostrar las visitas a cada casilla
casillas = list(visitas_por_casilla.keys())
visitas = list(visitas_por_casilla.values())

plt.figure(figsize=(12, 6))
plt.bar(casillas, visitas)
plt.xlabel("Casillas del Monopoly")
plt.ylabel("Número de Visitas")
plt.title("Número de Visitas a Cada Casilla en el Monopoly")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
