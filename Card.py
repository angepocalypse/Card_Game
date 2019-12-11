class Card:
    """A Card Class with standard attributes"""
    def __init__(self, name: str, health: int, damage: int, mana: int,
                 tagline=None):
        self.name = name
        self.health = health
        self.damage = damage
        self.mana = mana
        if tagline == None:
            self.tagline = ""
        else:
            self.tagline = tagline

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @property
    def damage(self):
        return self.__damage

    @property
    def mana(self):
        return self.__mana

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Card name must be string")
        self.__name = name

    @health.setter
    def health(self, health):
        if not isinstance(health, int):
            raise TypeError("Card health must be int")
        self.__health = health

    @damage.setter
    def damage(self, damage):
        if not isinstance(damage, int):
            raise TypeError("Card damage must be int")
        self.__damage = damage

    @mana.setter
    def mana(self, mana):
        if not isinstance(mana, int):
            raise TypeError("Card mana must be int")
        self.__mana = mana

    def attack(self):
        """Return the outgoing attack and cost to use"""
        self.send = self.damage
        self.cost = self.mana
        print("{} attacks!".format(self.name))
        return [self.send, self.cost]

    def victim(self, receive):
        """A method that must be called whenever attacked"""
        self.health = self.health - receive
        if not self.alive():
            self.__del__()

    def alive(self):
        """Check to see if I'm still alive"""
        if self.health < 1:
            return False
        return True

    def say_tagline(self):
        print(self.tagline)

    def __del__(self):
        print("{} has been destroyed".format(self.name))
