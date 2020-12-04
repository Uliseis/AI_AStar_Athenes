from selenium import webdriver
import csv
import time
homeURL = "https://www.google.es/maps/dir//" 
line_print = list()
line_input = list()
contiguas = {}
coordenadas = {}

def contiguasRead(file):
    f = open(file, "r")
    totalFile = f.read()
    lines = totalFile.split("\n").split(";")
    for i in range(len(lines)):
        for j in range(1,len(lines[i])):
            contiguas.update({lines[i][0] : lines[i][j]})
    f.close()

def readFile(file):
    f = open(file,"r")
    totalFile = f.read()
    lines = totalFile.split("\n").split(";")
    for i in range(len(lines)):
        coordenadas.update({lines[i][0] : lines[i][1]})
        



def getBetweenStations(fromStation,toStation):
    driver.find_element_by_xpath('//*[@id="sb_ifc50"]/input').clear_field()#Borra el campo comienzo
    driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input').clear_field()#Borra el campo destino
    driver.find_element_by_xpath('//*[@id="sb_ifc50"]/input').send_keys(fromStation) #Escribe comienzo
    driver.find_element_by_xpath('//*[@id="sb_ifc51"]/input').send_keys(toStation)  #Escribe destino
    driver.find_element_by_xpath('//*[@id="directions-searchbox-1"]/button[1]').click() #Busca
    driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[3]/button/img').click() #Cambia a t p
    driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/button[2]/span[1]').click() # Elige el metro
    driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/label/span[2]').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="section-directions-trip-0"]/div[1]').click() # Expande
    time.sleep(1)
    t = driver.find_element_by_xpath('//*[@id="transit_group_0"]/div[2]/div/div[6]/div[1]/div[2]/div[2]/div/div[1]/span[1]').text #Coge texto
    l.append(t)

if __name__ == '__main__':
    driver = webdriver.Chrome('./chromedriver')  
    readFile('contiguas.csv')
    driver.get(homeURL)
    time.sleep(5)
    start = "37.999439265603414,23.72276748575201" #Atiki
    end = "37.992113729429086,23.72110445426731"   #Larissa 
    getBetweenStations(start,end)
