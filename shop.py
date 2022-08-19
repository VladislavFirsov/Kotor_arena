from random import choice

class MedicalKit:
    def __new__(cls, *args, **kwargs):
        if args[0] =='small_kit' and args[1] == 15 or args[0] =='medium_kit'\
        and args[1] == 30 or args[0] =='large_kit' and args[1] == 55:
            return super().__new__(cls)

    def __init__(self, name, restoration_points, price):
        self.name = name
        self.restoration_points = restoration_points
        self.price = price

    def __str__(self):
        return f'{self.name} - restoration_points: {self.restoration_points}'

class Armor:
    def __init__(self, model, defence_bonus):
        self.model = model
        self.defence_bonus = defence_bonus
        self.dexterity_bonus = None

    def __str__(self):
        return self.model


class Weapon:
    def __init__(self, model, damage):
        self.model = model
        self.damage = damage

    def hit(self):
        return choice(self.damage)

    def __str__(self):
        return self.model


class MedShop:
    medshop = [MedicalKit('small_kit', 15, 30), MedicalKit('medium_kit', 30, 60), MedicalKit('large_kit', 55, 90)]

    def show_medkits(self):
        for i in self.medshop:
            print(f'{i.name} price: {i.price} kredits')

    def sell_medkit(self, medkit):
        for i in range(len(self.medshop)):
            if self.medshop[i].name == medkit:
                return self.medshop[i]

class Arsenal:
    pass





