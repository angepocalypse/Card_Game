from Card import Card


class Deck:
    """Deck Class for storing player's cards"""
    def __init__(self, user, deck_name):
        self.cards = []
        self.user = user
        self.name = deck_name

    def add_card(self, card):
        """Adds card object to deck, input must be of type Card"""
        if not isinstance(card, Card):
            raise TypeError("add_card only takes type Card object")
        self.cards.append(card)
        print("Added {} to {}'s deck".format(card.name, self.user))

    def remove_card(self, card_name):
        """Removes card from deck if it exists"""
        for index, obj in enumerate(self.cards):
            if obj.name == card_name:
                self.cards.pop(index)
                print("Removed {} from {}'s deck".format(card_name, self.user))
                return
        print("{} not found in {}'s deck".format(card_name, self.user))
