from tkinter import *
import MenuCreator
import ButtonCreator

window = Tk()

window.title('WELCOME TO BLACKJACK')

label = Label(window, text = 'Hello')

label.pack(padx = 60, pady = 50)

menu = MenuCreator.CreateMenu(window)

ButtonCreator.HitButton(window, label)

ButtonCreator.StandButton(window)

window.config(menu = menu)

window.mainloop()