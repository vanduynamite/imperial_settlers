# abilities are where many things happen! only on buildings at the moment
# abilities will have a trigger, a cost (resources in), and a benefit (resources out)

class Ability(object):

	def __init__(self, trigger, resources_in, resources_out):
		self.trigger = trigger
		self.available = True

		self.resources_in = resources_in
		self.resources_out = resources_out

	def activate(self, player, trigger):
		# activations do not handle the actual BUYING (placing) of a location
		# almost everything else should go in here though
		
		if trigger != self.trigger:
			pass

		cancel = False
		for resource, amount in resources_in.items():
			if amount > player.resources[resources]:
				print "%s does not have enough %i" % player.name, resource
				cancel = True

		if cancel:
			pass

		for resource, amount in resources_in.items():
			player.resources[resource] -= amount

		for resource, amount in resources_out.items():
			player.resources[resource] += amount


