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
estados = np.arange(16, 25, 0.5)
num_estados = len(estados)

df = pd.read_csv('TPC.csv')

coste_encender = df.iloc[0, 1].values.tolist()
coste_apagar = df.iloc[0, 2].values.tolist()
prob_encender = df.iloc[1:, :].values.tolist()
prob_apagar = df.iloc[21:, :].values.tolist()
"""
V = np.zeros(num_estados)
pron = np.zeros((num_acciones, num_estados, num_estados))
recompensas = np.zeros(num_estados)

while iteraciones < max_iteraciones:
    V_anterior = V.copy()
    for i in range(len(costes)):
        coste = costes.iloc[i]
        valor_max = float('-inf')

        for j in range(len(prob.columns)):
            valor = coste + prob.iloc[i, j] * V_anterior[j]

            if (valor > valor_max).all():
                valor_max = valor

        V[i] = valor_max

    difference = [abs(V[i] - V_anterior[i]) for i in range(len(V)) if prob.iloc[i].any() != 0]

    if max(difference) < tolerancia:
        convergencia = True
        break
    iteraciones += 1
print("Valores de la función de valor V:", V)
print(convergencia)
"""