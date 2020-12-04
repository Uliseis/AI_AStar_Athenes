from selenium import webdriver
import csv
import time

homeURL = "https://www.google.es/maps/dir//" 
output = list()
contiguas = list()
contiguasdic = {}
coordenadas = {}

with open("../Algoritmo/contiguas.csv","r") as file1:
    reader1 = csv.reader(file1, delimiter = ";")
    for row in reader1:
        contiguas.append(row)
def conti ():
    for i in range(len(contiguas)):
        aux = list()
        for j in range(1,len(contiguas[i])):
            aux.append(contiguas[i][j])
        contiguasdic.update({contiguas[i][0] : aux})        

def readFile(file):
    f = open(file, "r")
    totalFile = f.read()
    lines = totalFile.split("\n")
    for i in range(len(lines)):
        m = lines[i].split(";") 
        aux = str(m[1]) + "," + str(m[2])
        coordenadas.update({m[0] : aux })
    f.close()

def writeOutput(file):
    f = open(file, 'w')
    for line in range(len(output)):
        f.write(str(output[line][0]) + " " + str(output[line][1] + " " +str(output[line][2])) + "\n")
    f.close()

def getCoordenadas(name):
    return coordenadas.get(name)

def getBetweenStations(fromStation,toStation):
    driver.find_element_by_xpath('//*[@id="sb_ifc50"]/input').clear()#Borra el campo comienzo
    driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input').clear()#Borra el campo destino
    driver.find_element_by_xpath('//*[@id="sb_ifc50"]/input').send_keys(fromStation) #Escribe comienzo
    driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input').send_keys(toStation)  #Escribe destino
    driver.find_element_by_xpath('//*[@id="directions-searchbox-1"]/button[1]').click() #Busca
    driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[3]/button/img').click() #Cambia a t p
    metro = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/button[2]/span[1]') # Elige el metro
    metro.clear()
    metro.click()
    driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/label/span[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="section-directions-trip-0"]/div[1]').click() # Expande
    time.sleep(0.5)
    t = driver.find_element_by_xpath('//*[@id="transit_group_0"]/div[2]/div/div[6]/div[1]/div[2]/div[2]/div/div[1]/span[1]').text #Coge texto
    print(t + "\n")                        
    return t

if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')  
    conti()
    readFile("../Algoritmo/coordenadas.csv")
    k = list(contiguasdic.keys())
    driver.get(homeURL)
    time.sleep(5)
    for i in range(len(k)):
        startname = k[i]
        start = getCoordenadas(startname)
        aux = (contiguasdic.get(startname)) #list, value of key
        for j in range(len(aux)):
            endname = aux[j]
            end = getCoordenadas(endname)
            print(startname)
            print(endname)
            output.append([startname, endname,getBetweenStations(start,end)])
            driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[1]/button').click()

    writeOutput("tiempos.csv")


    #TODO
    # linea 8 , posicion 1 - 2 - perissos
    # linea 9, posicion 0-1 - persissos
    # linea 10, posicion 2-3 - persisos