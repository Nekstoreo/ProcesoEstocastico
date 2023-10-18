import random
import tkinter as tk
from tkinter import Entry, Button, Label
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import Monopoly


# Función para simular la trayectoria de un jugador hasta que sea encarcelado
def simular_trayectoria():
    tablero = Monopoly.Tablero()
    jugador = Monopoly.Jugador("Jugador 1", tablero)
    trayectoria = []

    while not jugador.encarcelado:
        jugador.mover()
        casilla_actual = jugador.posicion_actual.nombre
        trayectoria.append(casilla_actual)

    return trayectoria

# Función para simular múltiples partidas y registrar las casillas visitadas


def simular_partidas():
    n_partidas = int(entry_partidas.get())
    casillas_visitadas = {}  # Diccionario para registrar las casillas visitadas

    for i in range(n_partidas):
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

# Función para graficar la trayectoria hasta que el jugador sea encarcelado


def graficar_trayectoria():
    trayectoria = simular_trayectoria()

    # Limpiar el área del gráfico anterior (si existe)
    for widget in frame.winfo_children():
        widget.destroy()

    # Crear el gráfico de la trayectoria
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(range(1, len(trayectoria) + 1),
            [casillas.index(casilla) for casilla in trayectoria], marker='o')
    ax.set_xlabel("Número de lanzamientos")
    ax.set_ylabel("Casilla visitada")
    ax.set_title("Trayectoria del jugador hasta encarcelamiento")
    ax.set_xticks(range(1, len(trayectoria) + 1))
    ax.set_yticks(range(len(casillas)))
    ax.set_xticklabels(range(1, len(trayectoria) + 1))
    ax.set_yticklabels(casillas)
    plt.xticks(rotation=45)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack()
    canvas.draw()

# Función para graficar las visitas a casillas


def graficar_visitas_casillas():
    n_partidas = int(entry_partidas.get())
    resultados = simular_partidas()

    # Limpiar el área del gráfico anterior (si existe)
    for widget in frame.winfo_children():
        widget.destroy()

    casillas = list(resultados.keys())
    frecuencias = list(resultados.values())

    # Crear el gráfico de visitas a casillas
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(casillas, frecuencias)
    ax.set_xlabel("Casillas del Monopoly")
    ax.set_ylabel("Frecuencia de visitas")
    ax.set_title("Frecuencia de visitas a casillas del Monopoly")
    ax.set_xticklabels(ax.get_xticks(), rotation=45)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack()
    canvas.draw()

# Función para mostrar el campo de entrada para el número de partidas


def mostrar_campo():
    entry_partidas.pack()

# Función para ocultar el campo de entrada para el número de partidas


def ocultar_campo():
    entry_partidas.pack_forget()


# Función para simular múltiples partidas y registrar los números de turnos en que terminan
def simular_turnos_partidas(n_partidas):
    turnos_terminacion = []  # Lista para registrar los turnos de terminación

    for _ in range(n_partidas):
        tablero = Monopoly.Tablero()
        jugador = Monopoly.Jugador("Jugador 1", tablero)

        turnos = 0
        while not jugador.encarcelado:
            jugador.mover()
            turnos += 1

        turnos_terminacion.append(turnos)

    return turnos_terminacion

# Función para graficar los números de turnos en los que terminan las partidas


def graficar_turnos_partidas():
    n_partidas = int(entry_partidas.get())
    if n_partidas <= 0:
        return  # Evitar divisiones por cero si no se ingresan partidas

    turnos_terminacion = simular_turnos_partidas(n_partidas)

    # Limpiar el área del gráfico anterior (si existe)
    for widget in frame.winfo_children():
        widget.destroy()

    # Crear el gráfico de barras
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.hist(turnos_terminacion, bins=range(
        1, max(turnos_terminacion) + 2), rwidth=0.8, align='left')
    ax.set_xlabel("Número de turnos")
    ax.set_ylabel("Frecuencia de partidas")
    ax.set_title("Números de turnos en los que terminan las partidas")
    ax.set_xticks(range(1, max(turnos_terminacion) + 1))
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack()
    canvas.draw()

# Función para limpiar el campo de entrada cuando se hace clic en él


def limpiar_campo(event):
    default_value = "Ingrese el número de partidas"
    if entry_partidas.get() == default_value:
        entry_partidas.delete(0, "end")
        entry_partidas.config(fg="black")


# Crear la ventana de tkinter
root = tk.Tk()
root.title("Proceso Estocástico: Monopoly")
root.iconbitmap("Monopoly.ico")
root.geometry("1280x720")
root.resizable(0,0)


# Etiqueta y campo de entrada para el número de partidas
label_autores = Label(
    root, text="Autores:\nJonhson Chen Yu\nNestor Miguel Gutierrez Arias\nSimón Tamara Gómez")
label_autores.pack()
label_autores.place(x=1, y=1)

label_partidas = Label(root, text="Número de partidas:")
label_partidas.pack()
label_partidas.place(x=591, y=20)

entry_partidas = Entry(root)
entry_partidas.pack()
entry_partidas.place(x=586, y=50)

# Botones para iniciar la simulación
button_trayectoria = ttk.Button(
    root, text="Simular Trayectoria", command=graficar_trayectoria)
button_partidas = ttk.Button(
    root, text="Simular Partidas", command=graficar_visitas_casillas)
button_turnos = ttk.Button(root, text="Simular Turnos",
                           command=graficar_turnos_partidas)
button_partidas.pack()
button_trayectoria.pack(side="left")
button_turnos.pack(side="right")
button_partidas.place(x=600, y=97)
button_trayectoria.place(x=450, y=97)
button_turnos.place(x=735, y=97)



# Frame para mostrar el gráfico
frame = tk.Frame(root)
frame.pack(side="bottom")




# Obtén la lista de casillas del tablero
casillas = [casilla.nombre for casilla in Monopoly.Tablero().casillas]

# Iniciar el bucle principal de tkinter
root.mainloop()
