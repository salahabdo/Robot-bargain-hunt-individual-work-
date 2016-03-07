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
def StartGame():
    TIME = (Game.TIME.get())
    
    LOOP = Game.LOOP.get()
    start(TIME)
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

PlayButton = Button(Game, text= "Play", width=20,command=StartGame)
PlayButton.pack(side="bottom",padx=15,pady=15)

Game.mainloop()

#######################################################
