from shop import Weapon, Armor, MedicalKit, MedShop
#still have to add show weapon and armor in inventory


class Characteriscics:
    def __set_name__(self, owner, name):
        self.name = f'__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Inventory:
    medkits = {'small_kit': 0, 'medium_kit': 1, 'large_kit': 2}

    def __init__(self):
        self.__inventory = [[], [], [], [], []]

    def add_to_inventory(self, entity):
        if type(entity) is MedicalKit and entity.name == 'small_kit':
            self.__inventory[0].append(entity)
        elif type(entity) is MedicalKit and entity.name == 'medium_kit':
            self.__inventory[1].append(entity)
        elif type(entity) is MedicalKit and entity.name == 'large_kit':
            self.__inventory[2].append(entity)
        elif type(entity) is Weapon:
            self.__inventory[3].append(entity)
        elif type(entity) is Armor:
            self.__inventory[4].append(entity)

    def show_medkits(self):
        for i in range(3):
            print(f'{list(self.medkits.keys())[i]} {len(self.__inventory[i])}')


    def use_medkit(self, player, medkit):
        if medkit in self.medkits.keys() and len(self.__inventory[self.medkits[medkit]]) != 0:
            player.vitality += self.__inventory[self.medkits[medkit]][0].restoration
            if player.vitality > player.max_health:
                player.vitality = player.max_health
        del self.__inventory[self.medkits[medkit]][-1]

    @property
    def inventory(self):
        return self.__inventory

class Player:
    __exp_to_lvl_up = {1: 0, 2: 100, 3: 300, 4: 600, 5: 1200, 6: 2400, 7: 5000, 8: 10000, 9: 15000, 10: 25000}

    upgrade_points = 0

    strength = Characteriscics()
    dexterity = Characteriscics()
    vitality = Characteriscics()
    balance = Characteriscics()
    experience = Characteriscics()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Player, cls).__new__(cls)
        return cls.instance

    def __init__(self, name, strength=8, dexterity=8, vitality=50):
        self.__name = name
        self.__lvl = 1
        self.__body = None
        self.__left_hand = None
        self.__right_hand = None
        self.experience = 0
        self.inventory = Inventory()
        self.strength = strength
        self.dexterity = dexterity
        self.vitality = vitality
        self.balance = 0
        self.max_health = vitality
        self.flurry = 1
        self.power_attack = 1

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

    def buy_medkit(self, shop, medkit):
        temp = shop.sell_medkit(medkit)
        if self.balance >= temp.price:
            self.inventory.add_to_inventory(temp)
            self.balance -= temp.price

    def lvl_up(self):
        self.upgrade_points += 3
        self.__lvl += 1

    def __check_points(self):
        return self.upgrade_points > 0

    def upgrade_dexterity(self):
        if self.__check_points():
            self.dexterity += 1
            self.upgrade_points -= 1

    def upgrade_strength(self):
        if self.__check_points():
            self.strength += 1
            self.upgrade_points -= 1

    def upgrade_vitality(self):
        if self.__check_points():
            self.vitality += 15
            self.upgrade_points -= 1

    def show_lvl(self):
        print(f'{self.__lvl}  {self.experience}/{self.__exp_to_lvl_up[self.__lvl + 1]}')

    def show_chars(self):
        print(f'strength: {self.strength}\nvitality: {self.vitality}\ndexterity: {self.dexterity}')






