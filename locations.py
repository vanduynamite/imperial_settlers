from abilities import *

# buildings will have costs, razes, deals, and abilities
# see abilities for more

class Location(object):

	def __init__(self, name, cost, raze, deal, abilities):

		self.name = name
		self.cost = cost
		self.raze = raze
		self.deal = deal
		self.abilties = abilities

		self.abilities.append = Ability('make_a_deal', {'Food':1}, deal)
		self.abilities.append = Ability('raze_from_hand', {'Raze':1}, raze)
