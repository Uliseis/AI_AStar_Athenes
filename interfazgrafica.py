from tkinter import *
import tkinter as tk
from Algoritmo.algorithm import definirestructuras, generarCamino, calcularTiempo, lineasUtilizadas, listaNodos
import os


def controlErrores():
    origen = e1.get()
    destino = e2.get()
    estaciones = listaNodos()
    if not origen in estaciones:
        errOr = tk.Label(master, text="Estacion de origen incorrecta", bg="red")
        errOr.config(font=("Arial", 11))
        errOr.pack()
        errOr.place(x=170, y=330)
        master.after(3500, errOr.destroy)
    if not destino in estaciones:
        errDest = tk.Label(master, text="Estacion de destino incorrecta", bg="red")
        errDest.config(font=("Arial", 11))
        errDest.pack()
        errDest.place(x=170, y=360)
        master.after(3500, errDest.destroy)
    if origen == destino:
        errA = tk.Label(master, text="Estacion de origen debe ser distinta la de destino", bg="red")
        errA.config(font=("Arial", 11))
        errA.pack()
        errA.place(x=100, y=430)
        master.after(3500, errA.destroy)
        return
    if destino in estaciones and origen in estaciones:
        ventanaresultado(origen, destino)

def ventanaresultado(origen, destino):
    win2 = tk.Toplevel()
    win2.geometry("640x560")
    #win2.iconbitmap("atena.ico")
    total = ""
    camino = generarCamino(origen, destino)
    largo = 200
    longitud = len(camino)
    largo += 15 * len(camino)
    tama = "640x" + str(largo)
    win2.geometry(tama)
    win2.resizable(False, False)
    tiempo = calcularTiempo(camino)
    lineas = lineasUtilizadas(camino)
    for i in range(len(camino)):
        if i != len(camino)-1:
            total += camino[i] + "\n"
        else:
            total += camino[i]
    lin =""
    linea = 0
    for i in range(len(lineas)):
        if linea == 0:
            if lineas[i] == 1:
                lin += "Linea " + str(lineas[i]) + '\n'
                linea = lineas[i]
            elif lineas[i] == 2:
                lin += "\tLinea " + str(lineas[i]) + '\n'
                linea = lineas[i]
            else:
                lin += "\t\tLinea " + str(lineas[i]) + '\n'
                linea = lineas[i]
        elif linea != lineas[i]:
            if lineas[i] == 1:
                lin += "Linea " + str(lineas[i]) + '\n'
                linea = lineas[i]
            elif lineas[i] == 2:
                lin += "\tLinea " + str(lineas[i]) + '\n'
                linea = lineas[i]
            else:
                lin += "\t\tLinea " + str(lineas[i]) + '\n'
                linea = lineas[i]
        else:
            if lineas[i] == 1:
                lin += "   |" + '\n'
            elif lineas[i] == 2:
                lin += "\t   |" + '\n'
            else:
                lin += "\t\t   |" + '\n'
    if lineas[len(lineas) - 1] == 1:
        lin += "   |"
    elif lineas[len(lineas) - 1] == 2:
        lin += "\t   |"
    else:
        lin += "\t\t   |"
    etiqCamino = tk.Label(win2, text="Camino entre ambas estaciones: \n")
    etiqCamino.place(x=40, y=30)
    etiqCamino.config(font=("Calibri", 16))

    cam = tk.Label(win2, text=total, justify=LEFT)
    cam.place(x=50, y=70)
    cam.config(font=("Arial", 11))

    etiqLin = tk.Label(win2, text=lin, justify=LEFT)
    etiqLin.place(x=300, y=70)
    etiqLin.config(font=("Arial", 11))

    tiemp = tk.Label(win2, text="Trayecto entre " + origen + " y " + destino + ": " + os.linesep + str(int(tiempo))
                                + " minutos", fg="blue")
    tiemp.place(x=50, y=largo-100)
    tiemp.config(font=("Calibri", 13))

    botonSalir = tk.Button(win2, text='Salir', command=win2.destroy)
    botonSalir.place(x=530, y=largo-60)

definirestructuras()
master = tk.Tk()

master.geometry("640x480")
master.resizable(False, False)

#master.iconbitmap("atena.ico")

master.title("Metro de Atenas")

imagen = tk.PhotoImage(file="metro.gif")
tk.Label(master, image=imagen).place(x=320-(imagen.width()/2), y=25)

intro = tk.Label(master,
         text="Introduce estaciones para las cuales quieres\nobtener el tiempo de desplazamiento")
intro.place(x=115, y=155)
intro.config(font=("Calibri", 16))

ori = tk.Label(master, text="Estacion de origen:")
ori.place(x=130, y=250)
ori.config(font=("Arial", 11))

des = tk.Label(master, text="Estacion de destino:")
des.place(x=130, y=300)
des.config(font=("Arial", 11))

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.place(x=330, y=250)
e2.place(x=330, y=300)


tk.Button(master,
          text='Salir',
          command=master.quit).place(x=170, y=400)
bot = tk.Button(master, text='Mostrar', command=controlErrores)
bot.place(x=330, y=400)

tk.mainloop()
