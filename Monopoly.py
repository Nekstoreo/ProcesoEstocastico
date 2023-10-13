import random

import numpy as np


class Dado:
    @staticmethod
    def calcular_probabilidad() -> list:
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

        self.prob_transicion = np.zeros((len(self.nombrecasillas), len(self.nombrecasillas)))

        # Crear instancias de Casilla y establecer enlaces
        self.casillas = [Casilla(nombre) for nombre in self.nombrecasillas]

        # Establecer los enlaces para crear una lista enlazada circular
        for i in range(len(self.casillas)):
            self.casillas[i].siguiente = self.casillas[(i + 1) % len(self.casillas)]



    def asignar_probabilidades_transicion(self):
        prob_dados = Dado.calcular_probabilidad()
        for i in range(len(self.nombrecasillas)):
            for j in range(2, 13):
                if i + j < len(self.nombrecasillas):
                    self.prob_transicion[i, i + j] = prob_dados[j - 2]
        self.prob_transicion[self.nombrecasillas.index("Ve a la Carcel"), :] = 0


class Jugador:
    def __init__(self, nombre, tablero):
        self.nombre = nombre
        self.tablero = tablero
        self.posicion_actual = tablero.nombrecasillas[0]
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

            # Comprobar si el jugador cayó en "Ve a la Carcel"
            if self.posicion_actual.nombre == "Ve a la Carcel":
                self.encarcelado = True
                return

    def __str__(self):
        return f"Jugador: {self.nombre}, Posición: {self.posicion_actual.nombre}"
