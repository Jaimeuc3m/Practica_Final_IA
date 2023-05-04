import csv

meta = 22
iteraciones = 5000
tolerancia = 1e-5


with open('TPC.csv', 'r') as file:
    lector = csv.reader(file)
    for i in lector:
        print(i)