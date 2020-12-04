import networkx as nx
import csv
from queue import PriorityQueue

frows = list()
estrows = list()
distrows = list()
distancias = dict()
metro = nx.Graph()
TRANSBORDO = 7

def definirestructuras ():
    with open("tiempos.csv", "r") as file1:
        reader1 = csv.reader(file1, delimiter=" ")
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

def h(intermedia, destino, lineaAct):
    n = buscarestaciones(destino, intermedia)
    if lineaAct != lineaCompartida(intermedia, destino):
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
    if lineaActual != 0 and not lineaActual in listaLineas:
        coste = coste + TRANSBORDO
    return coste

def f(origen, intermedia, destino, lineaActual):
    lineaOrInter = lineaCompartida(origen, intermedia)
    return g(origen, intermedia, lineaActual) + h(intermedia, destino, lineaOrInter)

def findPath(origen, destino):
    activos = PriorityQueue()
    solucion = nx.Graph()
    solucion.add_node(origen)
    visitados = list()
    visitados.append(origen)
    lineaActual = 0
    return findPathRec(origen, destino, activos, solucion, visitados, lineaActual)


def findPathRec(nActual, nDestino, activos, solActual, visitados, lineaActual):
    if nActual == nDestino:
        return solActual
    nuevosAbiertos = metro.adj[nActual]
    for ady in nuevosAbiertos:
        if not ady in visitados:
            activos.put(f(nActual, ady, nDestino, lineaActual), [ady, lineaCompartida(nActual, ady)])
    seleccionado = activos.get()
    siguienteEstacion = seleccionado[0]
    visitados.append(siguienteEstacion)
    solActual.add_node(siguienteEstacion)
    solActual.add_edge(nActual, siguienteEstacion)
    lineaActual = seleccionado[1]
    return findPathRec(siguienteEstacion, nDestino, activos, solActual, visitados, lineaActual)

def generarCamino(estOrigen, estDest):
    arbol = findPath(estOrigen, estDest)



