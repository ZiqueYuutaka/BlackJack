from tkinter import *
import MenuCreator
import ButtonCreator
import CardManager
import GameLogic

window = Tk()

window.title('WELCOME TO BLACKJACK')

cardManager = CardManager.createManager(window)

ButtonCreator.create(window, cardManager)

#label = Label(window, text = 'Hello')

#label.pack(padx = 60, pady = 50)

#buttonCreator.CreateCards(window)

menu = MenuCreator.CreateMenu(window, cardManager)

#ButtonCreator.HitButton(window, label)
#buttonCreator.HitButton(window)

#buttonCreator.StandButton(window)

window.config(menu = menu)

window.mainloop()