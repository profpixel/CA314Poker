#!/usr/env/bin python3

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        if value == 1:
            self.value = 14
        else:
            self.value = value

    def __str__(self):
        Names = {
        11: "Jack", 12: "Queen", 13: "King", 14: "Ace",
        }
        return "{} of {}".format(Names[self.value], self.suit)
    #matches
    def __eq__(self, other):
        return self.value == other.value
    #greaterthan
    def __gt__(self, other):
        return self.value > self.other
    #lessthan
    def __lt__(self, other):
        return self.value > self.other
    
class Player:
    #hand is a list
    def __init__(self, hand, bet=0, cash=0):
        self.hand = hand
        self.bet = bet
        self.cash = cash

    # literally ignores the rules of poker, just getting a skeleton done rn
    def hand_type(self):
        sum = 0
        for card in self.hand:
            sum += card.value
        return sum


    def pay(self, payment):
        pass

def main():
    MyCard = Card("Hearts", 11)
    BadCard = Card("Diamonds", 1)
    
    PlayerOne = Player([MyCard, BadCard])
    print(PlayerOne.hand_type())

if __name__ == '__main__':
    main()