import numpy as np

class Markov:
    def __init__(self, tabla, coste, meta, estados, tolerancia = 0.00001, max_iteraciones=5000):
        self.tabla = tabla
        self.coste = coste
        self.meta = meta
        self.estados = estados
        self.tolerancia = tolerancia
        self.max_iteraciones = max_iteraciones
    #introducimos la ecuacion de bellman
    def bellman(self):
        #Calculamos el numero de estados de la taba, iniciamos el array de valores a 0 e inicializamos la Convergencia
        num_estados = self.tabla.shape[0]
        V = np.zeros(num_estados)
        convergencia = False
        iteraciones = 0
        #mientras que no haya convergencia y las iteraciones sean inferiores al maximo
        while not convergencia and iteraciones < self.max_iteraciones:
            V_antiguo = V.copy()
            #iteramos sobre i hasta que llegue al num_estados
            for i in range(num_estados):
                estado = self.estados[i]
                posible_valor = []
                sumatorio = 0
                if estado != self.meta:                         #Comprobamos que el estado actual no es la meta
                    for pos_des in range(num_estados):          #Realizamos el sumatorio y lo añadimos al coste
                        if self.tabla[i][pos_des] != 0:
                            sumatorio += self.tabla[i][pos_des] * V_antiguo[pos_des]
                            posible_valor.append(self.coste + sumatorio)
                    V[i] = np.min(posible_valor)
                else:
                    V[i] = 0.0
            #Buscamos la convergencia
            if np.linalg.norm(V - V_antiguo) < self.tolerancia:
                convergencia = True
            iteraciones += 1

        return V

    def politica_optima(self, V0, V1, V2):
        #Buscamos la politica óptima de ambos valores óptimos
        politica_optima = []

        for i in range(len(self.estados)):
            estado = self.estados[i]
            #Si el estado actual es la meta, va apagar la calefaccion
            valor_encendido = V0[i]
            valor_apagado = V1[i]
            #valor_mantenido = V2[i]
            #vamos yendo 1 por 1 los valores óptimos, comparando sus valores
            if valor_encendido <= valor_apagado:
                politica_optima.append('Encender')
            #elif valor_mantenido <= valor_apagado and politica_optima [i-1] == "encender" or politica_optima [i-1] == "mantener":
            #    politica_optima.append("mantener encendido")
            else:
                politica_optima.append('Apagar')
        #Devulve la lista de politica óptima
        return politica_optima

