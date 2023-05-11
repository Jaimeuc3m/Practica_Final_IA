import csv
import pandas as pd

acciones = ['encender', 'apagar']
estados = []
for i in range(160, 255, 5):
    estados.append(i/10)

max_iteraciones = 5000
iteraciones = 0
tolerancia = 1e-5
convergencia = False

df = pd.read_csv('TPC.csv')

costes = df.iloc[:, 0]
meta = df.iloc[:, 1]
prob = df.iloc[:, 2:21]


V = [0] * len(costes)

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
