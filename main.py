import numpy as np

# Definimos el espacio muestral
espacio_muestral = [
    "Salida", "Avenida Mediterraneo", "Arca Comunal", "Avenida Baltico",
    "Impuesto sobre la renta", "Ferrocarril de Reading", "Avenida Oriental", "Suerte",
    "Avenida Vermont", "Avenida Connecticut", "Carcel", "Plaza San Carlos",
    "Compania de electricidad", "Avenida States", "Avenida Virginia", "Ferrocarril de Pennsylvania",
    "Plaza St. James", "Arca Comunal", "Avenida Tennessee", "Avenida New York",
    "Parking gratuito", "Avenida Kentucky", "Suerte", "Avenida Indiana",
    "Avenida Illinois", "Ferrocarril B. & O.", "Avenida Atlantico", "Avenida Ventnor",
    "Compania de agua", "Jardines Marvin", "Ve a la carcel", "Avenida Pacifico",
    "Avenida Carolina del Norte", "Arca Comunal", "Avenida Pensilvania",
    "Ferrocarril de Short Line", "Suerte", "Plaza Park", "Impuesto sobre lujo", "El Muelle"
]

# Definimos las probabilidades de transición
probabilidades_transicion = np.zeros((len(espacio_muestral), len(espacio_muestral)))

# Propiedades, salida, impuestos y parking
for i in range(0, len(espacio_muestral)):
    if (
            espacio_muestral[i].startswith("Avenida")
            or espacio_muestral[i].startswith("Plaza")
            or espacio_muestral[i].startswith("Jardines")
            or espacio_muestral[i] == "El Muelle"
            or espacio_muestral[i].startswith("Ferrocarril")
            or espacio_muestral[i].startswith("Compania")
            or espacio_muestral[i] == "Salida"
            or espacio_muestral[i].startswith("Impuesto")
            or espacio_muestral[i] == "Parking gratuito"):
        for j in range(i + 1, i + 13):
            if j < len(espacio_muestral):
                probabilidades_transicion[i, j] = round(1 / 12, 3)
    # Ve a la carcel
    if espacio_muestral[i] == "Ve a la carcel":
        probabilidades_transicion[i, 10] = 1
    # Carcel
    if espacio_muestral[i] == "Carcel":
        probabilidades_transicion[i, 10] = 1

    # Suerte(16 cartas)
    if espacio_muestral[i] == "Suerte":
        # Retrocede 3 casillas
        probabilidades_transicion[i, i - 3] = round(1 / 16, 3)
        # Ir a la carcel
        probabilidades_transicion[i, 10] = round(1 / 16, 3)
        # Ir a la salida
        probabilidades_transicion[i, 0] = round(1 / 16, 3)
        # Ir a la Avenida Illinois
        probabilidades_transicion[i, 24] = round(1 / 16, 3)
        # Ir a la Plaza San Carlos
        probabilidades_transicion[i, 11] = round(1 / 16, 3)
        # Ir a la Plaza Park
        probabilidades_transicion[i, 34] = round(1 / 16, 3)
        # Ir al Ferrocarril de Reading
        probabilidades_transicion[i, 5] = round(1 / 16, 3)
        # Ir al ferrocarril o utilidad mas cercano:
        if i == 7:
            # Ferrocarril de Pennsylvania
            probabilidades_transicion[i, 15] = round(1 / 16, 3)
            # Compania de electricidad
            probabilidades_transicion[i, 12] = round(1 / 16, 3)
        elif i == 22:
            # Ferrocarril B. & O.
            probabilidades_transicion[i, 25] = round(1 / 16, 3)
            # Compania de agua
            probabilidades_transicion[i, 28] = round(1 / 16, 3)
        elif i == 36:
            # Ferrocarril de Short Line
            probabilidades_transicion[i, 5] = round(1 / 16, 3)
            # Compania de electricidad
            probabilidades_transicion[i, 12] = round(1 / 16, 3)
# Arca comunal(16 cartas)
for i in range(0, len(espacio_muestral)):
    if espacio_muestral[i] == "Arca Comunal":
        # Ir a la carcel o a la salida
        probabilidades_transicion[i, 10] = round(1 / 16, 3)
        probabilidades_transicion[i, 0] = round(1 / 16, 3)


# imprimimos la matriz de probabilidades de transición

def imprimir_matriz(matriz):
    for fil in matriz:
        for e in fil:
            print(e, end=" ")
        print()


imprimir_matriz(probabilidades_transicion)

# Definimos la matriz de probabilidades de estado inicial
probabilidades_estado_inicial = np.zeros((1, len(espacio_muestral)))
probabilidades_estado_inicial[0, 0] = 1

# TODO: multiplicamos la matriz de probabilidades de estado inicial por la matriz de probabilidades de transición con n lanzamientos
