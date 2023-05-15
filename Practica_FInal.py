import numpy as np
import pandas as pd

import random

class Markov:
    def __init__(self, tabla, coste, meta, estados, tolerancia = 0.00001, max_iteraciones=5000):
        self.tabla = tabla
        self.coste = coste
        self.meta = meta
        self.estados = estados
        self.tolerancia = tolerancia
        self.max_iteraciones = max_iteraciones

    def bellman(self):
        num_estados = self.tabla.shape[0]
        V = np.zeros(num_estados)
        convergencia = False
        iteraciones = 0

        while not convergencia and iteraciones < self.max_iteraciones:
            V_antiguo = V.copy()
            for i in range(num_estados):
                estado = self.estados[i]
                posible_valor = []
                sumatorio = 0
                if estado != self.meta:
                    for pos_des in range(num_estados):
                        if self.tabla[i][pos_des] != 0:
                            sumatorio += self.tabla[i][pos_des] * V_antiguo[pos_des]
                            posible_valor.append(self.coste + sumatorio)
                    V[i] = np.min(posible_valor)
                else:
                    V[i] = 0.0

            if np.linalg.norm(V - V_antiguo) < self.tolerancia:
                convergencia = True
            iteraciones += 1

        return V

    def politica_optima(self, V0, V1):
        politica_optima = []

        for i in range(len(self.estados)):
            estado = self.estados[i]
            if estado != self.meta:
                valor_encendido = V0[i]
                valor_apagado = V1[i]
                if valor_encendido <= valor_apagado:
                    politica_optima.append('Encender')
                else:
                    politica_optima.append('Apagar')
            else:
                politica_optima.append('Apagar')

        return politica_optima

class SimuladorCalefaccion:
    def __init__(self, politica_optima, temperatura_deseada, tiempo_maximo):
        self.politica_optima = politica_optima
        self.temperatura_deseada = temperatura_deseada
        self.temperatura_actual = 16
        self.tiempo_maximo = tiempo_maximo

    def ejecutar_simulacion(self):
        print("Temperatura inicial:", self.temperatura_actual)
        print("Temperatura deseada:", self.temperatura_deseada)
        #self.temperatura_actual != self.temperatura_deseada
        tiempo = 0
        while tiempo <= self.tiempo_maximo:
            accion = self.politica_optima[int((self.temperatura_actual - 16) * 2)]
            print("Tiempo:", tiempo, "- Acción:", accion, "- Temperatura actual:", self.temperatura_actual)
            if accion == 'Encender':
                self.temperatura_actual += random.choice([-0.5, 0, 0.5, 1])
            else:
                self.temperatura_actual += random.choice([-0.5, 0, 0.5])

            self.temperatura_actual = max(min(self.temperatura_actual, 25), 16)  # Aplicar límites
            self.temperatura_actual = round(self.temperatura_actual, 1)  # Redondear a una decimal

            tiempo += 0.5
        if self.temperatura_actual == self.temperatura_deseada:
            print("Simulación finalizada. Temperatura alcanzada:", self.temperatura_actual)
        else:
            print("Tiempo máximo alcanzado. Temperatura actual:", self.temperatura_actual)


def main():
    datos = pd.read_csv('TPC.csv')

    # Extraer los valores de costos y probabilidades
    coste_enc = datos.iloc[0, 0]
    coste_ap = datos.iloc[0, 1]
    probabilidades_encendido = datos.iloc[1:20, :].values
    probabilidades_apagado = datos.iloc[20:, :].values
    estados = np.arange(16, 25.5, 0.5)

    # Definir la temperatura deseada por el usuario
    temperatura_deseada = 22
    tiempo_maximo = 16

    # Crear el objeto Markov y calcular la política óptima
    solver_enc = Markov(probabilidades_encendido, coste_enc, temperatura_deseada, estados)
    solver_ap = Markov(probabilidades_apagado, coste_ap, temperatura_deseada, estados)

    V_enc = solver_enc.bellman()
    V_ap = solver_ap.bellman()

    politica_optima = solver_enc.politica_optima(V_enc, V_ap)

    # Crear el simulador de calefacción y ejecutar la simulación
    simulador = SimuladorCalefaccion(politica_optima, temperatura_deseada, tiempo_maximo)
    simulador.ejecutar_simulacion()

if __name__ == '__main__':
    main()