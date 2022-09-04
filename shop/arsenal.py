from random import choice


class Armor:
    def __init__(self, name, defence_bonus, price, lvl):
        self.name = name
        self.defence_bonus = defence_bonus
        self.price = price
        self.lvl = lvl

    def __str__(self):
        return f'name: {self.name}, defence_bonus: {self.defence_bonus}, price: {self.price} kredits, lvl: {self.lvl}'


class Weapon:
    def __init__(self, name, damage: range, price, lvl, one_handed=True):
        self.name = name
        self.damage = damage
        self.one_handed = one_handed
        self.price = price
        self.lvl = lvl

    def hit(self):
        return choice(self.damage)

    def __str__(self):
        return f'name: {self.name}, damage: {self.damage[0], self.damage[-1]}, price: {self.price} credits, lvl: {self.lvl}, {"one_handed" if self.one_handed else "double_handed"}'
