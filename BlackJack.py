from tkinter import *
import MenuCreator
import GameDisplayManager
import CardManager
import GameLogic

window = Tk()

window.title('WELCOME TO BLACKJACK')

cardManager = CardManager.createManager(window)

displayManager = GameDisplayManager.create(window, cardManager)

#label = Label(window, text = 'Hello')

#label.pack(padx = 60, pady = 50)

#GameDisplayManager.CreateCards(window)

menu = MenuCreator.CreateMenu(window, cardManager, displayManager)

#GameDisplayManager.HitButton(window, label)
#GameDisplayManager.HitButton(window)

#buttonCreator.StandButton(window)

window.config(menu = menu)

window.mainloop()