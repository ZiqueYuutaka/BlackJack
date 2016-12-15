from tkinter import *
import ButtonCreator

####################TEST SECTION################
#window = Tk()
#window.title('My Menu')
#window.geometry('400x400')

################################################

#menu = Menu(window) #create a menu bar to hold options
#window.config(menu = menu) #configure the window with a menu bar
def CreateMenu(window):
	
	def NewGame():
		print('New game!')
		ButtonCreator.cardManager.CreateCards()

	def Stats():
		print('Viewing Stats!')

	def About():
		print('About BlackJack')

	def Exit():
		print('ByeBye!')
		window.destroy()

	menu = Menu()
	filemenu = Menu(menu) # create a file menu
	menu.add_cascade(label='File', menu = filemenu) #when clicked File will drop down
	filemenu.add_command(label='New', command=NewGame)
	filemenu.add_command(label='Stats',command=Stats)
	filemenu.add_separator()
	filemenu.add_command(label='Exit', command=Exit)

	#create a helpmenu
	helpmenu = Menu(menu)
	menu.add_cascade(label='Help', menu=helpmenu)
	helpmenu.add_command(label='About',command=About)

	return menu


#mainloop()