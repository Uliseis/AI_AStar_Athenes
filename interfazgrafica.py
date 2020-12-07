import tkinter as tk
from Algoritmo.algorithm import definirestructuras, generarCamino, calcularTiempo, lineasUtilizadas, listaNodos
import time


def controlErrores():
    origen = e1.get()
    destino = e2.get()
    estaciones = listaNodos()
    if origen == destino:
        errA = tk.Label(master, text="Estacion de origen debe ser distinta la de destino", bg="red")
        errA.config(font=("Arial", 11))
        errA.pack()
        errA.place(x=100, y=430)
        master.after(4000, errA.destroy)
        return
    if not origen in estaciones:
        errOr = tk.Label(master, text="Estacion de origen incorrecta", bg="red")
        errOr.config(font=("Arial", 11))
        errOr.pack()
        errOr.place(x=170, y=330)
        master.after(4000, errOr.destroy)
    if not destino in estaciones:
        errDest = tk.Label(master, text="Estacion de destino incorrecta", bg="red")
        errDest.config(font=("Arial", 11))
        errDest.pack()
        errDest.place(x=170, y=360)
        master.after(4000, errDest.destroy)
    if destino in estaciones and origen in estaciones:
        ventanaresultado()

def ventanaresultado():
    win2 = tk.Toplevel()
    win2.geometry("640x560")
    #win2.iconbitmap("atena.ico")
    total = ""
    camino = generarCamino(e1.get(), e2.get())
    tiempo = calcularTiempo(camino)
    lineas = lineasUtilizadas(camino)
    for i in range(len(camino)):
        if i != len(camino)-1:
            total += camino[i] + " - " + str(lineas[i]) + "\n"
        else:
            total += camino[i]

    tk.Label(win2, text="Camino entre ambas estaciones: \n" + total).place(x=75, y=75)
    tk.Label(win2, text="Tiempo entre " + str(e1.get()) + " y " + str(e2.get()) + ": " + str(int(tiempo)) + " minutos.",
             fg="blue").place(x=295, y=75)

    tk.Button(win2,
              text='Salir',
              command=win2.destroy).place(x=400, y=475)


definirestructuras()
master = tk.Tk()

master.geometry("640x480")
master.resizable(False, False)

#master.iconbitmap("atena.ico")

master.title("Metro de Atenas")

text = tk.Text(master)
text.configure(font=("Courier", 24, "italic"))

imagen = tk.PhotoImage(file="metro.gif")
tk.Label(master, image=imagen).place(x=320-(imagen.width()/2), y=25)

intro = tk.Label(master,
         text="Introduce estaciones para las cuales quieres\nobtener el tiempo de desplazamiento")
intro.place(x=115, y=155)
intro.config(font=("Arial", 16))

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
