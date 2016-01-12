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
		print 'Begin the game!'

		# every player gets 2 common cards and 2 faction cards

	def lookout_phase(self):
		print '  Lookout phase, round %i' % self.round

		# every player gets one faction card to start

		# lay out players + 1 common cards
		# loop through player order and have them choose one each

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

		# un-pass everyone
		for player in self.turn_order:
			player.passed = False

		# while all players have not passed, circle around taking turns
		for player in self.turn_order:
			if not(player.passed):
				print '%s\'s actions: ' %player.name, player.check_actions()
				#player.list_resources()

		print ' End round %i!' % self.round

	def end_game(self):
		# determine victor...?
		print 'End the game?'

	def list_players(self):
		for player in self.players:
			print '%s is playing as the %s' % (player.name, player.faction.name) 

	def run_game(self, players):

		# set up the players
		for name, faction in players.items():
			self.players.append(Player(name, Faction(faction)))

		self.list_players()

		self.start_game()

		for i in range(self.num_rounds):
			self.round = i + 1
			self.run_round()

		self.end_game()