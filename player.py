#still have to add show weapon and armor in inventory

class Player:
    __exp_to_lvl_up = {1: 0, 2: 100, 3: 300, 4: 600, 5: 1200, 6: 2400, 7: 5000, 8: 10000, 9: 15000, 10: 25000}

    upgrade_points = 0


    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, name, strength=8, dexterity=8, vitality=50):
        self.__name = name
        self.__lvl = 1
        self.__body = None
        self.__left_hand = None
        self.__right_hand = None
        self.experience = 0
        self.strength = strength
        self.dexterity = dexterity
        self.vitality = vitality
        self.balance = 0
        self.max_health = vitality
        self.flurry = 1
        self.power_attack = 1



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



vlad = Player('vlad')



