from tkinter import *
import MenuCreator

window = Tk()

window.title('My Lable example')

label = Label(window, text = 'Hello World!')

label.pack(padx = 200, pady = 50)

menu = MenuCreator.CreateMenu(window)

window.config(menu = menu)

window.mainloop()