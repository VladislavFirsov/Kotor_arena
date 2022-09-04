class Abilities:
    @classmethod
    def calculate_modifier(cls, feature):
        return ((feature - 10) // 2) + 1

    def strong_attack(self):
        return self.calculate_modifier(self.strength)

    def flurry(self):
        return self.calculate_modifier(self.dexterity)

    def force_push(self):
        return self.calculate_modifier(self.intelligence)

    def force_lightning(self):
        return self.calculate_modifier(self.wisdom)





