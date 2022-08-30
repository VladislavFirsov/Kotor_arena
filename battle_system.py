from random import randint


class Abilities:
    def strong_attack(self):
        pass

    def flurry(self):
        pass

    def critical_strike(self):
        pass

    def force_push(self):
        pass

    def force_lightning(self):
        pass

    def force_suffocation(self):
        pass



def damage_from_one_hand(player, villain):
    damage = randint(1, 20) + player.strength + player.right_hand.hit()
    return damage if damage >= protection(villain) else 0


def protection(person):
    defence = 10 + person.dexterity + person.body.defence_bonus \
    + (person.body.dexterity_bonus if person.body.dexterity_bonus else 0)
    return defence


