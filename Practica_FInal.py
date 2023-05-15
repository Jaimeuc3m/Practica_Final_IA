import numpy as np
import pandas as pd
from markov import Markov
from simulacion import SimuladorCalefaccion

def main():
    datos = pd.read_csv('TPC.csv')

    # Extraer los valores de costos y probabilidades
    coste_enc = datos.iloc[0, 0]
    coste_ap = datos.iloc[0, 1]
    #coste_man = datos.iloc[0,2]
    probs_encendido = datos.iloc[1:20, :].values
    probs_apagado = datos.iloc[20:, :].values
    estados = np.arange(16, 25.5, 0.5)

    # Definir la temperatura deseada y el tiempo maximo de la simulacion
    temperatura_deseada = 22
    tiempo_maximo = 10

    # Crear el objeto Markov y calcular la política óptima
    solver = Markov(probs_encendido, probs_apagado, coste_enc, coste_ap, temperatura_deseada, estados)
    #solver_man = Markov(probabilidades_encendido, coste_man, temperatura_deseada, estados)

    V = solver.bellman()

    politica_optima = solver.politica_optima(V)
    print(politica_optima)
    # Crear el simulador de calefacción y ejecutar la simulación
    simulador = SimuladorCalefaccion(politica_optima, temperatura_deseada, tiempo_maximo)
    simulador.ejecutar_simulacion()

if __name__ == '__main__':
    main()