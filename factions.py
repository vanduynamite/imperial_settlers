# information about the factions (barbarians, romans, egyptians, japanese)
# not exactly sure what will go in here yet but ok

class Faction(object):

	def __init__(self, name):
		self.name = name

		egyptian_income = {
		'Workers': 3,
		'Raze': 1,
		'Defense': 1,
		'Gold': 1,
		}

		barbarian_income = {
		'Workers': 5,
		'Raze': 1,
		'Defense': 1,
		}

		roman_income = {
		'Workers': 2,
		'Wood': 1,
		'Stone': 1,
		'Raze': 1,
		'Defense': 1,
		}

		japanese_income = {
		'Workers': 4,
		'Wood': 1,
		'Raze': 1,
		'Defense': 1,
		}

		all_income = {
		'Egyptian' : egyptian_income,
		'Barbarian' : barbarian_income,
		'Roman' : roman_income,
		'Japanese' : japanese_income,
		}

		resources_to_keep = {
		'Egyptian' : 'Gold',
		'Barbarian' : 'Workers',
		'Roman' : 'Raze',
		'Japanese' : 'Food',
		}

		# this could be better, classes for each faction for instance...not now though.
		self.income = all_income[name]
		self.resources_to_keep = resources_to_keep[name]

		# along with making these classes, also give them the special abilities of the faction. and perhaps the deck and stuff too. I dunno where that's going to live eventually.