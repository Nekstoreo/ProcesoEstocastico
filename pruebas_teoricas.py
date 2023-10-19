import Monopoly as mp
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import Frame
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def castToProb(dicc, n_partidas):
    for key in dicc:
        if dicc[key] != 0:
            dicc[key] = dicc[key] / n_partidas
    return dicc


def simular_partidas(n_partidas):
    tablero = mp.Tablero()
    casillas_visitadas = {}
    for casilla in tablero.casillas:
        casillas_visitadas[casilla.nombre] = 0

    for i in range(n_partidas):
        jugador = mp.Jugador("Jugador", tablero)
        jugador.mover()
        casilla_actual = jugador.posicion_actual.nombre
        casillas_visitadas[casilla_actual] += 1

    return castToProb(casillas_visitadas, n_partidas)


def obtener_values_casillas_visitadas(casillas_visitadas):
    values_casillas_visitadas = list(casillas_visitadas.values())
    return values_casillas_visitadas


def cutDicc(dicc, n):
    result = {}
    for i in range(n):
        result[list(dicc.keys())[i]] = list(dicc.values())[i]
    return result


def graficar_casillas_visitadas(casillas_visitadas):
    nombres_casillas = list(casillas_visitadas.keys())
    valores_casillas = list(casillas_visitadas.values())
    # Crear el frame para el gráfico
    frame = tk.Frame(window)
    frame.pack()
    # Limpiar el área del gráfico anterior (si existe)
    for widget in frame.winfo_children():
        widget.destroy()
    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(nombres_casillas, valores_casillas)
    ax.set_xlabel("Casillas del Monopoly")
    ax.set_ylabel("Frecuencia")
    ax.set_title("Visitas a las casillas en el Monopoly")
    ax.set_xticklabels(nombres_casillas, rotation=45)
    ax.set_yticklabels(valores_casillas)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack()
    canvas.draw()


def graficar_prob_dados():
    markov = mp.Markov()
    prob_dados = {i: markov.prob_dados[i] for i in range(13)}
    valor_dados = list(prob_dados.keys())
    prob_dados = list(prob_dados.values())
    # Crear el frame para el gráfico
    frame = tk.Frame(window)
    frame.pack()
    # Limpiar el área del gráfico anterior (si existe)
    for widget in frame.winfo_children():
        widget.destroy()
    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(valor_dados, prob_dados)
    ax.set_xlabel("Valor de los dados")
    ax.set_ylabel("Probabilidad")
    ax.set_title("Probabilidad de los valores de los dados")
    ax.set_xticklabels(valor_dados, rotation=90)
    ax.set_yticklabels(prob_dados)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack()
    canvas.draw()

# def graficar_casillas_visitadas(casillas_visitadas):
#    nombres_casillas = list(casillas_visitadas.keys())
#    valores_casillas = list(casillas_visitadas.values())
#
#    plt.figure(figsize=(10, 5))
#    plt.bar(nombres_casillas, valores_casillas)
#    plt.xlabel('Casillas')
#    plt.ylabel('Visitas')
#    plt.title('Visitas a las casillas en el Monopoly')
#    plt.xticks(rotation=90)
#    plt.show()
#
# def graficar_prob_dados(prob_dados):
#    valor_dados = list(prob_dados.keys())
#    prob_dados = list(prob_dados.values())
#    plt.figure(figsize=(10, 5))
#    plt.bar(valor_dados, prob_dados)
#    plt.xlabel('Suma de los dados')
#    plt.ylabel('Probabilidad')
#    plt.title('Probabilidad de la suma de los dados')
#    plt.xticks(rotation=90)
#    plt.show()


def gengrafcasillas():
    n_partidas = entry_n_partidas.get()
    if n_partidas:  # Verificar que n_partidas no esté vacío
        graficar_casillas_visitadas(
            cutDicc(simular_partidas(int(n_partidas)), 12))


# Create the Tkinter window
window = tk.Tk()
window.title("Monopoly Graphs")
# Create the label and entry widgets for n_partidas
label_n_partidas = tk.Label(window, text="Número de partidas:")
label_n_partidas.pack()
entry_n_partidas = tk.Entry(window)
entry_n_partidas.pack()
# Create the button to generate the graph
button_casillas_visitadas = tk.Button(
    window, text="Generar gráfico Casillas", command=gengrafcasillas)
button_casillas_visitadas.pack()
button_prob_dados = tk.Button(
    window, text="Generar gráfico Dados", command=graficar_prob_dados)
button_prob_dados.pack()
# Run the Tkinter event loop
window.mainloop()
