import random
import numpy as np

class SimuladorCalefaccion:
    def __init__(self, politica_optima, temperatura_deseada, tiempo_maximo):
        self.politica_optima = politica_optima
        self.temperatura_deseada = temperatura_deseada
        self.temperatura_actual = random.choice(np.arange(16, 25.5, 0.5))
        self.tiempo_maximo = tiempo_maximo
    #Una simulacion del la calefacción
    def ejecutar_simulacion(self):
        print("Temperatura inicial:", self.temperatura_actual)
        print("Temperatura deseada:", self.temperatura_deseada)

        tiempo = 0
        hora_inicial = 9
        while tiempo <= self.tiempo_maximo:
            #acceder a la accion de la temperatura actual
            accion = self.politica_optima[int((self.temperatura_actual - 16) * 2)]
            #Hora, con formato (Hora:min)
            horas_completas = int(tiempo) // 1
            minutos = int((tiempo % 1) * 60)
            horas = (hora_inicial + horas_completas) % 24
            if horas == 24:
                horas = 0
            tiempo_actual = "{:02d}:{:02d}".format(horas, minutos)
            print("Tiempo:", tiempo_actual, "- Acción:", accion, "- Temperatura actual:", self.temperatura_actual)
            #Dependiendo de la accion, cambia la temperatura acorde a las probabilidades de la temperatura actual
            if accion == 'Encender':
                if self.temperatura_actual == 16:
                    opciones_encender = [0, 0.5, 1]
                    prob_encend = [0.3, 0.5, 0.2]
                elif self.temperatura_actual == 24.5:
                    opciones_encender = [-0.5, 0, 0.5]
                    prob_encend = [0.1, 0.2, 0.7]
                elif self.temperatura_actual == 25:
                    opciones_encender = [-0.5, 0]
                    prob_encend = [0.1, 0.9]
                else:
                    opciones_encender = [-0.5, 0, 0.5, 1]
                    prob_encend = [0.1, 0.2, 0.5, 0.2]
                #escoge caunto cambia la termperatura de forma aleatoria teniendo en cuenta sus pesos
                cambio_temperatura = random.choices(opciones_encender, weights=prob_encend)[0]
            else:
                if self.temperatura_actual == 16:
                    opciones_apagar = [0, 0.5]
                    prob_apagar = [0.9, 0.1]
                elif self.temperatura_actual == 25:
                    opciones_apagar = [-0.5, 0]
                    prob_apagar = [0.7, 0.3]
                else:
                    opciones_apagar = [-0.5, 0, 0.5]
                    prob_apagar = [0.7, 0.2, 0.1]
                #escoge caunto cambia la termperatura de forma aleatoria teniendo en cuenta sus pesos
                cambio_temperatura = random.choices(opciones_apagar, weights=prob_apagar)[0]

            self.temperatura_actual += cambio_temperatura
            self.temperatura_actual = max(min(self.temperatura_actual, 25), 16)  # Aplicar límites
            self.temperatura_actual = round(self.temperatura_actual, 1)  # Redondear a una decimal
            #En cuanto la temperatura llegue a la temperatura deseada, para
            if self.temperatura_actual == self.temperatura_deseada:
                print("Simulación finalizada. Temperatura alcanzada:", self.temperatura_actual)
                break
            tiempo += 0.5
        if self.temperatura_actual != self.temperatura_deseada:
            print("Tiempo máximo alcanzado. Temperatura actual:", self.temperatura_actual)

