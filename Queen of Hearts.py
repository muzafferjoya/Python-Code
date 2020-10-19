class Deck:
	def __init__(self):
		self.cards=['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
		self.shuffle()
	def deal(self):
		card=random.choice(self.cards)
		self.cards.remove(card)
		return f'You got {card}'
	def shuffle(self):
		random.shuffle(self.cards)
	def show(self):
		return self.cards
