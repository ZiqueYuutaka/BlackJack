from tkinter import *
import GameLogic

class CardManager: 
	def __init__(self, window):
		self.window = window
		self.cards = []
		self.acePosition = []
		self.cardIndex = 0
		self.CreateCards()

	def SetNextCard(self, cardType):
		print(cardType)
		try:
			#if it's an Ace card
			# create an ace card button
			# set the ace card button to the empty slot

			#else just add the card to the cards
			self.cards[self.cardIndex].config(text = cardType, bg ='white')
			# if card type is Ace, create an Ace card and set in to cards
			self.cardIndex += 1
		except IndexError:
			GameLogic.box.showinfo('Total cards', 'Dealt card limit reached')

	def CreateCards(self):
		i = 0
		while i < 5:
			btn = Button(self.window, height=15, width=20)
			btn.config(bg='black')
			btn.pack(side = LEFT, padx = 10, pady = 10)
			self.cards.append(btn)
			i+=1
		self.cardIndex = 0

	def NewCards(self):
		for card in self.cards:
			card.config(text = '', bg = 'black')
		self.cardIndex = 0


	def GetCards(self):
		return self.cards

	def GetCurrentCardIndex(self):
		return self.cardIndex

	def SetFirstTwo(self):
		i = 0
		while i < 2:
			suit = GameLogic.GetSuit()
			rank = GameLogic.GetRank()
			lblStr = rank + ' of ' + suit
			#Check created card with cards in hand
			#	if the card is in the hand, while no matches found get a new card
			isMatch = GameLogic.CheckHand(lblStr, self.cards)
			while isMatch == 'match':
				suit = GameLogic.GetSuit()
				rank = GameLogic.GetRank()
				lblStr = rank + ' of ' + suit
				isMatch = GameLogic.CheckHand(lblStr, self.cards)

			self.SetNextCard(lblStr)


def createManager(window):
	return CardManager(window)
		