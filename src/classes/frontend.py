from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
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

class DublinHoldEm(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1

        self.window.add_widget(Image(source="../assets/homepage.png")

        return self.window
