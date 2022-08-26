from random import choice


class Armor:
    def __init__(self, name, defence_bonus):
        self.name = name
        self.defence_bonus = defence_bonus
        self.dexterity_bonus = None


class Weapon:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def hit(self):
        return choice(self.damage)










