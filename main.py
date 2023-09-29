import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Crear la ventana principal
window = tk.Tk()
window.title("Simulación de Proceso de Markov")

# Agregar elementos de la interfaz, como etiquetas y cuadros de texto
label1 = tk.Label(window, text="Número de estados:")
entry1 = tk.Entry(window)
label2 = tk.Label(window, text="Probabilidades de transición:")
entry2 = tk.Entry(window)

# Agregar un botón para iniciar la simulación
button = tk.Button(window, text="Simular")

# Agregar un área de gráficos
fig, ax = plt.subplots(figsize=(6, 4))
canvas = FigureCanvasTkAgg(fig, master=window)
canvas_widget = canvas.get_tk_widget()

# Colocar los elementos en la ventana
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
button.pack()
canvas_widget.pack()


# Función para manejar el clic del botón y realizar la simulación
def simulate():
    num_states = int(entry1.get())
    transition_probs = [float(prob) for prob in entry2.get().split(",")]

    # Realizar la simulación y generar gráficos
    # (Reemplaza esto con tu lógica de simulación y gráficos)
    days = np.arange(1, 31)
    temperature = np.random.randint(50, 100, size=30)

    ax.clear()
    ax.plot(days, temperature)
    ax.set_xlabel("Día")
    ax.set_ylabel("Temperatura")
    ax.set_title("Simulación de Temperatura")
    canvas.draw()


button.config(command=simulate)

# Iniciar el bucle de la interfaz
window.mainloop()

