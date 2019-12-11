from Player import Player


class Table:
    """A user's table to put cards in play"""
    def __init__(self, player):
        self.player = player

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player):
        if not isinstance(player, Player):
            raise TypeError("Table player must be Player object")
        self.__player = player
