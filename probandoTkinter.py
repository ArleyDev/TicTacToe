from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random

gameMode = 0

def dialogBox():
    global gameMode

    def setGameMode():
        global gameMode
        gameMode = var.get()
        print(gameMode)
        dialog.destroy()
        root.deiconify()  # Mostrar la ventana principal después de seleccionar una opción

    dialog = Toplevel()
    dialog.title("Select Game Mode")
    dialog.geometry("300x150")
    dialog.resizable(0, 0)

    var = IntVar()
    r1 = Radiobutton(dialog, text="Player vs Player", variable=var, value=1)
    r2 = Radiobutton(dialog, text="Player vs AI (easy)", variable=var, value=2)
    r3 = Radiobutton(dialog, text="Player vs AI (hard)", variable=var, value=3)
    r1.pack()
    r2.pack()
    r3.pack()

    #agregar un botón de aceptar que llame a la función setGameMode
    boton = Button(dialog, text="Aceptar", command=setGameMode)
    boton.pack()
   
    root.withdraw()  # Ocultar la ventana principal al mostrar el diálogo

# Crear la ventana principal
root = Tk()
root.title("Main Window")

# Llamar a la función para mostrar el diálogo
dialogBox()

print("aqui imprime la variable gameMode"+str(gameMode))
root.mainloop()