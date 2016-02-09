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
		self.resources_to_keep = self.faction.resources_to_keep

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

		self.action_taken = False
		self.passed = False

		self.board = Board(self)

	def receive_income(self):
		for resource, qty in self.income.items():
			self.resources[resource] += qty

		for deal in self.board.deals:
			for resource, qty in deal.items():
				self.resources[resource] += qty

		for location in self.board.locations:
			for ability in location.abilities:
				ability.activate(self, 'begin round')

		# anything else?

	def build(self):
		# choose the location you want to buy from within this hand
		
		locations = []

		for i in reversed(range(0, len(self.hand))):
			location = self.hand[i]

			can_build_this = True

			for resource, qty in location.cost.items():
				# print self.resources[resource], qty
				if self.resources[resource] < qty:
					can_build_this = False

			if can_build_this:
				locations.append(self.hand.pop(i))


		print '  %s\'s buildable locations:' %self.name
		print '   0 - Cancel'

		for i in range(1,len(locations)+1):
			print '   %d - %s' %(i, locations[i-1].name)

		print ''
		a = input('  Build which location? ')

		if a != 0:
			location = locations.pop(a-1)
			self.hand.append(locations)

			for ability in location.abilities:
				self.action_taken = ability.activate(self, 'build')

#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################
			if self.action_taken:
				for ability in location.abilities:
					ability.activate(self, 'build_bonus')

				self.board.locations.append(location)

			for loc in self.board.locations:
				print loc.name
			for loc in self.hand:
				# print loc.name
				pass
			
			self.list_resources()

#########################################################################
#########################################################################
#########################################################################
#########################################################################
#########################################################################

		else:
			self.action_taken = False

	def make_a_deal(self):
		# choose the location from within your hand and make the deal
		
		################
		# Not done yet #
		################

		
		self.action_taken = True

	def raze_from_hand(self):
		# choose the location that will be razed from within this hand
		
		################
		# Not done yet #
		################

		
		self.action_taken = True

	def raze_opponent_location(self):
		# choose the location from the other players in the game
		# get the raze stuff and give that player a foundation and a WOOD!
		
		################
		# Not done yet #
		################

		
		self.action_taken = True

	def location_action(self):
		# choose an action from your locations to take
		
		################
		# Not done yet #
		################

		self.action_taken = True

	def base_trade(self):

		print ''
		print '   Possible trades:'
		print '    0 - Cancel'
		print '    1 - Wood'
		print '    2 - Stone'
		print '    3 - Food'
		print '    4 - Common card'
		print '    5 - Faction card'

		a = input('   Trade for what? ')

		# this is sloppy right now, should clean it up
		if a == 1:
			wood = Ability('trade', {'Workers' : 2}, {'Wood' : 1})
			wood.activate(self, 'trade')

		elif a == 2:
			stone = Ability('trade', {'Workers' : 2}, {'Stone' : 1})
			stone.activate(self, 'trade')

		elif a == 3:
			food = Ability('trade', {'Workers' : 2}, {'Food' : 1})
			food.activate(self, 'trade')

		elif a == 4:
			self.draw_common_card()

		elif a == 5:
			self.draw_faction_card()


		if a != 0:
			print '   Trade complete!'
			self.list_resources()
			self.action_taken = True

			if self.base_trade_possible():
				print ''
				print '    0 - Done trading'
				print '    1 - Trade again'
				if input('   Trade again? ') == 1:
					self.base_trade()
			self.action_taken = True

	def pass_action(self):
		# when the player passes, discard all resources and reset all action cards
		
		for resource, qty in self.resources.items():
			if self.resources_to_keep.count(resource) == 0:
				self.resources[resource] = 0

		self.list_resources()

		self.action_taken = True
		self.passed = True

	def draw_common_card(self):
		
		################
		# Not done yet #
		################

		pass

	def draw_faction_card(self):
		
		################
		# Not done yet #
		################

		pass

####################################

	def build_possible(self):

		can_build_something = False

		for location in self.hand:

			can_build_this_location = True

			for resource, qty in location.cost.items():
				if self.resources[resource] < qty:
					can_build_this_location = False

			if can_build_this_location:
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
		print ''
		print '   %s\'s resources:' % self.name
		for resource, qty in self.resources.items():
			print '    %s - %i' % (resource, qty)