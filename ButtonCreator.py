from tkinter import *


def HitButton(window):
	def Hit():
		print('Dealer deals new card')
	btn = Button(window, text = 'HIT ME!', command = Hit)
	btn.pack(side = LEFT, padx = 60, pady = 20)
#	return btn

def StandButton(window):
	def Stand():
		print('Standing with current hand')
	btn = Button(window, text = 'STAND!', command = Stand)
	btn.pack(side = LEFT, padx = 60, pady = 20)
#	return btn