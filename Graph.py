import networkx as nx;
import csv

distrows = list()
distancias = dict()
with open("distancias.csv", "r") as file1:
    reader1 = csv.reader(file1)
    for row in reader1:
        distrows.append(row)

for k in len(distrows):  # Añade al dictionary
    estinicial = distrows[k][0]
    estfinal = distrows[k][1]
    distap = int(distrows[k][2])
    listaestaciones = list()
    for n in len (distrows):

    distancias[estfinal] = [estinicial, distap]

frows = list()
estrows = list()

with open("distancias2.csv", "r") as file2:
    reader2 = csv.reader(file2)
    for row in reader2:
        frows.append(row)

with open("estaciones.csv", "r") as file3:
    reader3 = csv.reader(file3)
    for row in reader3:
        estrows.append(row)

metro = nx.Graph()
for i in len(estrows):  # Añade nodos
    nodo = estrows[i][0]
    line = list()
    for j in range (1, len(estrows[i])):
        line.append(int(estrows[i][j]))
    metro.add_node(nodo, linea=line)

for j in len(frows):  # Añade aristas
    first = frows[j][0]
    second = frows[j][1]
    distance = int(frows[j][2])
    if not metro.has_edge(second, first):
        metro.add_edge(first, second, time=distance)
