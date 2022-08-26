class BasePlayer:
    class Characteriscics:
        def __set_name__(self, owner, name):
            self.name = f'__{name}'

        def __get__(self, instance, owner):
            return getattr(instance, self.name)

        def __set__(self, instance, value):
            if type(value) is int and value > 0:
                instance.__dict__[self.name] = value

    strength = Characteriscics()
    dexterity = Characteriscics()
    vitality = Characteriscics()
    intelligence = Characteriscics()
    wisdom = Characteriscics()
    force_points = Characteriscics()

    def __init__(self, name, strength, dexterity, vitality, intelligence, wisdom, force_points):
        self.__name = name
        self.__body = None
        self.__right_hand = None
        self.__left_hand = None
        self.strength = strength
        self.dexterity = dexterity
        self.vitality = vitality
        self.force_points = force_points
        self.intelligence = intelligence
        self.wisdom = wisdom

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value):
        if isinstance(value, Armor):
            self.__body = value

    @property
    def right_hand(self):
        return self.__right_hand

    @right_hand.setter
    def right_hand(self, value):
        if isinstance(value, Weapon):
            self.__right_hand = value

    @property
    def left_hand(self):
        return self.__left_hand

    @left_hand.setter
    def left_hand(self, value):
        if isinstance(value, Weapon) and self.__right_hand:
            self.__left_hand = value

    def __str(self):
        return self.__name