from Player import Player
from PlayArea import  PlayArea


class Table:
    """A table to put two Players"""

    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.play_area1 = PlayArea(self.player_one)
        self.play_area2 = PlayArea(self.player_two)

    @property
    def player_one(self):
        return self.__player_one

    @player_one.setter
    def player_one(self, player_one):
        if not isinstance(player_one, Player):
            raise TypeError("Table player must be Player object")
        self.__player_one = player_one
    
    @property
    def player_two(self):
        return self.__player_two

    @player_two.setter
    def player_two(self, player_two):
        if not isinstance(player_two, Player):
            raise TypeError("Table player must be Player object")
        self.__player_two = player_two
