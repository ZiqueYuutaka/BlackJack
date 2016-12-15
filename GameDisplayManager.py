from tkinter import *
import GameLogic
import CardManager
class DisplayManager:
	def __init__(self, root, cardManager):
		self.root = root
#		self.cardManager = CardManager.createManager(root)
		self.cardManager = cardManager
		self.fundsLabel = Label(self.root)
		self.SetLabel()
#		self.StandButton()
		self.HitButton()	

	def HitButton(self):

		def Hit():
			#use the IndexError Exception that is thrown
			#if self.index == 5 do not deal new card and display error window
			#else play scenario below
			if GameLogic.cardTotal > 21 or GameLogic.funds <= 0:
				GameLogic.box.showinfo('Lost', 'You have lost the game.\nPlease choose New from File menu')
			else: 
				print('Dealer deals new card')
				suit = GameLogic.GetSuit()
				rank = GameLogic.GetRank()
				lblStr = rank + ' of ' + suit
				print(GameLogic.cardTotal)
				#Check created card with cards in hand
				#	if the card is in the hand, while no matches found get a new card
				isMatch = GameLogic.CheckHand(lblStr, self.cardManager.GetCards())
				while isMatch == 'match':
					suit = GameLogic.GetSuit()
					rank = GameLogic.GetRank()
					lblStr = rank + ' of ' + suit
					isMatch = GameLogic.CheckHand(lblStr, self.cardManager.GetCards())

				#	else add the new card in to the hand
				if rank == 'Ace':
					if 11 + GameLogic.cardTotal > 21:
						GameLogic.cardTotal += 1
					else:
						GameLogic.cardTotal += 11
				else:
					GameLogic.cardTotal += GameLogic.GetRankNum(rank)
				
				self.cardManager.SetNextCard(lblStr)
				if GameLogic.isOver(GameLogic.cardTotal) == 'true':
					GameLogic.box.showinfo('Lost', 'You have lost the game.\nPlease choose New from File menu')
					GameLogic.funds -= 50
					self.SetLabel()
				elif GameLogic.cardTotal == 21:
					GameLogic.box.showinfo('WIN!!!!!', 'You have WON the game!!!!')
					GameLogic.funds += 100
					self.SetLabel()
		btn = Button(self.root, text = 'HIT ME!', command = Hit)
		btn.pack(side = BOTTOM, padx = 60, pady = 20)
		self.fundsLabel.config(font=100)
		self.fundsLabel.pack(side = BOTTOM, padx = 60, pady = 20)
	#	return btn

	def SetLabel(self):
		if GameLogic.funds <= 0:
			self.fundsLabel.config(text = '$0.00')
		else:
			self.fundsLabel.config(text = '$' + str(GameLogic.funds))

#	def StandButton(self):
#		def Stand():
#			print('Standing with current hand')
#		btn = Button(self.root, text = 'STAND!', command = Stand)
#		btn.pack(side = BOTTOM, padx = 60, pady = 20)
	#	return btn

def create(root, cardManager):
	return DisplayManager(root, cardManager)