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

    def politica_optima(self, V0, V1, coste1, coste2, tabla1, tabla2):
        #Buscamos la politica óptima de ambos valores óptimos
        politica_optima = []
        num_estados = len(self.estados)
        for i in range(num_estados):
            estado = self.estados[i]
            valores_encendido = self.cos_sum(tabla1, coste1, num_estados, V0)
            valores_apagado = self.cos_sum(tabla2, coste2, num_estados, V1)
            cual = np.argmin([valores_encendido[i], valores_apagado[i]])
            if cual == 0:
                politica_optima.append("Encender")
            else:
                politica_optima.append('Apagar')
        #Devulve la lista de politica óptima
        return politica_optima

    def cos_sum(self, tabla, coste, num_estados, V):
        Valor = [0.0] * num_estados
        for i in range(num_estados):
            posible_valor = []
            sumatorio = 0
            for pos_des in range(num_estados):  # Realizamos el sumatorio y lo añadimos al coste
                if tabla[i][pos_des] != 0:
                    sumatorio += tabla[i][pos_des] * V[pos_des]
                    posible_valor.append(coste + sumatorio)
            Valor[i] = np.min(posible_valor)
        return Valor

