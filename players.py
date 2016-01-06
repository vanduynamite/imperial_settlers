from factions import *
from board import *
from locations import *

# Where the player information is stored
# will include current resources, hand, special abilities, and buildings

class Player(object):

	def __init__(self, name, faction):
		
		self.name = name
		self.faction = faction
		self.income = self.faction.income

		self.resources = {
		'Workers': 0,
		'Food': 0,
		'Wood': 0,
		'Stone': 0,
		'Raze': 0,
		'Defense': 0,
		'Gold': 0,
		'Victory': 0,
		}

		self.hand = []
		self.deck = [] # evetually inherit from the faction

		self.board = Board(self)

	def buy_location(self):
		# choose the location you want to buy from within this hand
		pass

	def raze_location_from_hand(self):
		# choose the location that will be razed from within this hand
		pass

	def raze_opponent_location(self):
		# choose the location from the other players in the game
		# get the raze stuff and give that player a foundation and a WOOD!
		pass

	def use_location(self):
		# choose the location from the locations on this player's board
		pass

	def make_a_deal(self):
		# choose the location from within your hand and make the deal
		pass

	def base_trade(self):
		# perform a base trade
		pass
