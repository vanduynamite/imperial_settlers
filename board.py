# class of the board

class Board(object):

	def __init__(self, player):
		self.player = player

		self.deals = []

		self.locations = []

		self.common_production = []
		self.common_features = []
		self.common_actions = []

		self.faction_production = []
		self.faction_features = []
		self.faction_actions = []