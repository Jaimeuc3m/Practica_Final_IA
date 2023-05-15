import pandas as pd
import numpy as np

# Cargar los datos del archivo CSV
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
num_acciones = 2  # Encendido (acción 0) o Apagado (acción 1)

# Crear una matriz de valores óptimos inicializados en cero
V_enc = np.zeros(num_estados)
V_ap = np.zeros(num_estados)

# Definir la función de utilidad de las acciones
acciones = np.array([coste_enc, coste_ap])

# Iterar hasta alcanzar la convergencia
convergencia = False
tolerancia = 0.00001
max_iteraciones = 5000
iteraciones = 0

while not convergencia and iteraciones < max_iteraciones:
    V_antiguo_enc = V_enc.copy()
    i = 0
    while i < num_estados:
        estado = estados[i]
        posible_valor = []
        sumatorio = 0
        if estado != meta:
            for pos_des in range(num_estados):
                if probabilidades_encendido[i][pos_des] != 0:
                    sumatorio += probabilidades_encendido[i][pos_des] * V_antiguo_enc[pos_des]
                    posible_valor.append(coste_enc + sumatorio)
            V_enc[i] = np.min(posible_valor)
        else:
            V_enc[i] = 0.0
        i += 1
    if np.linalg.norm(V_enc - V_antiguo_enc) < tolerancia:
        convergencia = True
    iteraciones += 1
print("Iteraciones:", iteraciones)
print("Convergencia:", convergencia)
print("Valores óptimos:")
print(V_enc)

convergencia = False
iteraciones = 0
while not convergencia and iteraciones < max_iteraciones:
    V_antiguo_ap = V_ap.copy()
    i = 0
    while i < num_estados:
        estado = estados[i]
        posible_valor = []
        sumatorio = 0
        if estado != meta:
            for pos_des in range(num_estados):
                if probabilidades_apagado[i][pos_des] != 0:
                    sumatorio += probabilidades_apagado[i][pos_des] * V_antiguo_ap[pos_des]
                    posible_valor.append(coste_ap + sumatorio)
            V_ap[i] = np.min(posible_valor)
        else:
            V_ap[i] = 0.0
        i += 1
    if np.linalg.norm(V_ap - V_antiguo_ap) < tolerancia:
        convergencia = True
    iteraciones += 1
print("Iteraciones:", iteraciones)
print("Convergencia:", convergencia)
print("Valores óptimos:")
print(V_ap)
i = 0
politica_optima = []
valores_enc = []
valores_ap = []
while i < num_estados:
    sumatorio_encendido = 0
    sumatorio_apagado = 0
    for pos_des in range(num_estados):
        if probabilidades_encendido[i][pos_des] != 0:
            sumatorio_encendido += probabilidades_encendido[i][pos_des] * V_enc[pos_des]
        if probabilidades_apagado[i][pos_des] != 0:
            sumatorio_apagado += probabilidades_apagado[i][pos_des] * V_ap[pos_des]
    valores_enc.append(coste_enc + sumatorio_encendido)
    valores_ap.append(coste_ap + sumatorio_apagado)
    i += 1
print("Valores_enc ", valores_enc)
print("Valores_ap ", valores_ap)
for i in range(num_estados):
    if valores_enc[i] < valores_ap[i]:
        politica_optima.append('Encender')
    else:
        politica_optima.append('Apagar')
print("Política óptima:")
print(politica_optima)



