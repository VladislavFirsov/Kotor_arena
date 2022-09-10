from random import randint


class Abilities:
    @classmethod
    def calculate_modifier(cls, feature):
        return ((feature - 10) // 2) + 1

    def strong_attack(self):
        return randint(1, 20) + self.calculate_modifier(self.strength)

    def flurry(self):
        return randint(1, 20) + self.calculate_modifier(self.dexterity)

    def force_push(self):
        return randint(1, 20) + self.calculate_modifier(self.intelligence)

    def force_lightning(self):
        return randint(1, 20) + self.calculate_modifier(self.wisdom)





