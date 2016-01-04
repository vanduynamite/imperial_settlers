from game import *

# Main function of Paul's Imperial Settlers simulator

def main():
	
	game = Game()

	players = {
	'Paul': 'type',
	'Audrey': 'type',
	}

	game.run_game(players)

if __name__ == "__main__":
    main()