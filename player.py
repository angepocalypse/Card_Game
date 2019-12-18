from Deck import Deck


class Player:
    '''Player class'''
    def __init__(self, player_name, user_id):
        self.name = player_name
        self.id = user_id
        self.decks = []
        self.decks.append(Deck(player_name, "{}'s Deck".format(player_name)))

    def new_deck(self, deck_name):
        '''Adds a new deck to the player instance'''
        self.decks.append(Deck(self.name, deck_name))
