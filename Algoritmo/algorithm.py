import networkx as nx
import csv

frows = list()
estrows = list()
distrows = list()
distancias = dict()
metro = nx.Graph()
lineaActual = 0
TRANSBORDO = 7

def definirestructuras ():
    with open("tiempos.csv", "r") as file1:
        reader1 = csv.reader(file1, delimiter=";")
        for row in reader1:
            frows.append(row)

    with open("estaciones.csv", "r") as file2:
        reader2 = csv.reader(file2, delimiter=";")
        for row in reader2:
            estrows.append(row)

    for i in range(0, len(estrows)):  # Añade nodos
        nodo = estrows[i][0]
        line = list()
        for j in range(1, len(estrows[i])):
            line.append(int(estrows[i][j]))
        distancias[nodo] = list()
        metro.add_node(nodo, linea=line)

    for j in range(0, len(frows)):  # Añade aristas
        first = frows[j][0]
        second = frows[j][1]
        distance = float(frows[j][2])
        if not metro.has_edge(second, first):
            metro.add_edge(first, second, time=distance)

    with open("distancias.csv", "r") as file3:
        reader3 = csv.reader(file3, delimiter=";")
        for row in reader3:
            distrows.append(row)

    for k in range(0, len(distrows)):  # Añade al dictionary
        estfinal = distrows[k][0]
        estinicial = distrows[k][1]
        distap = float(distrows[k][2])
        distancias[estfinal].append([estinicial, distap])


def buscarestaciones (estacionfin, estacionini):
    res = float
    for cad in distancias[estacionfin]:
        if cad[0] == estacionini:
            res = cad[1]
            break
    return res

def h(intermedia, destino):
    n = buscarestaciones(destino, intermedia)
    if not metro[intermedia]['linea'] in metro[destino]['linea']:
        n = n + TRANSBORDO;
    return n

def lineaCompartida(inicio, final):
    lineasOrigen = metro[inicio]['linea']
    lineasFinal = metro[final]['linea']
    for linea in lineasOrigen:
        if linea in lineasFinal:
            return linea
    return 0

def g(origen, intermedia, lineaActual):
    coste = metro.edges[origen][intermedia]['time']
    listaLineas = metro[origen, intermedia]['linea']
    if not lineaActual in listaLineas:
        coste = coste + TRANSBORDO
    return coste

def f(origen, intermedia, destino, listDistAereas, lineaActual):
    return g(origen, intermedia, lineaActual) + h(intermedia, destino, listDistAereas)

def findPath(origen, destino):



def findPathRec(nOrigen, nDestino, distAereas, ):
