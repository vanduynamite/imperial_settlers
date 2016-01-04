# Where the game is run


class Game(object):
	def __init__(self):
		self.num_players = 0
		self.num_rounds = 5
		self.players = []

		self.round = 0


	def run_game(self, players):

		self.players = players

		print self.players