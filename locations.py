from abilities import *
import csv

# buildings will have costs, razes, deals, and abilities
# see abilities for more

class Location(object):

	def __init__(self, datarow):

		self.datarow = datarow

		self.name = datarow['Name']
		self.faction = datarow['Faction']
		self.color = datarow['Color']
		self.trigger = datarow['Trigger']
		self.limit = datarow['Trigger Limit']

		self.cost = self.get_resource_data(datarow, 'Cost')
		self.raze = self.get_resource_data(datarow, 'Raze')
		self.buildbonus = self.get_resource_data(datarow, 'BB')
		self.deal = self.get_resource_data(datarow, 'Deal')
		self.res_in = self.get_resource_data(datarow, 'In')
		self.res_out = self.get_resource_data(datarow, 'Out')


		self.abilities = []

		self.abilities.append(Ability('build', self.cost, {}))

		if self.deal != {}:
			self.abilities.append(Ability('make_a_deal', {'Food':1}, self.deal))

		if self.raze != {}:
			self.abilities.append(Ability('raze_from_hand', {'Raze':1}, self.raze))

		if self.buildbonus != {}:
			self.abilities.append(Ability('build_bonus', {}, self.buildbonus))

		if self.trigger == 'Production':
			self.abilities.append(Ability('begin_round', self.res_in, self.res_out))

		if self.trigger == 'Raze':
			self.abilities.append(Ability('raze', self.res_in, self.res_out))

		if self.trigger == 'Action':
			self.abilities.append(Ability('action', self.res_in, self.res_out))

		if 'Build' in self.trigger:
			self.abilities.append(Ability(self.trigger, self.res_in, self.res_out))

	def get_resource_data(self, datarow, category):

		category_data = {}

		for category_resource, qty in datarow.items():

			if qty != '' and category == category_resource[0:category_resource.find(' ')]:
				resource = category_resource[category_resource.find(' ')+1:len(category_resource)]

				category_data[resource] = qty
				if qty.isdigit():
					category_data[resource] = int(qty)


		return category_data


def LoadCommonLocations():

	# this will load all the cards from the deck
	csv_file = open('card_list.csv', 'rb')
	rdr = csv.reader(csv_file, delimiter=',', quotechar='"')
	loc_list = [x for x in rdr]

	# check the headers?
	headers = loc_list[0]
	
	# go down the list of cards
	# for each column, store in the appropriate place

	common_locations = []
	datarow = {}

	for row in range(1, len(loc_list)):

		for col in range(0,len(headers)):

			header = headers[col]
			datarow[header] = loc_list[row][col]

		common_locations.append(Location(datarow))

	return common_locations

	# for location in common_locations:
	# 	print location.name, ': ', location.trigger

	# 	for ability in location.abilities:
	# 		print ' ', ability.trigger
	# 		print '    spend: ', ability.resources_in
	# 		print '    get:   ', ability.resources_out

	# 	print ''
	# 	print ''
		# print '   Cost: ' ,location.cost
		# print '   Raze: ', location.raze
		# print '   BB:   ', location.buildbonus
		# print '   Deal: ', location.deal