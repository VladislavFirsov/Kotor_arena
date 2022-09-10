from base_class.base_player import BasePlayer
from base_class.abilities import Abilities


class Villain(BasePlayer, Abilities):
    names = ('Kantina Scoundrel', 'Bounty Hunter', 'Sinister Killer')
    lvl = 1
    attack_types = ('flurry', 'strong attack', 'force push', 'force lightning')
