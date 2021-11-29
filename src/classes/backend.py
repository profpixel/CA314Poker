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
        names = {
            2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten",
            11: "Jack", 12: "Queen", 13: "King", 14: "Ace",
        }
        return "{} of {}".format(names[self.value], self.suit)

    def __eq__(self, other: 'Card') -> bool:
        return self.value == other.value

    def __gt__(self, other: 'Card') -> bool:
        return self.value > other.value

    def __lt__(self, other: 'Card') -> bool:
        return self.value < other.value


class Player:
    def __init__(self, name: str, hand: List[Card], bet: int = 0, cash: int = 0):
        self.name = name
        self.hand = hand
        self.bet = bet
        self.cash = cash

    def draw(self, card: Card):
        self.hand.append(card)

    def hand_type(self) -> int:
        vals = sorted([i.value for i in self.hand])
        high_card = vals[-1]
        if len(set([i.suit for i in self.hand])) == 1 and vals == list(range(vals[0], vals[-1] + 1)):
            return 120 + high_card
        if vals[0] == vals[3] or vals[1] == vals[4]:
            return 105 + high_card
        if (vals[0] == vals[2] and vals[3] == vals[4]) or (vals[0] == vals[1] and vals[2] == vals[4]):
            return 90 + high_card
        if len(set([i.suit for i in self.hand])) == 1:
            return 75 + high_card
        if vals == [range(vals[0], vals[-1] + 1)]:
            return 60 + high_card
        if vals[0] == vals[2] or vals[1] == vals[3] or vals[2] == vals[4]:
            return 45 + high_card
        if (vals[0] == vals[1] and (vals[2] == vals[3] or vals[3] == vals[4])) or (vals[1] == vals[2] and vals[3] == vals[4]):
            return 30 + high_card
        if any([vals[i] == vals[i+1] for i in range(len(vals) - 1)]):
            return 15 + high_card
        return high_card

    def pay(self, payment: int):
        self.cash += int

    def raise_pot(self, amount: int, pot: 'Pot'):
        self.bet += amount
        pot.raise_pot(amount, self)

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
        self.cards = [Card(suit, val) for suit in ["Hearts", "Diamonds", "Spades", "Clubs"] for val in range(1, 15)]
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def dist_cards(self, players: List[Player], amount: int):
        for player in players:
            for _ in range(amount):
                player.draw(self.cards.pop())


class Pot:
    def __init__(self, value: int = 0):
        self.value = value
        self.last_raise: Player = None

    def raise_pot(self, amount: int, player: Player):
        self.value += amount
        self.last_raise = player


def main():
    deck = Deck()
    player = Player("test", [])
    deck.dist_cards([player], 5)
    print([str(i) for i in sorted(player.hand)])
    print(player.hand_type())


if __name__ == '__main__':
    main()
