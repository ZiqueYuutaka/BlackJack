from tkinter import *
import tkinter.messagebox as box

class Test:
	def __init__(self, window):
		self.window = window
		self.btnGame = Button(self.window, text = 'Play the Game', command = self.PlayGame)
		self.btnGame.pack(padx=100, pady=100)

	def PlayGame(self):
		print('Play game')
		
		result = box.askquestion('Play BlackJack', 'Are you ready to play BlackJack?')
		if result == 'yes':
			self.window.destroy()
			gameWindow = Tk()
			gameWindow.title('WELCOME TO BLACKJACK')

			cardManager = CardManager.createManager(gameWindow)

			displayManager = GameDisplayManager.create(gameWindow, cardManager)

			#label = Label(gameWindow, text = 'Hello')

			#label.pack(padx = 60, pady = 50)

			#GameDisplayManager.CreateCards(gameWindow)

			menu = MenuCreator.CreateMenu(gameWindow, cardManager, displayManager)

			#GameDisplayManager.HitButton(gameWindow, label)
			#GameDisplayManager.HitButton(gameWindow)

			#buttonCreator.StandButton(gameWindow)

			gameWindow.config(menu = menu)
			gameWindow.mainloop()


if __name__ == '__main__':
	window = Tk()
	var = Test(window)
#	window.withdraw()
#	result = box.askquestion('Open', 'Open window?')
#	if result == 'yes':
#		window.deiconify()
#	else:
#		window.destroy()
	window.mainloop()
