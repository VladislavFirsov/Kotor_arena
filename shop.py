import sqlite3
import re
from arsenal.arsenal import Armor, Weapon


class Shop():
    @classmethod
    def get_connection(cls):
        with sqlite3.connect('shop.db') as db:
            cursor = db.cursor()
            return cursor

    def show_armor(self):
        c = self.get_connection()
        c.execute('SELECT * from armor')
        for i in c:
            print(f'name: {i[1]}, defence_bonus: {i[2]}, price: {i[3]} kredits, lvl: {i[-1]}')

    def show_weapons(self):
        c = self.get_connection()
        c.execute('SELECT * from weapon')
        for i in c:
            print(f'name: {i[1]}, damage: {i[2]}, price: {i[3]} kredits, lvl: {i[4]}, {"One_handed" if i[-1] else "Double_handed"}')


    def sell_weapon(self, name):
        c = self.get_connection()
        model = c.execute('SELECT * from weapon WHERE name = (?)', [name]).fetchone()
        damage = re.findall('[0-9]+', model[2])
        weapon = Weapon(model[1], range(int(damage[0]), int(damage[-1]) + 1), model[3], model[4], model[-1])
        return weapon

    def sell_armor(self, name):
        c = self.get_connection()
        model = c.execute('SELECT * from armor WHERE name = (?)', [name]).fetchone()
        armor = Armor(model[1], model[2], model[3], model[-1])
        return armor



















