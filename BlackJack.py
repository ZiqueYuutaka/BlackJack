from tkinter import *
import MenuCreator
import ButtonCreator

window = Tk()

window.title('WELCOME TO BLACKJACK')

ButtonCreator.create(window)

#label = Label(window, text = 'Hello')

#label.pack(padx = 60, pady = 50)

#buttonCreator.CreateCards(window)

menu = MenuCreator.CreateMenu(window)

#ButtonCreator.HitButton(window, label)
#buttonCreator.HitButton(window)

#buttonCreator.StandButton(window)

window.config(menu = menu)

window.mainloop()