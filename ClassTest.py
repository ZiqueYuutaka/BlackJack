class Test:
	def __init__(self):
		self.cards = []
		self.index = 0

	def createList(self):
		
		while self.index < 5:
			self.cards.append("Hello")
			self.index+=1

		self.index = 0

	def printList(self):
		while self.index < 5:
			print(self.cards[self.index])
			self.index+=1

if __name__ == '__main__':
	var = Test()
	var.createList()
	var.printList()