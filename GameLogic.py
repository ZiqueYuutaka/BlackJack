import random

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

#def CheckHand():
