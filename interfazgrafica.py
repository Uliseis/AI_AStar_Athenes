import tkinter as tk
from Algoritmo.algorithm import definirestructuras, generarCamino, calcularTiempo, lineasUtilizadas


def ventanaresultado():
    win2 = tk.Toplevel()
    win2.geometry("1280x960")
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

    tk.Label(win2, text="Camino entre ambas estaciones: \n" + total).place(x=200, y=150)
    tk.Label(win2, text="Tiempo entre " + str(e1.get()) + " y " + str(e2.get()) + ": " + str(int(tiempo)) + " minutos.",
             fg="blue").place(x=400, y=150)

    tk.Button(win2,
              text='Salir',
              command=win2.destroy).place(x=600, y=500)


definirestructuras()

master = tk.Tk()

master.geometry("640x480")

#master.iconbitmap("atena.ico")

master.title("Metro de Atenas")

imagen = tk.PhotoImage(file="metro.gif")
tk.Label(master, image=imagen).place(x=240, y=25)
tk.Label(master,
         text="Introduce estaciones para las cuales quieres\nobtener el tiempo de desplazamiento") \
    .place(x=200, y=130)
tk.Label(master,
         text="Estacion de origen:").place(x=150, y=175)
tk.Label(master,
         text="Estacion de destino:").place(x=150, y=200)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.place(x=280, y=175)
e2.place(x=280, y=200)

tk.Button(master,
          text='Salir',
          command=master.quit).place(x=220, y=250)
tk.Button(master,
          text='Mostrar', command=ventanaresultado).place(x=380, y=250)

tk.mainloop()
