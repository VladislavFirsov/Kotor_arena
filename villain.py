from random import choice
from player import Player

class Villain(Player):
    __random_names = []

    def __init__(self):
        super().__init__(choice(self.__random_names), 10, 10, 50)


a = Villain()
print(a.__dict__)