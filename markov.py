import numpy as np

class Markov:
    def __init__(self, tabla1, tabla2, coste1, coste2, meta, estados, tolerancia = 0.00001, max_iteraciones=5000):
        self.tabla1 = tabla1
        self.tabla2 = tabla2
        self.coste1 = coste1
        self.coste2 = coste2
        self.meta = meta
        self.estados = estados
        self.tolerancia = tolerancia
        self.max_iteraciones = max_iteraciones
        self.num_estados = len(estados)
    #introducimos la ecuacion de bellman
    def bellman(self):
        #Calculamos el numero de estados de la taba, iniciamos el array de valores a 0 e inicializamos la Convergencia
        V = np.zeros(self.num_estados)
        convergencia = False
        iteraciones = 0
        #mientras que no haya convergencia y las iteraciones sean inferiores al maximo
        while not convergencia and iteraciones < self.max_iteraciones:
            V_antiguo = V.copy()
            #iteramos sobre i hasta que llegue al num_estados
            for i in range(self.num_estados):
                estado = self.estados[i]
                posible_valor = []
                sumatorio1 = 0
                sumatorio2 = 0
                if estado != self.meta:                         #Comprobamos que el estado actual no es la meta
                    for pos_des in range(self.num_estados):          #Realizamos el sumatorio y lo añadimos al coste
                        if self.tabla1[i][pos_des] != 0:
                            sumatorio1 += self.tabla1[i][pos_des] * V_antiguo[pos_des]

                        if self.tabla2[i][pos_des] != 0:
                            sumatorio2 += self.tabla2[i][pos_des] * V_antiguo[pos_des]
                    posible_valor.append(self.coste1 + sumatorio1)
                    posible_valor.append(self.coste2 + sumatorio2)
                    V[i] = np.min(posible_valor)
                else:
                    V[i] = 0.0
            #Buscamos la convergencia
            if np.linalg.norm(V - V_antiguo) < self.tolerancia:
                convergencia = True
            iteraciones += 1
        print("Número de iteraciones: ", iteraciones)
        return V

    def politica_optima(self, V):
        #Buscamos la politica óptima de ambos valores óptimos
        politica_optima = []
        for i in range(self.num_estados):
            valores_encendido = self.cos_sum(self.tabla1, self.coste1, V)
            valores_apagado = self.cos_sum(self.tabla2, self.coste2, V)
            if valores_encendido[i] < valores_apagado[i]:
                politica_optima.append('Encender')
            else:
                politica_optima.append('Apagar')
        #Devulve la lista de politica óptima
        return politica_optima

    def cos_sum(self, tabla, coste, V):
        Valor = []
        for i in range(self.num_estados):
            sumatorio = 0
            for pos_des in range(self.num_estados):  # Realizamos el sumatorio y lo añadimos al coste
                if tabla[i][pos_des] != 0:
                    sumatorio += tabla[i][pos_des] * V[pos_des]
            Valor.append(coste + sumatorio)
        return Valor

