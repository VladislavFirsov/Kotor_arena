#add a desription
class Armor:
    def __init__(self, name, defence_bonus, price, lvl, dexterity_bonus=None):
        self.name = name
        self.defence_bonus = defence_bonus
        self.dexterity_bonus = dexterity_bonus
        self.price = price
        self.lvl = lvl

    def __str__(self):
        return self.name


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
        return self.name