from kivy.app import App
from kivy.uix.widget import Widget
from backend import *


class CardDisplay(Card):
    def __init__(self, x: int, y: int, *args, **kwargs):
        super().__init__
        self.x = x
        self.y = y

    def draw(self):
        """
        Draw card to screen
        """


class PlayerDisplay(Player):
    def __init__(self, x: int, y: int, *args, **kwargs):
        super().__init__
        self.x = x
        self.y = y

    def draw(self):
        """
        Draw player to screen
        """


class PotDisplay(Pot):
    def __init__(self, x: int, y: int, *args, **kwargs):
        super().__init__
        self.x = x
        self.y = y

    def draw(self):
        """
        Draw pot to screen
        """


class DublinHoldEm(Widget):
    pass


class PokerApp(App):
    def build(self):
        return DublinHoldEm()
