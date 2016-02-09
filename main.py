from game import *

# Main function of Paul's Imperial Settlers simulator

def main():
	
	game = Game()

	players = {
	'Roland': 'Roman',
	'Lorenzo': 'Egyptian',
	'Evan': 'Japanese',
	'Josh': 'Barbarian',
	}

	game.run_game(players)

def test():

	LoadCommonLocations()	

if __name__ == "__main__":
    test()
    # main()