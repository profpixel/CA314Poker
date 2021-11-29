from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.config import Config

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


class StartScreen(Screen):
    pass


class GameScreen(Screen):
    pass


class WinScreen(Screen):
    pass


class RootScreen(ScreenManager):
    pass


class PokerApp(App):
    def __init__(self):
        super().__init__
        self.deck = None
        self.player = None
        self.built = None


    def player_init(self, deck, player):
        self.deck = deck
        self.player = player

    def build(self):
        Config.set("graphics", "width", "1350")
        Config.set("graphics", "height", "650")
        return RootScreen()

if __name__ == '__main__':
    deck = Deck()
    player = Player("John", [], 0, 10)
    deck.dist_cards([player], 2)
    app = PokerApp()
    app.player_init(deck, player)
    app.run()
