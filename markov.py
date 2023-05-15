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

datos = pd.read_csv('TPC.csv')

# Extraer los valores de costos y probabilidades
coste_enc = datos.iloc[0, 0]
coste_ap = datos.iloc[0, 1]
probabilidades_encendido = datos.iloc[1:20, :].values
probabilidades_apagado = datos.iloc[20:, :].values
estados = np.arange(16, 25.5, 0.5)
# Definir la temperatura deseada por el usuario
meta = 22

# Obtener el número de estados y acciones
num_estados = probabilidades_encendido.shape[0]

solver_enc = Markov(probabilidades_encendido, coste_enc, meta, estados)
solver_ap = Markov(probabilidades_apagado, coste_ap, meta, estados)

V_enc = solver_enc.bellman()
V_ap = solver_ap.bellman()

politica_optima = solver_enc.politica_optima(V_enc, V_ap)
print("Política óptima:")
print(politica_optima)

