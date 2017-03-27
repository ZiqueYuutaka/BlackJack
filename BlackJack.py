from tkinter import *
import MenuCreator
import GameDisplayManager
import CardManager
import GameLogic

import tkinter.messagebox as msgbox
#This is my change here that I want to push to ZiqueYuutaka
#This is my change from ZiqueYuutaka BlackJack
#This is a test of the bat file on iwoodferren machine
class BlackJackGame:
	def __init__(self, window):
		self.window = window
		self.window.title('WELCOME TO BLACKJACK')
		self.CreateMenuButtons()
		self.ConfigureButtons()
		self.cardManager = ''
		self.displayManager = ''
		self.fundsLabel = ''

	def PlayGame(self):
		print('Play game')
		
		result = msgbox.askquestion('Play BlackJack', 'Are you ready to play BlackJack?')
		if result == 'yes':
			if GameLogic.funds <= 0:
				GameLogic.box.showinfo('No Funds', 'You have NO FUNDS.\nPlease hit restart')
			else:
				gameWindow = Tk()
				gameWindow.title('BLACKJACK')

				self.cardManager = CardManager.createManager(gameWindow)

				self.displayManager = GameDisplayManager.create(gameWindow, self.cardManager)

	def DisplayFunds(self):
		fundsWindow = Tk()
		fundsWindow.title('Your available funds')
		self.fundsLabel = Label(fundsWindow)
		self.SetLabel()

	def SetLabel(self):
		fundStr = 'You have:\n'
		fontSize = 20
		if GameLogic.funds <= 0:
			self.fundsLabel.config(text = fundStr + '$0.00', font=fontSize)
			self.fundsLabel.pack(padx = 60, pady = 50)
		else:
			self.fundsLabel.config(text = fundStr + '$' + str(GameLogic.funds), font=fontSize)
			self.fundsLabel.pack(padx = 60, pady = 50)

	def Restart(self):
		result = msgbox.askquestion('Restart','Are you sure you want to reset all stats?')
		if result == 'yes':
			GameLogic.cardTotal = 0
			GameLogic.playerWins = 0
			GameLogic.playerLoses = 0
			GameLogic.funds = 1000

	def Exit(self):
		print('ByeBye!')
		result = msgbox.askquestion('Exit','Are you sure you want to Exit?')
		if result == 'yes':
			window.destroy()


	def CreateMenuButtons(self):
		self.btnGame = Button(self.window, text = 'Play the Game', command = self.PlayGame)
		self.btnFunds = Button(self.window, text = 'Display Available Funds', command = self.DisplayFunds)
		self.btnReset = Button(self.window, text = 'Restart', command = self.Restart)
		self.btnQuit =	Button(self.window, text = 'Quit', command = self.Exit)

	def ConfigureButtons(self):
		padx = 100
		pady = 10
		width = 50
		height = 2
		self.btnGame.pack(padx=padx, pady=pady)
		self.btnGame.config(width=width, height=height)
		self.btnFunds.pack(padx=padx, pady=pady)
		self.btnFunds.config(width=width, height=height)
		self.btnReset.pack(padx=padx, pady=pady)
		self.btnReset.config(width=width, height=height)
		self.btnQuit.pack(padx=padx, pady=pady)
		self.btnQuit.config(width=width, height=height)

if __name__ == '__main__':
	window = Tk()
	BlackJackGame(window)
	window.config(menu = MenuCreator.CreateMenu(window))
	window.mainloop()