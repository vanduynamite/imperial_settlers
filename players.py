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
		'Foundation' : 0,
		}

		self.hand = []
		self.deck = [] # evetually inherit from the faction

		self.action_taken = False
		self.passed = False

		self.board = Board(self)

	def receive_income(self):
		for resource, qty in self.income.items():
			self.resources[resource] += qty

		for deal in self.board.deals:
			for resource, qty in deal.items():
				self.resources[resource] += qty

		# any deals
		# any production cards
		# anything else?

	def build(self):
		# choose the location you want to buy from within this hand
		self.action_taken = True

	def make_a_deal(self):
		# choose the location from within your hand and make the deal
		self.action_taken = True

	def raze_from_hand(self):
		# choose the location that will be razed from within this hand
		self.action_taken = True

	def raze_opponent_location(self):
		# choose the location from the other players in the game
		# get the raze stuff and give that player a foundation and a WOOD!
		self.action_taken = True

	def location_action(self):
		# choose an action from your locations to take
		self.action_taken = True

	def base_trade(self):
		print '0 - Cancel'
		print '1 - Wood'
		print '2 - Stone'
		print '3 - Food'
		print '4 - Common card'
		print '5 - Faction card'

		a = input('Trade for what? ')

		if a!=0 and self.base_trade_possible():
			print '1 - Done trading'
			print '2 - Trade again'
			if input('') == 2:
				self.base_trade()
			self.action_taken = True

	def pass_action(self):
		# when the player passes, discard all resources and reset all action cards
		self.action_taken = True
		self.passed = True

####################################

	def build_possible(self):

		can_build_something = False

		for card in self.hand:

			can_build_this_card = True

			for resource, qty in card.cost.items():
				if self.resources[resource] < qty:
					can_build_this_card = False

			if can_build_this_card:
				can_build_something = True

		return can_build_something

	def deal_possible(self):

		can_make_deal = False

		for card in self.hand:
			if card.deal != {}:
				can_make_deal = True

		return can_make_deal

	def raze_from_hand_possible(self):

		can_raze = False

		if self.resources['Raze'] > 0:
			for card in self.hand:
				if card.raze != {}:
					can_raze = True

		return can_raze

	def raze_opponent_location_possible(self):

		can_raze = False

		################################################
		# this one will need to be done a little later #
		################################################

		return can_raze

	def location_action_possible(self):

		can_take_action = False

		for location in self.board.locations:
			for action in location.abilities:
				if action.trigger == 'action' and action.available == True:
					
					can_afford = True

					for resource, qty in action.resources_in.items():
						if self.resources[resource] < qty:
							can_afford = False
					
					if can_afford:
						can_take_action = True

		return can_take_action

	def base_trade_possible(self):
		if self.resources['Workers'] > 1:
			return True
		else:
			return False

	def check_actions(self):
		# check to see which actions this player can take

		actions = [{'Pass' : self.pass_action}]

		if self.build_possible():
			actions.append({'Build' : self.build})

		if self.deal_possible():
			actions.append({'Make a Deal' : self.make_a_deal})

		if self.raze_from_hand_possible():
			actions.append({'Raze from Hand' : self.raze_from_hand})

		if self.raze_opponent_location_possible():
			actions.append({'Raze Opponent Location' : self.raze_opponent_location})

		if self.base_trade_possible():
			actions.append({'Base Trade' : self.base_trade})

		return actions

	def list_resources(self):
		print '   %s\'s resources:' % self.name
		for resource, qty in self.resources.items():
			print '    %s - %i' % (resource, qty)