from tkinter import *
import MenuCreator
import GameDisplayManager
import CardManager
import GameLogic

import tkinter.messagebox as msgbox

class BlackJackGame:
	def __init__(self, window):
		self.window = window
		self.window.title('WELCOME TO BLACKJACK')
		self.CreateMenuButtons()
		self.ConfigureButtons()
		self.cardManager = ''
		self.displayManager = ''

	def PlayGame(self):
		print('Play game')
		
		result = msgbox.askquestion('Play BlackJack', 'Are you ready to play BlackJack?')
		if result == 'yes':
#			self.window.withdraw()
			gameWindow = Tk()
			gameWindow.title('BLACKJACK')

			self.cardManager = CardManager.createManager(gameWindow)

			self.displayManager = GameDisplayManager.create(gameWindow, self.cardManager)

			#label = Label(gameWindow, text = 'Hello')

			#label.pack(padx = 60, pady = 50)

			#GameDisplayManager.CreateCards(gameWindow)

#			menu = MenuCreator.CreateMenu(gameWindow, cardManager, displayManager)

			#GameDisplayManager.HitButton(gameWindow, label)
			#GameDisplayManager.HitButton(gameWindow)

			#buttonCreator.StandButton(gameWindow)

#			gameWindow.config(menu = menu)
#			gameWindow.mainloop()

	def DisplayFunds(self):
		fundsWindow = Tk()
		fundsWindow.title('Your available funds')
		label = Label(fundsWindow, text = GameLogic.funds)

	def Restart(self):
		result = msgbox.askquestion('Restart','Are you sure you want to reset all stats?')
		if result == 'yes':
			cardManager.NewCards()
			GameLogic.cardTotal = 0
			GameLogic.playerWins = 0
			GameLogic.playerLoses = 0
			GameLogic.funds = 1000.00

	def Exit(self):
		print('ByeBye!')
		result = msgbox.askquestion('Restart','Are you sure you want to reset all stats?')
		if result == 'yes':
			window.destroy()


	def CreateMenuButtons(self):
		self.btnGame = Button(self.window, text = 'Play the Game', command = self.PlayGame)
		self.btnFunds = Button(self.window, text = 'Display Available Funds', command = self.DisplayFunds)
		self.btnReset = Button(self.window, text = 'Restart', command = self.Restart)
		self.btnQuit =	Button(self.window, text = 'Quit', command = self.Exit)

	def ConfigureButtons(self):
		self.btnGame.pack(padx=100, pady=10)
		self.btnGame.config(width=50, height=2)
		self.btnFunds.pack(padx=100, pady=10)
		self.btnFunds.config(width=50, height=2)
		self.btnReset.pack(padx=100, pady=10)
		self.btnReset.config(width=50, height=2)
		self.btnQuit.pack(padx=100, pady=10)
		self.btnQuit.config(width=50, height=2)

if __name__ == '__main__':
	window = Tk()
	BlackJackGame(window)
#	window.withdraw()
#	result = box.askquestion('Open', 'Open window?')
#	if result == 'yes':
#		window.deiconify()
#	else:
#		window.destroy()
	window.mainloop()