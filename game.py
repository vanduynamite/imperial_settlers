from players import *


class Game(object):
	def __init__(self):
		self.num_players = 0
		self.num_rounds = 5
		self.players = []

		self.round = 0

		self.turn_order = []

	def set_turn_order(self):
		if self.turn_order == []:
			# this should be better..?
			for player in self.players:
				self.turn_order.append(player)
		else:
			a = self.turn_order.pop(0)
			self.turn_order.append(a)

	def start_game(self):
		#what do I even need to do in here?
		print 'Begin the game!'

	def lookout_phase(self):
		# do the lookout phase
		print '  Lookout phase'

	def receive_income(self):
		# get income from all sources

		for player in self.turn_order:
			player.receive_income()

		print '  Everyone gets income'

	def run_round(self):
		print ' Begin round %i!' % self.round

		self.set_turn_order()
		self.lookout_phase()
		self.receive_income()

		# while all players have not passed, circle around taking turns
		for player in self.turn_order:
			print '   %s\'s resources:' % player.name

			for resource, amount in player.resources.items():
				print '    %s - %i' % (resource, amount)

		print ' End round %i!' % self.round

	def end_game(self):
		# determine victor...?
		print 'End the game?'

	def run_game(self, players):

		# set up the players
		for name, faction in players.items():
			self.players.append(Player(name, Faction(faction)))

		# list the players
		# for player in self.players:
		# 	print '%s is playing as the %s' % (player.name, player.faction.name)

		self.start_game()

		for i in range(self.num_rounds):
			self.round = i + 1
			self.run_round()

		self.end_game()