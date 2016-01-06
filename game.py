from players import *


class Game(object):
	def __init__(self):
		self.num_players = 0
		self.num_rounds = 5
		self.players = []

		self.round = 0


	def common_location_deck(self):
		# build the common location deck, probably from a text file eventually, but for now just a couple manually
		pass

	def run_game(self, players):

		for name, faction in players.items():
			self.players.append(Player(name, Faction(faction)))

		for player in self.players:
			print '%s is playing as the %s' % (player.name, player.faction.name)