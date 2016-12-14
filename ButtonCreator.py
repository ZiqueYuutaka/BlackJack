from tkinter import *
import GameLogic
class Creator:
	def __init__(self, root):
		self.root = root
		self.cards = []
		self.cardIndex = 0
		self.CreateCards()
		self.StandButton()
		self.HitButton()		

	def HitButton(self):

		def Hit():
			print('Dealer deals new card')
			suit = GameLogic.GetSuit()
			rank = GameLogic.GetRank()
			lblStr = rank + ' of ' + suit
			#Check created card with cards in hand
			print(lblStr)
			self.cards[self.cardIndex].config(text = lblStr)
			self.cardIndex += 1
			#label.config(text = lblStr)
		btn = Button(self.root, text = 'HIT ME!', command = Hit)
		btn.pack(side = BOTTOM, padx = 60, pady = 20)
	#	return btn

	def StandButton(self):
		def Stand():
			print('Standing with current hand')
		btn = Button(self.root, text = 'STAND!', command = Stand)
		btn.pack(side = BOTTOM, padx = 60, pady = 20)
	#	return btn

	def CreateCards(self):
		
		i = 0
		while i < 5:
			btn = Button(self.root, height=15, width=20)
			btn.pack(side = LEFT, padx = 10, pady = 10)
			self.cards.append(btn)
			i+=1

def create(root):
	Creator(root)