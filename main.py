from game import *

# Main function of Paul's Imperial Settlers simulator

def main():
	
	game = Game()

	players = {
	'Paul': 'Romans',
	'Audrey': 'Egyptians',
	}

	game.run_game(players)

def test():
	resources = {
		'Workers': 0,
		'Food': 0,
		'Wood': 0,
		'Stone': 0,
		'Raze': 0,
		'Defense': 0,
		'Gold': 0,
		'Foundations': 0,
		'Victory': 0,
		}

	for resource, amount in resources.items():
		print resources[resource]

if __name__ == "__main__":
    # test()
    main()