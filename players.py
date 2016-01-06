# Where the player information is stored
# will include current resources, hand, special abilities, and buildings

class Player(object):

	def __init__(self, name, faction):
		
		self.name = name
		self.faction = faction

		self.resources = {
		'Workers': 0,
		'Food': 0,
		'Wood': 0,
		'Stone': 0,
		'Raze': 0,
		'Defense': 0,
		'Gold': 0,
		'Foundations': 0,
		'Victory': 0,
		}

		self.hand = []

		self.board = Board()

		self.deals = []

		self.common_production = []
		self.common_features = []
		self.common_actions = []

		self.faction_production = []
		self.faction_features = []
		self.faction_actions = []

