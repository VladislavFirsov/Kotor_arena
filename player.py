#try to implement an automatic lvl_up if possible later
#create abilities
from base_class.base_player import BasePlayer
from arsenal.arsenal import Weapon, Armor


class Player(BasePlayer):
    class Inventory:
        inventory = [[], []]

        def add_to(self, value):
            if isinstance(value, Weapon):
                self.inventory[0].append(value)
            elif isinstance(value, Armor):
                self.inventory[1].append(value)

        def take_from(self, name):
            for bag in self.inventory:
                for item in bag:
                    if item.name == name:
                        return bag.pop(bag.index(item))

        def show_weapon(self):
            for i in self.inventory[0]:
                print(i)

        def show_armor(self):
            for i in self.inventory[1]:
                print(i)

    __upgrade_points = 0
    experience = BasePlayer.Characteriscics()
    balance = BasePlayer.Characteriscics()
    lvl = BasePlayer.Characteriscics()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name, experience, balance, lvl):
        super().__init__(name, 8, 8, 40, 8, 8, 9)
        self.inventory = Player.Inventory()
        self.experience = experience
        self.lvl = lvl
        self.balance = balance

    def lvl_up(self):
        if len(str(self.experience)) == 4 and self.experience % 1000 == 0 and self.lvl <= 10:
            self.__upgrade_points += 3
            self.lvl += 1

    def __check_points(self, number):
        return self.__upgrade_points - number >= 0

    def upgrade_chars(self, char, number):
        if self.__check_points(number):
            if char == 'strength':
                self.strength += number
            elif char == 'dexterity':
                self.dexterity += number
            elif char == 'vitality':
                self.vitality += number * 10
            elif char == 'intelligence':
                self.intelligence += number
                self.force_points += number * 3
            else:
                self.wisdom += number
        self.__upgrade_points -= number

    def show_chars(self):
        print(f'strength: {self.strength}\nvitality: {self.vitality}\ndexterity: {self.dexterity}\n'
              f'intelligence: {self.intelligence}\nwisdom: {self.wisdom}')

    @property
    def upgrade_points(self):
        return self.__upgrade_points

    def equip_weapon(self, name):
        blade = self.inventory.take_from(name)
        if blade.one_handed and self.right_hand is not None:
            self.inventory.add_to(self.right_hand)
            self.right_hand = blade
        else:
            self.inventory.add_to(self.right_hand)
            self.right_hand = blade
            self.left_hand = blade

    def equip_armor(self, name):
        armor = self.inventory.take_from(name)
        if self.body is not None:
            self.inventory.add_to(self.body)
        self.body = armor

    def sell_item(self, shop, name):
        item = self.inventory.take_from(name)
        self.balance += item.price // 2
        #add shop logic






