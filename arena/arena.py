from players.player import Player
from players.villain import Villain
from random import choice, randint
from shop.arsenal import Armor, Weapon
import time

#import player from final module, attack of player and villain is doing twice, idk why, getting error after return none
#of classmethod functions
vlad = Player('vlad', 0, 0, 1)


class Arena:
    player_attacks = {'flurry': vlad.flurry(), 'strong attack': vlad.strong_attack(),
                      'force push': vlad.force_push(), 'force lightning': vlad.force_lightning()}

    @staticmethod
    def create_villain():
        villain = Villain(choice(Villain.names), randint(10, vlad.strength), randint(10, vlad.dexterity),
                          randint(10, vlad.vitality), randint(10, vlad.intelligence), randint(10, vlad.wisdom))
        villain.lvl = vlad.lvl
        return villain

    @staticmethod
    def _is_successful_hit(player, type_of_attack):
        return player.defence() >= type_of_attack

    @classmethod
    def _player_move(cls):
        attack = input('Choose the type of attack: Flurry, Strong attack, Force push or Force lightning\n')
        if attack.lower() in cls.player_attacks.keys():
            print(attack, 'nice choice')
        else:
            while attack.lower() not in cls.player_attacks.keys():
                attack = input(
                    'It seems that you made a mistake, please try again: Flurry, Strong attack, Force push or Force lightning\n')
        time.sleep(2)
        print('Calculating damage...')
        time.sleep(2)
        if cls._is_successful_hit(vlad, cls.player_attacks[attack.lower()]):
            if vlad.right_hand:
                damage = vlad.right_hand.hit()
            else:
                time.sleep(2)
                damage = vlad.right_hand.hit() + vlad.left_hand.hit()
            print(f'The hit was successful and {villain} lost {damage} hp')
            return damage, True
        else:
            time.sleep(2)
            print(f'The {villain} was lucky enough to dodge your attack')

    @classmethod
    def _villain_move(cls):
        time.sleep(2)
        print(f'The {villain} is attacking you with the {choice(villain.attack_types)}')
        time.sleep(1)
        if cls._is_successful_hit(vlad, choice((villain.flurry(), villain.strong_attack(), villain.force_push(),
                                                villain.force_lightning()))):
            print('You successfully blocked his attack')
        else:
            time.sleep(2)
            if villain.right_hand:
                damage = villain.right_hand.hit()
            else:
                damage = villain.right_hand.hit() + villain.left_hand.hit()
            print(f'The {villain} succeeded and you lost {damage} hp')
            return damage, True

    def fight(self):
        while vlad.vitality > 0 or villain.vitality > 0:
            if self._player_move()[1]:
                villain.vitality -= self._player_move()[0]
                print(f'villain hp: {villain.vitality}')
            if self._villain_move()[1]:
                vlad.vitality -= self._villain_move()[0]
                print(f'{Player.__name__} hp: {Player.vitality}')


arena = Arena()
villain = arena.create_villain()
vlad.right_hand = villain.right_hand = Weapon('Sword', range(1, 7), 100, 1)
villain.body = vlad.body = Armor('robe', 1, 300, 1)
arena.fight()
