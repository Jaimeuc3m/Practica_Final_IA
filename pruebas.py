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
estados = [16 + i * 0.5 for i in range(19)]

prob_encender = []
prob_apagar = []

with open('TPC.csv', 'r') as file:
    lector_csv = csv.reader(file)
    datos = list(lector_csv)

    for i in range(1, 20):
        fila = [float(dato) for dato in datos[i]]
        prob_encender.append(fila)
    for i in range(20, len(datos)):
        fila = [float(dato) for dato in datos[i]]
        prob_apagar.append(fila)

num_estados = len(estados)
V = [0.0] * num_estados
coste_encender = float(datos[0][0])
coste_apagar = float(datos[0][1])
V_antiguo = V.copy()

while not convergencia and iteraciones < max_iteraciones:
    i = 0
    valores = []
    while estados[i] and i < num_estados:
        estado = estados[i]
        posible_valor = []
        sumatorio = 0
        if estado != meta:
            for pos_dest in prob_encender[i]:
                if pos_dest != 0:
                    sumatorio += pos_dest * V_antiguo[i]
            posible_valor.append(coste_encender + sumatorio)
            V[i] = min(posible_valor)
        else:
            V[i] = [0.0]
        i += 1
    j = 0
    for antiguo in V_antiguo:
        nuevo = V[j]
        if abs(antiguo/nuevo) < tolerancia:
            convergencia = True
    iteraciones += 1
    print(iteraciones)

"""
politica_optima = []
for estado in range(num_estados):
    valor_encender = coste_encender + min([prob_encender[estado][i] * V_antiguo[i] for i in range(num_estados)])
    valor_apagar = coste_apagar + min([prob_apagar[estado][i] * V_antiguo[i] for i in range(num_estados)])

    if valor_encender > valor_apagar:
        politica_optima.append('Encender')
    else:
        politica_optima.append('apagar')
print(politica_optima)
"""
"""
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