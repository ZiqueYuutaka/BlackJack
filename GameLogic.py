import random
import tkinter.messagebox as box

playerName = ''
playerWins = 0
playerLoses = 0

cardTotal = 0
funds = 1000.00
isGameOver = 'false'

def GetSuit():
	suit = random.randint(1, 4)
	if(suit == 1):
		return 'Diamonds'
	elif(suit == 2):
		return 'Hearts'
	elif(suit == 3):
		return 'Clubs'
	else:
		return 'Spades'

def GetRank():
	rank = random.randint(1, 13)
	if(rank == 1):
		return 'Ace'
	elif(rank == 13):
		return 'King'
	elif(rank == 12):
		return 'Queen'
	elif(rank == 11):
		return 'Jack'
	else:
		return str(rank)

def GetRankNum(rankStr):
	if(rankStr == 'King'):
		return 10
	elif(rankStr == 'Queen'):
		return 10
	elif(rankStr == 'Jack'):
		return 10
	else:
		return int(rankStr)

def CheckHand(card, cardList):

	for ownedCard in cardList:
		if card == ownedCard.cget('text'):
			return 'match'

def isOver(score):
	if score > 21:
		return 'true'
	else:
		print('Not over')


