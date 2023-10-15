import random

import numpy as np


class Casilla:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None

    def __str__(self):
        return f"Casilla: {self.nombre} Siguiente: {self.siguiente.nombre}"


class Tablero:
    def __init__(self):
        self.nombrecasillas = [
            "Salida", "Avenida Mediterraneo", "Avenida Baltico", "Impuesto sobre la renta", "Ferrocarril de Reading",
            "Avenida Oriental", "Avenida Vermont", "Avenida Connecticut", "Plaza San Carlos",
            "Compania de electricidad", "Avenida States", "Avenida Virginia", "Ferrocarril de Pennsylvania",
            "Plaza St. James", "Avenida Tennessee", "Avenida New York", "Parking gratuito", "Avenida Kentucky",
            "Avenida Indiana", "Avenida Illinois", "Ferrocarril B. & O.", "Avenida Atlantico", "Avenida Ventnor",
            "Compania de agua", "Jardines Marvin", "Ve a la Carcel", "Avenida Pacifico", "Avenida Carolina del Norte",
            "Avenida Pensilvania", "Ferrocarril de Short Line", "Plaza Park", "Impuesto sobre lujo", "El Muelle"
        ]
        self.casillas = self.asignar_casillas()

    def asignar_casillas(self) -> list:
        casillas = [Casilla(nombre) for nombre in self.nombrecasillas]
        # Establecer los enlaces para crear una lista enlazada circular
        for i in range(len(casillas)):
            casillas[i].siguiente = casillas[(i + 1) % len(casillas)]
        return casillas


class Jugador:
    def __init__(self, nombre, tablero):
        self.nombre = nombre
        self.tablero = tablero
        self.posicion_actual = tablero.casillas[0]
        self.encarcelado = False

    @staticmethod
    def lanzar_dados():
        return random.randint(1, 6), random.randint(1, 6)

    def mover(self):
        if not self.encarcelado:
            dado1, dado2 = self.lanzar_dados()
            suma_dados = dado1 + dado2
            # Avanzar el jugador
            for _ in range(suma_dados):
                self.posicion_actual = self.posicion_actual.siguiente
            # Comprobar si the jugador cayó en "Ve a la Carcel"
            if self.posicion_actual.nombre == "Ve a la Carcel":
                self.encarcelado = True
            print(f"Avanza {suma_dados} casillas")
        else:
            return "El jugador está encarcelado"


    def __str__(self):
        return f"{self.nombre} en la casilla {self.posicion_actual.nombre}"


class Markov:
    def __init__(self):
        self.nombrecasillas = [
            "Salida", "Avenida Mediterraneo", "Avenida Baltico", "Impuesto sobre la renta", "Ferrocarril de Reading",
            "Avenida Oriental", "Avenida Vermont", "Avenida Connecticut", "Plaza San Carlos",
            "Compania de electricidad", "Avenida States", "Avenida Virginia", "Ferrocarril de Pennsylvania",
            "Plaza St. James", "Avenida Tennessee", "Avenida New York", "Parking gratuito", "Avenida Kentucky",
            "Avenida Indiana", "Avenida Illinois", "Ferrocarril B. & O.", "Avenida Atlantico", "Avenida Ventnor",
            "Compania de agua", "Jardines Marvin", "Ve a la Carcel", "Avenida Pacifico", "Avenida Carolina del Norte",
            "Avenida Pensilvania", "Ferrocarril de Short Line", "Plaza Park", "Impuesto sobre lujo", "El Muelle"
        ]
        self.prob_transicion = self.asignar_probabilidades_transicion()

    def asignar_probabilidades_transicion(self) -> np.ndarray:
        matriz = np.zeros((len(self.nombrecasillas), len(self.nombrecasillas)))
        prob_dados = Markov.calc_prob_dados()
        for i in range(len(self.nombrecasillas)):
            for j in range(2, 13):
                if i + j < len(self.nombrecasillas):
                    matriz[i, i + j] = prob_dados[j - 2]
        matriz[self.nombrecasillas.index("Ve a la Carcel"), :] = 0
        return matriz

    @staticmethod
    def calc_prob_dados() -> list:
        probabilidades = [0] * 11
        # Contador para llevar un registro del total de combinaciones posibles
        total_combinaciones = 0
        # Itera a través de todos los posibles resultados de lanzar dos dados
        for dado1 in range(1, 7):
            for dado2 in range(1, 7):
                suma = dado1 + dado2
                probabilidades[suma - 2] += 1
                total_combinaciones += 1
        # Calcula la probabilidad de obtener cada suma y redondea a 3 decimales
        for i in range(11):
            probabilidades[i] = round(probabilidades[i] / total_combinaciones, 3)
        return probabilidades
