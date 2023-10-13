import numpy as np
import matplotlib.pyplot as plt

# Definición de la matriz de probabilidades de transición (debes ajustar estas probabilidades según las reglas del juego)
# En este ejemplo, se utilizan valores de probabilidad aleatorios.
P = np.random.rand(40, 40)
P = P / P.sum(axis=1, keepdims=True)

# Inicialización de las probabilidades iniciales (comenzando en la casilla de "Salida")
P_0 = np.zeros(40)
P_0[0] = 1.0

# Número de lanzamientos de dos dados a considerar
n_lanzamientos = 1

# Iteración para simular los lanzamientos de dos dados y actualizar las probabilidades
P_t = P_0
for j in range(n_lanzamientos):
    # Simular los resultados de los dos dados (cada dado tiene 6 caras)
    resultado_dado1 = np.random.randint(1, 6)
    resultado_dado2 = np.random.randint(1, 6)
    suma_resultados = resultado_dado1 + resultado_dado2

    # Actualizar las probabilidades basadas en la matriz de transición
    P_t = np.dot(P_t, P)
    P_t = P_t / P_t.sum()  # Normalización

# Visualización de la PMF teórica
casillas = range(40)
plt.bar(casillas, P_t)
plt.title(f'PMF Después de {n_lanzamientos} Lanzamientos de Dos Dados (Simulados)')
plt.xlabel('Casilla')
plt.ylabel('Probabilidad')
plt.show()