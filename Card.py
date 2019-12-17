''' Card Module '''
from attr_dict import ATTR_DICT

class Card:
    '''A Card Class with standard attributes'''
    def __init__(self, init_dict: dict):
        if not isinstance(init_dict, dict):
            raise TypeError("Card object must be created with dictionary")
        self.attributes = {}
        for key, value in init_dict.items():
            self.attr_helper(key, value)

    def attr_helper(self, key, value):
        '''Helper function to check attribute dict has correct types'''
        if key not in ATTR_DICT.keys():
            raise TypeError("key in card initialization dict not recognized")
        if not isinstance(value, ATTR_DICT[key]):
            raise TypeError("Cannot initialize card. {} must be type {}".format(
                key, ATTR_DICT[key]))
        self.attributes[key] = value

    def attack(self):
        '''Return the outgoing attack and cost to use'''
        send = self.attributes['damage']
        cost = self.attributes['mana']
        print("{} attacks!".format(self.attributes['name']))
        return [send, cost]

    def victim(self, receive):
        '''A method that must be called whenever attacked'''
        self.attributes['health'] = self.attributes['health'] - receive
        if not self.alive():
            self.__del__()

    def alive(self):
        '''Check to see if I'm still alive'''
        if self.attributes['health'] < 1:
            return False
        return True

    def say_tagline(self):
        '''Return tagline'''
        print(self.attributes['tagline'])

    def __del__(self):
        print("{} has been destroyed".format(self.attributes['name']))
