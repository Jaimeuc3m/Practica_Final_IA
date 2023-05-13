import csv
import pandas as pd
import numpy as np

acciones = ['encender', 'apagar']
num_acciones = len(acciones)
max_iteraciones = 5000
iteraciones = 0
tolerancia = 1e-5
convergencia = False
meta = 22

df = pd.read_csv('TPC.csv')
coste_encender = df.iloc[0, 0]
coste_apagar = df.iloc[0, 1]
prob_encender = df.iloc[1:20, :]
prob_apagar = df.iloc[21:, :]
num_estados= prob_encender.shape[0]
V = np.zeros(num_estados)

while iteraciones < max_iteraciones:
    V_anterior = V.copy()
    valor_max = -np.inf
    for i in range(num_estados):
        sumatorio = np.sum(np.dot(prob_encender, V_anterior))
        valor = coste_encender + sumatorio
        print(sumatorio)
        if valor > valor_max:
                valor_max = valor
        V[i] = valor_max

    difference = np.abs(V - V_anterior)

    if max(difference) < tolerancia:
        convergencia = True
        break
    iteraciones += 1
print("Valores de la función de valor V:", V)
print(iteraciones)

"""
while iteraciones < max_iteraciones:
    V_anterior = V.copy()
    valor_max = -np.inf
    for i in range(num_estados_filas):
        valor = coste_encender + np.sum(np.dot(prob_encender, V_anterior))

        if valor > valor_max:
                valor_max = valor
        V[i] = valor_max

        difference = [abs(V[i] - V_anterior[i]) for i in range(len(V))]

        if max(difference) < tolerancia:
            convergencia = True
            break
        iteraciones += 1
print("Valores de la función de valor V:", V)
print(iteraciones)
"""