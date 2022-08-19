from random import randint


def flurry(player, villain):
    damage = 0
    for i in range(player.flurry + 1):
        damage += damage_from_one_hand(player, villain)
    if player.flurry == 1:
        damage -= 12
    elif player.flurry == 2:
        damage -= 8
    else:
        damage -= 4
    return damage


def power_attack(player, villain):
    if player.right_hand:
        if damage_from_one_hand(player, villain) - player.power_attack * 2 >= protection(villain):
            return damage_from_one_hand(player, villain) + player.power_attack * 4 - 2


def damage_from_one_hand(player, villain):
    damage = randint(1, 20) + player.strength + player.right_hand.hit()
    return damage if damage >= protection(villain) else 0


def protection(person):
    defence = 10 + person.dexterity + person.body.defence_bonus \
    + (person.body.dexterity_bonus if person.body.dexterity_bonus else 0)
    return defence


