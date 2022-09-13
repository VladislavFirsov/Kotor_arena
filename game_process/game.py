import sqlite3
from players.player import Player
from game_process.shop import Shop
#inventory not saving
#add armor and weapon through shop method sell in the final file

class GameCommands:
    player = None
    commands = ['fight', 'buy', 'sell', 'equip', 'upgrade']

    def start_new_game(self):
        player = input('Name your character: \n')
        self.player = Player(player, 10, 10, 40, 10, 10, 0, 0, 1)
        print(f'Welcome to the kotor arena {self.player}')
        return self.player

    def what_to_do(self):
        command = input('What would you like to do? \n')
        while command.lower() not in self.commands:
            command = input('Try that again please, but be more specific: \n')
        return command

    def save_game(self):
        with sqlite3.connect('database.db') as db:
            c = db.cursor()

            c.execute('INSERT INTO player VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                      [self.player.name, self.player.strength, self.player.dexterity,
                       self.player.vitality, self.player.intelligence, self.player.wisdom,
                       self.player.balance, self.player.lvl, self.player.experience,
                       self.player.body.name, self.player.right_hand.name])

    def load_game(self):
        with sqlite3.connect('database.db') as db:
            c = db.cursor()

            features = c.execute('SELECT * from player ORDER BY id DESC LIMIT 1').fetchall()
            self.player = Player(features[1], features[2], features[3],
                                 features[4], features[5], features[6],
                                 features[7], features[8], features[9])
            self.player.body = Shop.sell_armor(Shop, features[10])
            weapon = Shop.sell_weapon(Shop, features[-1])
            if not weapon.one_handed:
                self.player.right_hand = self.player.left_hand = weapon
            else:
                self.player.right_hand = weapon
            return self.player






