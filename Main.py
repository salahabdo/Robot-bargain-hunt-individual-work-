#open in python 3 not 2
from tkinter import *
import tkinter.messagebox
from game import *
###################################################
#Salah's own feature to the game.
Game = Tk()
Game.title("it belongs in the museum")
Game.geometry("550x400+200+200")

def QuitGame():
    Game.destroy()# destroying the main window
def StartGameDes():
    TIME = (Game.TIME.get())
    SORT = True
    LOOP = int(Game.LOOP.get())
    GameLoop(TIME, SORT, LOOP)
    Game.destroy()
def StartGameAsc():
    TIME = (Game.TIME.get())
    SORT = False
    LOOP = int(Game.LOOP.get())
    GameLoop(TIME, SORT, LOOP)
    Game.destroy()


w = Label(Game, text="It belongs in the museum!", fg="red", font=("Helvetica",25))
w.pack()

Game.label = Label (Game, text= "what frame rate would you like to run at ?")
Game.label.pack()

Game.TIME = StringVar()
Entry(Game, textvariable=Game.TIME).pack()

Game.label = Label (Game, text= "How many times do you want the game to loop for ?")
Game.label.pack()

Game.LOOP = StringVar()
Entry(Game, textvariable=Game.LOOP).pack()


QuitButton = Button(Game, text= "Quit", width=20,command=QuitGame)
QuitButton.pack(side="bottom",padx=15,pady=15)


PlayButton = Button(Game, text= "Descending", width=20,command=StartGameDes)
PlayButton.pack(side="bottom",padx=15,pady=15)

PlayButton2 = Button(Game, text= "Ascending ", width=20,command=StartGameAsc)
PlayButton2.pack(side="bottom",padx=15,pady=15)

Game.mainloop()

#######################################################
