from Deck import Deck
from Player import Player


class PlayArea:
    '''A user's play area to put cards in play'''

    def __init__(self, player, deck=None):
        self.player = player
        self.deck = deck

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player):
        if not isinstance(player, Player):
            raise TypeError("PlayArea player must be Player object")
        self.__player = player

    @property
    def deck(self):
        return self.__deck

    @deck.setter
    def deck(self, deck):
        if not isinstance(deck, Deck):
            raise TypeError("PlayArea deck must be Deck object")
        self.__deck = deck
