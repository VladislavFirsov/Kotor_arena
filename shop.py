from random import choice

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



class Arsenal:
    pass





