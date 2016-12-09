from tkinter import *
import GameLogic

def HitButton(window, label):

	def Hit():
		print('Dealer deals new card')
		suit = GameLogic.GetSuit()
		rank = GameLogic.GetRank()
		lblStr = rank + ' of ' + suit
		print(lblStr)
		label.config(text = lblStr)
	btn = Button(window, text = 'HIT ME!', command = Hit)
	btn.pack(side = LEFT, padx = 60, pady = 20)
#	return btn

def StandButton(window):
	def Stand():
		print('Standing with current hand')
	btn = Button(window, text = 'STAND!', command = Stand)
	btn.pack(side = LEFT, padx = 60, pady = 20)
#	return btn