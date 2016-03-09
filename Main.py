#open in python 3 not 2
# This WILL NOT! run in python 2
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
    start(TIME, SORT)
    Game.destroy()
def StartGameAsc():
    TIME = (Game.TIME.get())
    SORT = False
    start(TIME, SORT)
    Game.destroy()


w = Label(Game, text="It belongs in the museum!", fg="red", font=("Helvetica",25))
w.pack()

Game.label = Label (Game, text= "what frame rate would you like to run at ?")
Game.label.pack()

Game.TIME = StringVar()
Entry(Game, textvariable=Game.TIME).pack()

QuitButton = Button(Game, text= "Quit", width=20,command=QuitGame)
QuitButton.pack(side="bottom",padx=15,pady=15)


PlayButton = Button(Game, text= "Descending", width=20,command=StartGameDes)
PlayButton.pack(side="bottom",padx=15,pady=15)

PlayButton2 = Button(Game, text= "Ascending ", width=20,command=StartGameAsc)
PlayButton2.pack(side="bottom",padx=15,pady=15)

Game.mainloop()

#######################################################
