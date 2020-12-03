import networkx as nx

metro = nx.Graph
distancias = {}
lineaActual = 0

TRANSBORDO = 7

def h(intermedia, destino, listDistAereas):
    n = 0;
    for dist in listDistAereas:
        if dist[0] == intermedia:
            n = dist[1]
            break
    if not metro[intermedia]['linea'] in metro[destino]['linea']:
        n = n + TRANSBORDO;
    return n

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
