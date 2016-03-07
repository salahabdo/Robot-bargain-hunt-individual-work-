from tkinter import *
import tkinter.messagebox
#################################################
#Salah's own feature to the game.
def GameOver():
    Game = Tk()
    Game.title("it belongs in the museum")
    Game.geometry("550x400+200+200")
    w = Label(Game, text="Game Over!", fg="red", font=("Helvetica",25))
    w.pack()
    print ("HELLO")


    QuitButton = Button(Game, text= "Quit", width=20,command=QuitGame)
    QuitButton.pack(side="bottom",padx=15,pady=15)

    PlayButton = Button(Game, text= "Play Agin!", width=20,command=PlayGame)
    PlayButton.pack(side="bottom",padx=15,pady=15)

    Game.mainloop()

##################################################
GameOver()
