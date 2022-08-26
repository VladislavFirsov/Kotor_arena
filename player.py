#still have to add show weapon and armor in inventory and buy/sell functions
#try to implement an automatic lvl_up if possible later
#redo upgrade_char system
from base_class.base_player import BasePlayer


class Inventory:
    inventory = [[], []]

    def add_to(self, value):
        if isinstance(value, Weapon):
            self.inventory[0].append(value)
        elif isinstance(value, Armor):
            self.inventory[1].append(value)

    def take_from(self, value):
        if isinstance(value, Weapon):
            for i in self.inventory[0]:
                if value == i.name:
                    return self.inventory[0].pop(i)
        elif isinstance(value, Armor):
            for i in self.inventory[0]:
                if value == i.name:
                    return self.inventory[1].pop(i)

    def show_weapon(self):
        for i in self.inventory[0]:
            print(i)

    def show_armor(self):
        for i in self.inventory[1]:
            print(i)


class Player(BasePlayer):
    upgrade_points = 0
    experience = BasePlayer.Characteriscics()
    balance = BasePlayer.Characteriscics()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name):
        super().__init__(name, 8, 8, 40, 8, 8, 9)
        self.inventory = Inventory()
        self.experience = 0
        self.__lvl = 1
        self.balance = 0

    def lvl_up(self):
        if len(str(self.experience)) == 4 and self.experience % 1000 == 0 and self.__lvl <= 10:
            self.upgrade_points += 3
            self.__lvl += 1

    def __check_points(self):
        return self.upgrade_points > 0

    def upgrade_chars(self, char):
        if self.__check_points():
            if char == 'strength':
                self.strength += 1
            elif char == 'dexterity':
                self.dexterity += 1
            elif char == 'vitality':
                self.vitality += 10
            elif char == 'intelligence':
                self.intelligence += 1
            else:
                self.wisdom += 1
                self.force_points += 3
        self.upgrade_points -= 1

    def show_chars(self):
        print(f'strength: {self.strength}\nvitality: {self.vitality}\ndexterity: {self.dexterity}\n'
              f'intelligence: {self.intelligence}\nwisdom: {self.wisdom}')






