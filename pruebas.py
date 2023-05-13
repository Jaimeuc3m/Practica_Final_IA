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
num_estados, num_columnas = df.shape
coste_encender = df.iloc[0, 0]
coste_apagar = df.iloc[0, 1]
prob_encender = df.iloc[1:20, :]
num_filas, num_columnas = prob_encender.shape
prob_apagar = df.iloc[21:, :]

print(num_filas, num_columnas)
V = np.zeros(num_estados)
recompensas = np.zeros(num_estados)
"""
while iteraciones < max_iteraciones:
    V_anterior = V.copy()
    for i in range(num_estados):
        valor_max = float('-inf')

        for j in range(num_acciones):
            if acciones[j] == 'encender':
                valor = coste_encender + prob_encender[i, j] * V_anterior[j]
            else:
                valor = coste_apagar + np.dot(prob_apagar[i, :], V_anterior)
            if valor > valor_max:
                valor_max = valor
        V[i] = valor_max

    difference = [abs(V[i] - V_anterior[i]) for i in range(len(V)) if prob_encender.iloc[i].any() != 0]

    if max(difference) < tolerancia:
        convergencia = True
        break
    iteraciones += 1
print("Valores de la función de valor V:", V)
print(convergencia)
"""
"""
while iteraciones < max_iteraciones:
    V_anterior = V.copy()
    for i in range(len(costes)):
        coste = costes.iloc[i]
        valor_max = float('-inf')

        for j in range(len(prob.columns)):
            valor = coste + prob.iloc[i, j] * V_anterior[j]

            if valor > valor_max:
                valor_max = valor

        V[i] = valor_max

        # Calcular el costo actualizado y guardar el resultado
        coste_actualizado = # Cálculo del nuevo costo
        resultados.append([coste_actualizado, V[i]])
"""