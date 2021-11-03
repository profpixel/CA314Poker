#!/usr/env/bin python3

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return "{} of {}".format(self.value, self.suit)


def main():
    MyCard = Card("Hearts", 4)
    print(MyCard)

if __name__ == '__main__':
    main()