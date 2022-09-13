from players.villain import Villain
from random import choice, randint
import time


class Arena:
    player_attacks = {'flurry': name.flurry(), 'strong attack': name.strong_attack(),
                      'force push': name.force_push(), 'force lightning': name.force_lightning()}

    @staticmethod
    def create_villain():
        if name.lvl <= 9:
            villain = Villain(choice(Villain.names), randint(10, name.strength), randint(10, name.dexterity),
                              randint(20, name.vitality), randint(10, name.intelligence), randint(10, name.wisdom))
            villain.lvl = name.lvl
            return villain
        else:
            BOSS = Villain('Forgotten Warrior', 25, 25, 200, 25, 25)
            BOSS.lvl = 10
            BOSS.right_hand = Weapon('Blade of the unknown soldier', range(7, 18), 20000, 9, True)
            BOSS.body = Armor('Armor of unknown soldier', 15, 20000, 9)
            return BOSS

    @staticmethod
    def _is_successful_hit(player, type_of_attack):
        return player.defence() >= type_of_attack

    @classmethod
    def _player_move(cls):
        time.sleep(1)
        attack = input('Choose the type of attack: Flurry, Strong attack, Force push or Force lightning\n')
        if attack.lower() in cls.player_attacks.keys():
            print(attack, 'nice choice')
        else:
            while attack.lower() not in cls.player_attacks.keys():
                attack = input(
                    'It seems that you made a mistake, please try again: Flurry, Strong attack, Force push or Force lightning\n')
        time.sleep(1)
        print('Calculating damage...')
        time.sleep(1)
        if cls._is_successful_hit(name, cls.player_attacks[attack.lower()]):
            if name.right_hand:
                damage = name.right_hand.hit()
            else:
                time.sleep(1)
                damage = name.right_hand.hit() + name.left_hand.hit()
            print(f'The hit was successful and {villain} lost {damage} hp')
            return damage
        else:
            time.sleep(1)
            print(f'The {villain} was lucky enough to dodge your attack')
            return 0

    @classmethod
    def _villain_move(cls):
        time.sleep(1)
        print(f'The {villain} is attacking you with the {choice(villain.attack_types)}')
        if cls._is_successful_hit(name, choice((villain.flurry(), villain.strong_attack()))):
            print('You successfully blocked his attack')
            return 0
        else:
            time.sleep(2)
            if villain.right_hand:
                damage = villain.right_hand.hit()
            else:
                damage = villain.right_hand.hit() + villain.left_hand.hit()
            print(f'The {villain} succeeded and you lost {damage} hp')
            return damage

    def fight(self):
        player_lvl = name.lvl
        time.sleep(1)
        print('Welcome to the Arena!')
        time.sleep(1)
        print(f'Your opponent is {villain}, prepare to fight!')
        while name.vitality > 0 or villain.vitality > 0:
            damage_1 = self._player_move()
            villain.vitality -= damage_1
            if villain.vitality <= 0:
                exp = money = name.lvl * 100
                name.experience += exp
                name.balance += money
                name.lvl_up()
                time.sleep(1)
                print('Congratulations, you won!')
                time.sleep(1)
                print(f"You've earned {exp} experience and {money} kredits")
                if player_lvl < name.lvl:
                    time.sleep(1)
                    print('Your lvl is up')
                break
            print(f'{villain} vitality: {villain.vitality}')

            damage_2 = self._villain_move()
            name.vitality -= damage_2
            if name.vitality <= 0:
                print('Unfortunately, you lost')
                break
            print(f'Your vitality: {name.vitality}')



