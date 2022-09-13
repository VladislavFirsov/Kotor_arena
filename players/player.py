from base_class.base_player import BasePlayer
from base_class.abilities import Abilities
from game_process.arsenal import Armor, Weapon


class Player(BasePlayer, Abilities):
    class Inventory:
        inventory = [[], []]

        def add_to(self, value):
            if isinstance(value, Weapon):
                self.inventory[0].append(value)
            elif isinstance(value, Armor):
                self.inventory[1].append(value)

        def take_from(self, value):
            for bag in self.inventory:
                for item in bag:
                    if item.name == value.name:
                        return bag.pop(bag.index(item))

        def show_weapon(self):
            for i in self.inventory[0]:
                print(i)

        def show_armor(self):
            for i in self.inventory[1]:
                print(i)

    __upgrade_points = 0
    __exp_to_lvl_up = 1000
    experience = BasePlayer.Characteriscics()
    balance = BasePlayer.Characteriscics()
    lvl = BasePlayer.Characteriscics()
    force_points = BasePlayer.Characteriscics()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name, strength, dexterity, vitality, intelligence, wisdom, experience, balance, lvl):
        super().__init__(name, strength, dexterity, vitality, intelligence, wisdom)
        self.inventory = Player.Inventory()
        self.experience = experience
        self.lvl = lvl
        self.balance = balance

    def lvl_up(self):
        if self.experience >= self.__exp_to_lvl_up:
            self.__upgrade_points += 3
            self.lvl += 1
            self.__exp_to_lvl_up += 1000

    def __check_points(self, number):
        return self.__upgrade_points - number >= 0

    def upgrade_features(self, feature, number):
        if self.__check_points(number):
            if feature == 'strength':
                self.strength += number
            elif feature == 'dexterity':
                self.dexterity += number
            elif feature == 'vitality':
                self.vitality += number * 10
            elif feature == 'intelligence':
                self.intelligence += number
            else:
                self.wisdom += number
        self.__upgrade_points -= number

    def show_features(self):
        print(f'strength: {self.strength}\nvitality: {self.vitality}\ndexterity: {self.dexterity}\n'
              f'intelligence: {self.intelligence}\nwisdom: {self.wisdom}')

    def show_interface(self):
        print(f'experience: {self.experience}\nbalance: {self.balance}\n lvl: {self.lvl}\n'
              f'exp for the next lvl: {self.__exp_to_lvl_up - self.experience}')
        print(f'In your inventory now: {self.inventory.show_armor()}\n{self.inventory.show_weapon()}')

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

    def sell_item(self, name):
        item = self.inventory.take_from(name)
        self.balance += item.price // 2

    def buy_weapon(self, name):
        self.inventory.add_to(name)
        self.balance -= name.price

    def buy_armor(self, name):
        self.inventory.add_to(name)
        self.balance -= name.price


