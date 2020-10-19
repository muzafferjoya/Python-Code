class Candidate:
	def __init__(self):
		self.score=0
	def correct(self):
		self.score+=4
	def incorrect(self):
		self.score-=1
	def evaluate(self):
		return f'You scored {self.score}'
