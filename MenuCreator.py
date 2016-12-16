from tkinter import *
import tkinter.messagebox as msgbox
#import ButtonCreator
import GameLogic

####################TEST SECTION################
#window = Tk()
#window.title('My Menu')
#window.geometry('400x400')

################################################

#menu = Menu(window) #create a menu bar to hold options
#window.config(menu = menu) #configure the window with a menu bar
def CreateMenu(window):		

	def About():
		print('About BlackJack')
		aboutWindow = Tk()
		aboutStr = """
ABOUT
To win BlackJack your goal is to obtain the
score of 21.  You are only given 5 cards
total to achieve this goal.
Jack, Queen, and King have a value of 10.
An Ace has a value of one or eleven depending.
All other cards have their rank value.
When the game begins you are given two cards.
Each time you press the HIT button a new card
will be flipped over to reveal the next card.
You continue to click HIT until you achieve a
21 score or you lose by going over 21.
NOTE
The Ace is switches between one and eleven.
If you get an Ace and if your score would 
surpass 21, that Ace will be a one. Otherwise
it will be an eleven.
You are given $1000 to start the game.
You earn $100 for each win and lose
$50 for each loss."""
		label = Label(aboutWindow, text = aboutStr)
		label.pack(side=LEFT)

	def Exit():
		print('ByeBye!')
		result = msgbox.askquestion('Exit','Are you sure you want to Exit?')
		if result == 'yes':
			window.destroy()

	menu = Menu()
	filemenu = Menu(menu) # create a file menu
	menu.add_cascade(label='File', menu = filemenu) #when clicked File will drop down
	filemenu.add_command(label='About',command=About)
	filemenu.add_separator()
	filemenu.add_command(label='Exit', command=Exit)

	return menu


#mainloop()