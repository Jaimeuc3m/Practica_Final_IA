import numpy as np
import pandas as pd
from markov import Markov
from simulacion import SimuladorCalefaccion

def main():
    datos = pd.read_csv('TPC.csv')

    # Extraer los valores de costos y probabilidades
    coste_enc = datos.iloc[0, 0]
    coste_ap = datos.iloc[0, 1]
    probabilidades_encendido = datos.iloc[1:20, :].values
    probabilidades_apagado = datos.iloc[20:, :].values
    estados = np.arange(16, 25.5, 0.5)

    # Definir la temperatura deseada por el usuario
    temperatura_deseada = 22
    tiempo_maximo = 16

    # Crear el objeto Markov y calcular la política óptima
    solver_enc = Markov(probabilidades_encendido, coste_enc, temperatura_deseada, estados)
    solver_ap = Markov(probabilidades_apagado, coste_ap, temperatura_deseada, estados)

    V_enc = solver_enc.bellman()
    V_ap = solver_ap.bellman()

    politica_optima = solver_enc.politica_optima(V_enc, V_ap)

    # Crear el simulador de calefacción y ejecutar la simulación
    simulador = SimuladorCalefaccion(politica_optima, temperatura_deseada, tiempo_maximo)
    simulador.ejecutar_simulacion()

if __name__ == '__main__':
    main()