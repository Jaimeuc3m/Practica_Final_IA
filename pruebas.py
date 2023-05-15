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
temperatura_deseada = 22

# Obtener el número de estados y acciones
num_estados = probabilidades_encendido.shape[0]
num_acciones = 2  # Encendido (acción 0) o Apagado (acción 1)

# Crear una matriz de valores óptimos inicializados en cero
V = np.zeros(num_estados)

# Definir la función de utilidad de las acciones
acciones = np.array([coste_enc, coste_ap])

# Iterar hasta alcanzar la convergencia
convergencia = False
tolerancia = 0.00001
max_iteraciones = 5000
iteraciones = 0

while not convergencia and iteraciones < max_iteraciones:
    V_antiguo = V.copy()
    print("Antiguo: ", V_antiguo)
    i = 0
    while i < num_estados:
        estado = estados[i]
        posible_valor = []
        sumatorio = 0
        if estado != temperatura_deseada:
            for pos_des in range(num_estados):
                if probabilidades_encendido[i][pos_des] != 0:
                    sumatorio += probabilidades_encendido[i][pos_des] * V_antiguo[pos_des]
                posible_valor.append(coste_enc + sumatorio)
                print(pos_des)
            V[i] = np.min(posible_valor)
        else:
            V[i] = 0.0
        i += 1
        print(posible_valor)
        print("Valor ", V)
    if np.linalg.norm(V - V_antiguo) < tolerancia:
        convergencia = True
    iteraciones += 1
print("Iteraciones:", iteraciones)
print("Convergencia:", convergencia)
print("Valores óptimos:")
print(V)

