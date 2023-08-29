from tkinter import*
from tkinter import ttk 
from tkinter import messagebox
import random
from asyncio.windows_events import INFINITE

#insert a dialog box to select the game mode, the user can choose between three options: 1) Player vs Player, 2) Player vs AI(easy), 3) Player vs AI (hard). He will have three radio buttons to select the game mode.The result will be stored in a variable called gameMode
gameMode = 1

def dialogBox():
    global gameMode

    def setGameMode():
        global gameMode
        gameMode = var.get()
        funGameMode(gameMode)
        #print(gameMode)
        dialog.destroy()
        root.deiconify()  # Mostrar la ventana principal después de seleccionar una opción

    dialog = Toplevel()
    dialog.title("Tic Tac Toe by Arley Moreno")
    dialog.geometry("600x300")
    dialog.resizable(0, 0)

    var = IntVar()
    Label1=Label(dialog, text=" Welcome to the Tic Tac Toe Game!!",font=("Arial", 20))
    Label1.pack()
    label2=Label(dialog, text="Select Game Mode")
    label2.pack()
    #add some style to label2
    label2.configure(font=("Arial", 15))
    #chage the color of label1 to dark blue
    Label1.configure(fg="blue")
    #add some space beteween the labels
    label2.configure(padx=10,pady=10)

    r1 = Radiobutton(dialog, text="Player vs Player", variable=var, value=1,font=("Arial", 10))
    r2 = Radiobutton(dialog, text="Player vs AI (easy)", variable=var, value=2,font=("Arial", 10))
    r3 = Radiobutton(dialog, text="Player vs AI (hard)", variable=var, value=3,font=("Arial", 10))
    r1.pack()
    r2.pack()
    r3.pack()
    #add some space beteween the r3 and the button
    r3.configure(padx=10,pady=10)
    #agregar un botón de aceptar que llame a la función setGameMode
    boton = Button(dialog, text="Aceptar", command=setGameMode)
    boton.pack()
   
    root.withdraw()  # Ocultar la ventana principal al mostrar el diálogo

# Crear la ventana principal
root = Tk()
root.title("Tic Tac Toc Game- by Arley Moreno")
root.geometry("600x600")

dialogBox()

#root.mainloop()
# root=Tk()
# root.title("Tic Tac Toc Game- by Arley Moreno")


canvas=Canvas(root,width=600,height=600,background="#ffe5b4")
root.update_idletasks() 
canvas.pack()
root.update_idletasks() 


#contador=0
jugadorActual="X"
board= [["","",""],["","",""],["","",""]]
Score_X=0
Score_O=0
Tie=0

Score=NONE

def dibujarCuadricula():
    canvas.create_line(canvas.winfo_width()/3,0,canvas.winfo_width()/3,canvas.winfo_height(),width=5)
    canvas.create_line(canvas.winfo_width()*2/3,0,canvas.winfo_width()*2/3,canvas.winfo_height(),width=5)
    canvas.create_line(0,canvas.winfo_width()/3,canvas.winfo_width(),canvas.winfo_height()/3,width=5)
    canvas.create_line(0,canvas.winfo_height()*2/3,canvas.winfo_width(),canvas.winfo_height()*2/3,width=5)
dibujarCuadricula()
root.update_idletasks() 
#print(canvas.winfo_width())


def revisaGanador_Empate(posTablero,player):
    #player=""
    def devuelveResultadoGanador():
        if (player =="X"):
            return 1
        elif(player=="O"):
            return -1

    #diagonal principal
        
    if (posTablero[0][0] == player and posTablero[1][1] == player and posTablero[2][2] == player):
        S=devuelveResultadoGanador()
        return S
    
    #Filas
    if (posTablero[0][0]==player and posTablero[0][1]==player and posTablero[0][2]==player):
        S=devuelveResultadoGanador()
        return S
    if (posTablero[1][0]==player and posTablero[1][1]==player and posTablero[1][2]==player):
        S=devuelveResultadoGanador()
        return S
    if (posTablero[2][0]==player and posTablero[2][1]==player and posTablero[2][2]==player):
        S=devuelveResultadoGanador()
        return S
    #Columna
    if (posTablero[0][0]==player and posTablero[1][0]==player and posTablero[2][0]==player):
        S=devuelveResultadoGanador()
        return S
    if (posTablero[0][1]==player and posTablero[1][1]==player and posTablero[2][1]==player):
        S=devuelveResultadoGanador()
        return S
    if (posTablero[0][2]==player and posTablero[1][2]==player and posTablero[2][2]==player):
        S=devuelveResultadoGanador()
        return S

    #diagonal segundaria
    if (posTablero[0][2]==player and posTablero[1][1]==player and posTablero[2][0]==player):
        S=devuelveResultadoGanador()
        return S
# Aqui verifica si hay empate, devolviendo cero en ese caso
    emptySpots=0
    for i in range(len(posTablero)):
        for j in range(len(posTablero)):
            if (posTablero[i][j]!=""):
                emptySpots+=1
    if (emptySpots>8):
        empate=True
        return 0
 

def reiniciarJuego():
    global jugadorActual
    jugadorActual="X"
    #global contador
    global board
    global Score 
    board=[["","",""],["","",""],["","",""]]
    Score=NONE
    #contador=0
    canvas.delete("all")
    dibujarCuadricula()
   



def registrarJugada(fila,columna,currentPlayer):
    global board
    if (currentPlayer=="X"):
        board[fila][columna] = "X"
    elif (currentPlayer=="O"):
        board[fila][columna] = "O"

def dialogoGanador(resultado):
    global Score_X
    global Score_O
    global Tie
    if(resultado==1):
        respuesta=messagebox.askquestion("Player One is the Winner!!",message="Do you want to play again?")
        if (respuesta=="yes"):
            Score_X=Score_X+1
            reiniciarJuego()
           
        elif (respuesta=="no"):
            root.destroy()
    elif(resultado==-1):
        respuesta=messagebox.askquestion("Player Two is the Winner!!",message="Do you want to play again?")
        if (respuesta=="yes"):
            Score_O=Score_O+1
            reiniciarJuego()
            
        elif (respuesta=="no"):
            root.destroy()
    elif(resultado==0):
        respuesta=messagebox.askquestion("We have a Tie!!",message="Do you want to play again?")
        if (respuesta=="yes"):
            Tie=Tie+1
            reiniciarJuego()
            
        elif (respuesta=="no"):
            root.destroy()

def cambiarJugador():
    global jugadorActual
    if (jugadorActual=="X"):
        jugadorActual="O"
    elif(jugadorActual=="O"):
        jugadorActual="X"


listaDeJugadasAleatorias=[]

def jugadaAleatoriaAI():
    
    global listaDeJugadasAleatorias
    #move=([],[])
    count=0

    for i in range (len(board)):
        for j in range (len(board)):
            if (board[i][j]=="" and count<1):
                move=[i,j]
                listaDeJugadasAleatorias.append(move)

    movimientoAleatorio=random.choice(listaDeJugadasAleatorias)
    board[movimientoAleatorio[0]][movimientoAleatorio[1]]="O"
    listaDeJugadasAleatorias=[]
                
def dibujarJugadaAI():
    for i in range (len(board)):
        for j in range (len(board)):
            if(board[i][j]=="O"):

                canvas.create_oval(canvas.winfo_width()/9+j*3*canvas.winfo_width()/9,(canvas.winfo_width()/9)+i*3*canvas.winfo_width()/9,2*canvas.winfo_width()/9+j*3*canvas.winfo_width()/9,(2*canvas.winfo_width()/9)+i*3*canvas.winfo_width()/9,outline="#FF0040",width=3)


def bestMoveAI():
    global board
   
    bestScore=-INFINITE

    count=0
    move=[0,2]
    for i in range (len(board)):
       for j in range (len(board)):
            
            if (board[i][j]==""):
                board[i][j]="O"
                score=minimax(board,0,False)
    
                board[i][j]=""
                if (score>bestScore):
                    bestScore=score

                    move[0]=i
                    move[1]=j
                    

    board[move[0]][move[1]]="O"



def minimax(position,depth,maximizingPlayer):
    global board
    if (revisaGanador_Empate(board,"X")==1):
        return -1
    if (revisaGanador_Empate(board,"O")==-1):
        return 1
    if (revisaGanador_Empate(board,jugadorActual)==0):
        return 0

    if (maximizingPlayer):
        maxEvaluation=-INFINITE
        for i in range(len(position)):
            for j in range(len(position)):
                if(position[i][j]==""):
                    position[i][j]="O"
                    eval=minimax(position,depth+1,False)
                    position[i][j]=""
                    maxEvaluation=max(maxEvaluation,eval)
        return maxEvaluation

    else:
        minEvaluation=+INFINITE
        for i in range(len(position)):
            for j in range(len(position)):
                if(position[i][j]==""):
                    position[i][j]="X"
                    eval=minimax(position,depth+1,True)
                    position[i][j]=""
                    minEvaluation=min(minEvaluation,eval)
        return minEvaluation


def clickOnPlayAiMinimax(event):
    global playerOneActive
    global Score
    GameOver=False

    def luegoDeJugadaHumano():
        global Score
        if (Score==0 or Score==1 or Score==-1):
            dialogoGanador(Score)
            
        else:
            cambiarJugador()
            bestMoveAI()
            dibujarJugadaAI()
            Score= revisaGanador_Empate(board,jugadorActual)
            cambiarJugador()
            
            dialogoGanador(Score)


    if ((event.x<200 and event.y<200) and board[0][0]==""):
                
            registrarJugada(0,0,jugadorActual)
            dibujarJugada(0,0,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            #cambiarJugador()
            
            luegoDeJugadaHumano()
           
  
    if ((event.x>200 and event.x<400 and event.y<200) and board[0][1]==""):
      

            registrarJugada(0,1,jugadorActual)
            dibujarJugada(200,0,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            
            #cambiarJugador()
            luegoDeJugadaHumano()

    if ((event.x>400 and event.x<600 and event.y<200) and board[0][2]==""):
     
            registrarJugada(0,2,jugadorActual)
            dibujarJugada(400,0,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            
            #cambiarJugador()
            luegoDeJugadaHumano()

                        #Segunda Fila
                         
    if ((event.x>0 and event.x<200 and event.y>200 and event.y<400) and board[1][0]==""):
       
            registrarJugada(1,0,jugadorActual)
            dibujarJugada(0,200,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            
            #cambiarJugador()
            luegoDeJugadaHumano()


    if ((event.x>200 and event.x<400 and event.y>200 and event.y<400) and board[1][1]==""):

            registrarJugada(1,1,jugadorActual)
            dibujarJugada(200,200,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            
            #cambiarJugador()
            luegoDeJugadaHumano()


    if ((event.x>400 and event.x<600 and event.y>200 and event.y<400) and board[1][2]==""):

            registrarJugada(1,2,jugadorActual)
            dibujarJugada(400,200,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            
            #cambiarJugador()
            luegoDeJugadaHumano()

    #Tercera Fila
    if ((event.x>0 and event.x<200 and event.y>400 and event.y<600) and board[2][0]==""):

            registrarJugada(2,0,jugadorActual)
            dibujarJugada(0,400,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            #cambiarJugador()
            luegoDeJugadaHumano()

    if ((event.x>200 and event.x<400 and event.y>400 and event.y<600) and board[2][1]==""):

            registrarJugada(2,1,jugadorActual)
            dibujarJugada(200,400,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
           
            #cambiarJugador()
            luegoDeJugadaHumano()

    if ((event.x>400 and event.x<600 and event.y>400 and event.y<600) and board[2][2]==""):

            registrarJugada(2,2,jugadorActual)
            dibujarJugada(400,400,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            
            #cambiarJugador()
            luegoDeJugadaHumano()

def clickOnPlayAirandom(event):
    #global playerOneActive
    global Score
    GameOver=False
    def luegoDeJugadaOponente():
        global Score
        if (Score==0 or Score==1 or Score==-1):
            dialogoGanador(Score)
            
        else:
          
            cambiarJugador()
            jugadaAleatoriaAI()
            dibujarJugadaAI()
            Score= revisaGanador_Empate(board,jugadorActual)
            cambiarJugador()
            #print (Score)
            dialogoGanador(Score)

    if ((event.x<200 and event.y<200) and board[0][0]==""):

                  
            registrarJugada(0,0,jugadorActual)
            dibujarJugada(0,0,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            #cambiarJugador()
            #print (Score)

            luegoDeJugadaOponente()
           
    if ((event.x>200 and event.x<400 and event.y<200) and board[0][1]==""):
        

            registrarJugada(0,1,jugadorActual)
            dibujarJugada(200,0,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            #print (Score)
            #cambiarJugador()
            luegoDeJugadaOponente()

    if ((event.x>400 and event.x<600 and event.y<200) and board[0][2]==""):
        

            registrarJugada(0,2,jugadorActual)
            dibujarJugada(400,0,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            #print (Score)
            #cambiarJugador()
            luegoDeJugadaOponente()


    #Segunda Fila

    if ((event.x>0 and event.x<200 and event.y>200 and event.y<400) and board[1][0]==""):
        

            registrarJugada(1,0,jugadorActual)
            dibujarJugada(0,200,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            #print (Score)
            #cambiarJugador()
            luegoDeJugadaOponente()


    if ((event.x>200 and event.x<400 and event.y>200 and event.y<400) and board[1][1]==""):

            registrarJugada(1,1,jugadorActual)
            dibujarJugada(200,200,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            #print (Score)
            #cambiarJugador()
            luegoDeJugadaOponente()
    

    if ((event.x>400 and event.x<600 and event.y>200 and event.y<400) and board[1][2]==""):

            registrarJugada(1,2,jugadorActual)
            dibujarJugada(400,200,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            #print (Score)
            #cambiarJugador()
            luegoDeJugadaOponente()
  

    #Tercera Fila
    if ((event.x>0 and event.x<200 and event.y>400 and event.y<600) and board[2][0]==""):

            registrarJugada(2,0,jugadorActual)
            dibujarJugada(0,400,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            #print (Score)
            #cambiarJugador()
            luegoDeJugadaOponente()


    if ((event.x>200 and event.x<400 and event.y>400 and event.y<600) and board[2][1]==""):

            registrarJugada(2,1,jugadorActual)
            dibujarJugada(200,400,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            #print (Score)
            #cambiarJugador()
            luegoDeJugadaOponente()


    if ((event.x>400 and event.x<600 and event.y>400 and event.y<600) and board[2][2]==""):

            registrarJugada(2,2,jugadorActual)
            dibujarJugada(400,400,jugadorActual)
            Score= revisaGanador_Empate(board,jugadorActual)
            #print (Score)
            #cambiarJugador()
            luegoDeJugadaOponente()
 
  

def clickOnPlay(event):
    global playerOneActive

    if ((event.x<200 and event.y<200) and board[0][0]==""):
                        
        registrarJugada(0,0,jugadorActual)
        dibujarJugada(0,0,jugadorActual)
        Score= revisaGanador_Empate(board,jugadorActual)
        #print (Score)
        cambiarJugador()
        dialogoGanador(Score)
  
    if ((event.x>200 and event.x<400 and event.y<200) and board[0][1]==""):
        
        registrarJugada(0,1,jugadorActual)
        dibujarJugada(200,0,jugadorActual)
        Score= revisaGanador_Empate(board,jugadorActual)
        #print (Score)
        cambiarJugador()
        dialogoGanador(Score)

    if ((event.x>400 and event.x<600 and event.y<200) and board[0][2]==""):
        dibujarJugada(400,0,jugadorActual)
        registrarJugada(0,2,jugadorActual)
        Score= revisaGanador_Empate(board,jugadorActual)
        #print (Score)
        cambiarJugador()
        dialogoGanador(Score)

    #Segunda Fila

    if ((event.x>0 and event.x<200 and event.y>200 and event.y<400) and board[1][0]==""):
        
        dibujarJugada(0,200,jugadorActual)
        registrarJugada(1,0,jugadorActual)
        Score= revisaGanador_Empate(board,jugadorActual)
        #print (Score)
        cambiarJugador()
        dialogoGanador(Score)

    if ((event.x>200 and event.x<400 and event.y>200 and event.y<400) and board[1][1]==""):
        dibujarJugada(200,200,jugadorActual)
        registrarJugada(1,1,jugadorActual)
        Score= revisaGanador_Empate(board,jugadorActual)
        #print (Score)
        cambiarJugador()
        dialogoGanador(Score)

    if ((event.x>400 and event.x<600 and event.y>200 and event.y<400) and board[1][2]==""):
        dibujarJugada(400,200,jugadorActual)
        registrarJugada(1,2,jugadorActual)
        Score= revisaGanador_Empate(board,jugadorActual)
        #print (Score)
        cambiarJugador()
        dialogoGanador(Score)

    #Tercera Fila
    if ((event.x>0 and event.x<200 and event.y>400 and event.y<600) and board[2][0]==""):
        dibujarJugada(0,400,jugadorActual)
        registrarJugada(2,0,jugadorActual)
        Score= revisaGanador_Empate(board,jugadorActual)
        #print (Score)
        cambiarJugador()
        dialogoGanador(Score)

    if ((event.x>200 and event.x<400 and event.y>400 and event.y<600) and board[2][1]==""):
        dibujarJugada(200,400,jugadorActual)
        registrarJugada(2,1,jugadorActual)
        Score= revisaGanador_Empate(board,jugadorActual)
        #print (Score)
        cambiarJugador()
        dialogoGanador(Score)

    if ((event.x>400 and event.x<600 and event.y>400 and event.y<600) and board[2][2]==""):
        dibujarJugada(400,400,jugadorActual)
        registrarJugada(2,2,jugadorActual)
        Score= revisaGanador_Empate(board,jugadorActual)
        #print(Score)
        cambiarJugador()
        dialogoGanador(Score)
   

def dibujarJugada(coordenadaX,coordenadaY,currentPlayer):
            if (currentPlayer=="X"):
                canvas.create_line(coordenadaX+canvas.winfo_width()/9,coordenadaY+canvas.winfo_height()/9,coordenadaX+2*canvas.winfo_width()/9,coordenadaY+2*canvas.winfo_height()/9,width=3,fill="blue")
                canvas.create_line(coordenadaX+2*canvas.winfo_width()/9,coordenadaY+canvas.winfo_width()/9,coordenadaX+canvas.winfo_width()/9,coordenadaY+2*canvas.winfo_width()/9,width=3,fill="blue")
            elif(currentPlayer=="O"):
                canvas.create_oval(coordenadaX+canvas.winfo_width()/9,coordenadaY+canvas.winfo_height()/9,coordenadaX+2*canvas.winfo_width()/9,coordenadaY+2*canvas.winfo_height()/9,width=3,outline="#FF0040")
                canvas.create_oval(coordenadaX+2*canvas.winfo_width()/9,coordenadaY+canvas.winfo_width()/9,coordenadaX+canvas.winfo_width()/9,coordenadaY+2*canvas.winfo_width()/9,width=3,outline="#FF0040")


def funGameMode(gameMode):
    if(gameMode==1):
        canvas.bind("<Button-1>",clickOnPlay)
    elif(gameMode==2):
        canvas.bind("<Button-1>",clickOnPlayAirandom)
    elif(gameMode==3):
        canvas.bind("<Button-1>",clickOnPlayAiMinimax)
     

#print("aqui imprime gamemode: "+ str(gameMode))
root.mainloop()

