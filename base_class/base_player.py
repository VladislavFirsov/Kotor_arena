from game_process.arsenal import Armor, Weapon


class BasePlayer:
    class Characteriscics:
        def __set_name__(self, owner, name):
            self.name = f'_{name}'

        def __get__(self, instance, owner):
            return getattr(instance, self.name)

        def __set__(self, instance, value):
            if type(value) is int:
                instance.__dict__[self.name] = value

    strength = Characteriscics()
    dexterity = Characteriscics()
    vitality = Characteriscics()
    intelligence = Characteriscics()
    wisdom = Characteriscics()

    def __init__(self, name, strength, dexterity, vitality, intelligence, wisdom):
        self.name = name
        self._body = None
        self._right_hand = None
        self._left_hand = None
        self.strength = strength
        self.dexterity = dexterity
        self.vitality = vitality
        self.intelligence = intelligence
        self.wisdom = wisdom

    def defence(self):
        return 8 + self._body.defence_bonus

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, value):
        if type(value) == Armor:
            self._body = value

    @property
    def right_hand(self):
        return self._right_hand

    @right_hand.setter
    def right_hand(self, value):
        if type(value) == Weapon:
            self._right_hand = value

    @property
    def left_hand(self):
        return self._left_hand

    @left_hand.setter
    def left_hand(self, value):
        if isinstance(value, Weapon) and self._right_hand:
            self._left_hand = value

    def __str__(self):
        return self.name

