#open in python 3 not 2
from tkinter import *
import tkinter.messagebox
from game import *
###################################################
#Salah's own feature to the game.
def endGame(steps, ASCENDING, fps, AMOUNT, FSCORE):
    Game = Tk()
    Game.title("it belongs in the museum")
    Game.geometry("550x400+200+200")
    steps = steps
    if ASCENDING == False:
        ASCENDING = "Ascending"
    else:
        ASCENDING = "Descending"
    sc = str(ASCENDING) + " order"
    fps = fps
    Items = AMOUNT
    score = FSCORE
    blank = "--------------------------------------"


    w = Label(Game, text="GAME OVER", fg="red", font=("Helvetica",25))
    w.pack()

    Game.label = Label (Game, text= "Your frames per seconds where: " )
    Game.label.pack()

    Game.label = Label (Game, text= fps, fg="red" )
    Game.label.pack()

    Game.label = Label (Game, text=blank, fg="red")
    Game.label.pack()

    Game.label = Label (Game, text= "You collected a total of: " )
    Game.label.pack()

    Game.label = Label (Game, text=Items, fg="red")
    Game.label.pack()
    
    Game.label = Label (Game, text=blank, fg="red")
    Game.label.pack()

    Game.label = Label (Game, text= "you took a total steps of: " )
    Game.label.pack()
    
    Game.label = Label (Game, text= steps, fg="red" )
    Game.label.pack()

    Game.label = Label (Game, text=blank, fg="red")
    Game.label.pack()

    Game.label = Label (Game, text= "your items where sorteded in " )
    Game.label.pack()
    
    Game.label = Label (Game, text= sc, fg="red" )
    Game.label.pack()

    Game.label = Label (Game, text=blank, fg="red")
    Game.label.pack()

    Game.label = Label (Game, text= "your Total score is: " )
    Game.label.pack()
    
    Game.label = Label (Game, text= score, fg="red" )
    Game.label.pack()

    QuitButton = Button(Game, text= "Quit", width=20,command=Game.destroy)
    QuitButton.pack(side="bottom",padx=15,pady=15)

    Game.mainloop()
###################################################



