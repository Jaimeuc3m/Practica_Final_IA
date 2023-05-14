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
    while i < num_estados and estados[i] <= 25:
        estado = estados[i]
        posible_valor = []
        sumatorio = 0
        if estado != meta:
            for pos_dest in prob_encender[i]:
                if pos_dest != 0:
                    sumatorio += pos_dest * V_antiguo[i]
            posible_valor.append(coste_encender + sumatorio)
            V[i] = min(posible_valor)
            print(V)
            print(V_antiguo)
        i += 1
    j = 0
    for antiguo in V_antiguo:
        nuevo = V[j]
        if abs(antiguo/nuevo) < tolerancia:
            convergencia = True
    iteraciones += 1


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
