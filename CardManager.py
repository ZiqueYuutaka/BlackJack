from tkinter import *
import tkinter.messagebox as box
class CardManager: 
	def __init__(self, window):
		self.window = window
		self.cards = []
		self.cardIndex = 0
		self.CreateCards()

	def SetNextCard(self, cardType):
		print(cardType)
		try:
			self.cards[self.cardIndex].config(text = cardType)
			self.cardIndex += 1
		except IndexError:
			box.showinfo('Total cards', 'Dealt card limit reached')



	def CreateCards(self):
		
		i = 0
		while i < 5:
			btn = Button(self.window, height=15, width=20)
			btn.pack(side = LEFT, padx = 10, pady = 10)
			self.cards.append(btn)
			i+=1

	def GetCards(self):
		return self.cards

	def GetCurrentCardIndex(self):
		return self.cardIndex

def createManager(window):
	return CardManager(window)
		