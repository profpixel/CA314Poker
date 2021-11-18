from typing import List, Tuple
import random

class Card:
    def __init__(self, suit: str, value: int):
        self.suit = suit
        if value == 1:
            self.value = 14
        else:
            self.value = value

    def __str__(self) -> str:
        Names = {
        11: "Jack", 12: "Queen", 13: "King", 14: "Ace",
        }
        return "{} of {}".format(Names[self.value], self.suit)
    
    def __eq__(self, other: 'Card') -> bool:
        return self.value == other.value
    
    def __gt__(self, other: 'Card') -> bool:
        return self.value > self.other
    
    def __lt__(self, other: 'Card') -> bool:
        return self.value > self.other

    
class Player:
    def __init__(self, name: str, hand: List[Card], bet: int=0, cash: int=0):
        self.name = name
        self.hand = hand
        self.bet = bet
        self.cash = cash
    
    def draw(self, card: Card):
        self.hand += card

    def hand_type(self) -> Tuple[int, int]:
        """
        Calculates the value of the player's hand and returns the value of the player's hand and their highest card
        """

    def pay(self, payment: int):
        self.cash += int
    
    def raise_pot(self, amount: int):
        self.bet += amount
    
    def call(self):
        """
        Call bet
        """
    
    def check(self):
        """
        Check bet
        """
    
    def fold(self):
        """
        Fold
        """


class Deck:
    def __init__(self):
        self.cards = [[Card(suit, val) for suit in ["Hearts", "Diamonds", "Spades", "Clubs"]] for val in range(1, 15)]
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
    

    def dist_cards(self, players: List[Player], amount: int):
        for player in players:
            for _ in range(amount):
                player.draw(self.cards.pop())


class Pot:
    def __init__(self, value: int=0):
        self.value = 0
        self.last_raise: Player = None
    
    def raise_pot(self, amount: int, player: Player):
        self.pot += amount
        self.last_raise = player


def main():
    MyCard = Card("Hearts", 11)
    BadCard = Card("Diamonds", 1)
    
    PlayerOne = Player([MyCard, BadCard])
    print(PlayerOne.hand_type())

if __name__ == '__main__':
    main()
