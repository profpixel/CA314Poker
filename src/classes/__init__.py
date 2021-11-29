from frontend import PokerApp
from backend import *

def main():
    deck = Deck()
    player = Player("John", [], 0, 10)
    deck.dist_cards([player], 2)
    app = PokerApp()
    app.player_init(deck, player)
    app.run()

if __name__ == '__main__':
    main()
