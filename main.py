import random
import matplotlib.pyplot as plt
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


# Función para simular múltiples partidas y registrar las casillas visitadas
def simular_partidas(n_partidas):
    casillas_visitadas = {}  # Diccionario para registrar las casillas visitadas

    for _ in range(n_partidas):
        tablero = Monopoly.Tablero()
        jugador = Monopoly.Jugador("Jugador 1", tablero)

        while not jugador.encarcelado:
            jugador.mover()
            casilla_actual = jugador.posicion_actual.nombre

            # Registra la casilla visitada
            if casilla_actual in casillas_visitadas:
                casillas_visitadas[casilla_actual] += 1
            else:
                casillas_visitadas[casilla_actual] = 1

    return casillas_visitadas

# Simula 1000 partidas (puedes ajustar este número)
resultados = simular_partidas(1000)

# Graficar los resultados
casillas = list(resultados.keys())
frecuencias = list(resultados.values())

plt.figure(figsize=(12, 6))
plt.bar(casillas, frecuencias)
plt.xlabel("Casillas del Monopoly")
plt.ylabel("Frecuencia de visitas")
plt.title("Frecuencia de visitas a casillas del Monopoly")
plt.xticks(rotation=90)  # Rota las etiquetas del eje x para facilitar la lectura
plt.tight_layout()
plt.show()