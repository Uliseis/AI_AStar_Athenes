import numpy as np
from math import radians, cos, sin, asin, sqrt
import os


class distance_Calculator():

    stations = {}
    distances = list()

    def __init__(self):
        pass

    def readFile(self, file):
        f = open(file, "r")
        totalFile = f.read()
        lines = totalFile.split("\n")
        for i in range(len(lines) - 1):
            param = lines[i].split(";")
            self.stations[param[0]] = [float(param[1]), float(param[2])]
        f.close()

    def distance(self, lat1, lon1, lat2, lon2):

        # The math module contains a function named
        # radians which converts from degrees to radians.
        lon1 = radians(lon1)
        lon2 = radians(lon2)
        lat1 = radians(lat1)
        lat2 = radians(lat2)

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2

        c = 2 * asin(sqrt(a))

        # Radius of earth in kilometers. Use 3956 for miles
        r = 6371

        # calculate the result
        return (c * r)


    def calc_dists(self):
        l = list(self.stations.items())
        for i in range(len(l)):
            for j in range(len(l)):
                if i == j:
                    continue
                o1 = l[i]
                o2 = l[j]
                dist = (self.distance(o1[1][1], o1[1][0], o2[1][1], o2[1][0]) * 1000)/1332.8
                self.distances.append([o1[0], o2[0], dist])


    def writeFile(self, file):
        f = open(file, "w")
        for i in range(len(self.distances)-1):
            f.write(str(self.distances[i][0]) + ";" + str(self.distances[i][1]) + ";" + str(self.distances[i][2]) + os.linesep)
        f.write(str(self.distances[len(self.distances)-1][0]) + ";" + str(self.distances[len(self.distances)-1][1]) +
                ";" + str(self.distances[len(self.distances)-1][2]))
        f.close()



dC = distance_Calculator()
fileI = "coordenadas.csv"
fileO = "distancias.csv"
dC.readFile(fileI)
dC.calc_dists()
dC.writeFile(fileO)


