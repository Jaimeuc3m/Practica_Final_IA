import csv

acciones = ['encender', 'apagar']
estados = []
for i in range(160, 255, 5):
    estados.append(i/10)
meta = 22
V = []
iteraciones = 5000
tolerancia = 1e-5


with open('TPC.csv', 'r') as file:
    lector = csv.reader(file)
    for i in lector:
        coste_encender = i[0]
        coste_apagar = i[1]
        temp = i[2]
        break

    if temp == meta:
        V[0] = 0
    else:
        while i < iteraciones:
            i += 1
            ecuacion_encender = coste_encender + 
            ecuacion_apagar = coste_apagar +
            if ecuacion_apagar <= ecuacion_encender:
                V[i] = ecuacion_apagar
            else:
                V[i] = ecuacion_encender

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