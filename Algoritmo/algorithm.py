import networkx as nx
import csv
from queue import PriorityQueue
import matplotlib.pyplot as plt

frows = list()
estrows = list()
distrows = list()
distancias = dict()
metro = nx.Graph()
TRANSBORDO = 7


def definirestructuras ():
    with open("datos/tiempos.csv", "r") as file1:
        reader1 = csv.reader(file1, delimiter=";")
        for row in reader1:
            frows.append(row)

    with open("datos/estaciones.csv", "r") as file2:
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

    with open("datos/distancias.csv", "r") as file3:
        reader3 = csv.reader(file3, delimiter=";")
        for row in reader3:
            distrows.append(row)

    for k in range(0, len(distrows)):  # Añade al dictionary
        estfinal = distrows[k][0]
        estinicial = distrows[k][1]
        distap = float(distrows[k][2])
        distancias[estfinal].append([estinicial, distap])

#Busca las distancias aproximadas entre estaciones
def buscarestaciones (estacionfin, estacionini):
    res = 0.0
    for cad in distancias[estacionfin]:
        if cad[0] == estacionini:
            res = cad[1]
            break
    return res

#Calcula la h de una estacion a la estacion destino
def h(intermedia, destino, lineaAct):
    n = buscarestaciones(destino, intermedia)
    if not lineaAct in lineasEntre(intermedia, destino):
        n = n + TRANSBORDO;
    return n

#Devuelve la linea que hay entre dos estaciones contiguas
def lineaCompartida(inicio, final):
    lineasOrigen = metro.nodes[inicio]['linea']
    lineasFinal = metro.nodes[final]['linea']
    for linea in lineasOrigen:
        if linea in lineasFinal:
            return linea
    return 0

#Devuelve la lista de las lineas que hay entre dos estaciones
def lineasEntre(inicio, final):
    lineasOrigen = metro.nodes[inicio]['linea']
    lineasFinal = metro.nodes[final]['linea']
    lineas = list()
    for linea in lineasOrigen:
        if linea in lineasFinal:
            lineas.append(linea)
    return lineas

#Devuelve el tiempo real entre dos estaciones contiguas en funcion de la
#linea en la que estabamos
def g(origen, intermedia, lineaActual):
    coste = metro.edges[origen, intermedia]['time']
    linea = lineaCompartida(origen, intermedia)
    if lineaActual != 0 and lineaActual != linea:
        coste = coste + TRANSBORDO
    return coste

def f(origen, intermedia, destino, lineaActual):
    lineaOrInter = lineaCompartida(origen, intermedia)
    return g(origen, intermedia, lineaActual) + h(intermedia, destino, lineaOrInter)

#Encuentra el arbol recubridor de menor peso que contiene a origen y destino
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
            activos.put((f(nActual, ady, nDestino, lineaActual), [ady, lineaCompartida(nActual, ady), nActual]))
    seleccionado = activos.get()
    siguienteEstacion = seleccionado[1][0]
    visitados.append(siguienteEstacion)
    solActual.add_node(siguienteEstacion)
    solActual.add_edge(seleccionado[1][2], siguienteEstacion)
    lineaActual = seleccionado[1][1]
    return findPathRec(siguienteEstacion, nDestino, activos, solActual, visitados, lineaActual)

#Dado un arbol recubridor devuelve el camino que une a origen y destino
def generarCamino(estOrigen, estDest):
    arbol = findPath(estOrigen, estDest)
    camino = list()
    visitados = list()
    camino = generarCaminoRec(estOrigen, estDest, camino, visitados, arbol)
    return camino

def generarCaminoRec(estOr, estDest, camino, visitados, arbol):
    if estOr == estDest:
        camino.append(estOr)
        return camino
    camino.append(estOr)
    visitados.append(estOr)
    sigEst = arbol.adj[estOr]
    for sig in sigEst:
        if not sig in visitados:
            posCamino = generarCaminoRec(sig, estDest, camino, visitados, arbol)
            if posCamino != None:
                return posCamino
    camino.pop()
    return None

#Calcula el tiempo que se tarda en recorrer un camino
def calcularTiempo(camino):
    lineaActual = lineaCompartida(camino[0], camino[1])
    tiempo = 0
    for i in range(len(camino)-1):
        if lineaActual == lineaCompartida(camino[i], camino[i+1]):
            tiempo = tiempo + metro.edges[camino[i], camino[i + 1]]['time']
        else:
            tiempo = tiempo + metro.edges[camino[i], camino[i + 1]]['time'] + TRANSBORDO
            lineaActual = lineaCompartida(camino[i], camino[i+1])
    return tiempo

#Devuelve una lista con las lineas que se han utilizado entre cada estacion del camino
def lineasUtilizadas(camino):
    lineas = list()
    for i in range(len(camino) - 1):
        lineas.append(lineaCompartida(camino[i], camino[i+1]))
    return lineas

definirestructuras()
camino = generarCamino("Airport", "Monastiraki")
print(camino)
tiempo = calcularTiempo(camino)
print(tiempo)
lineas =  lineasUtilizadas(camino)
print(lineas)