import time
from game_process.shop import Shop


class InterfaceInteraction:
    attrs = ('strength', 'dexterity', 'vitality', 'intelligence', 'wisdom')

    @staticmethod
    def show_attributes():
        name.show_interface()
        time.sleep(1)
        name.show_features()

    def upgrade_attributes(self):
        answer = input(f'What would you like to upgrade: {self.attrs}\n'
                       f"if you don't want upgrades just type leave \n")
        while answer.lower() not in self.attrs:
            if answer.lower() == 'leave':
                return
            answer = input(f'Maybe you wrote something wrong, please try again or type leave: {self.attrs}\n')
        time.sleep(1)
        points = input(f'How many points would you like to use? Now you have {name.upgrade_points} \n'
                       f"if you don't want upgrades just type leave \n")
        if points.lower() == 'leave':
            return
        while int(points) > name.upgrade_points:
            time.sleep(1)
            points = input("You don't have so many points, please try again or type leave: \n")
            if points.lower() == 'leave':
                return
        print(f'You successfully upgraded {answer} with {points} points')
        name.upgrade_features(answer.lower(), int(points))
        return


class ShopInteraction:
    armor_names = Shop.show_armor_names(Shop)
    weapon_names = Shop.show_weapon_names(Shop)

    def go_shopping(self):
        choice = input(f'What would you like to buy: armor or weapon?\n'
                       f'for leaving just type leave \n')
        if choice.lower() == 'leave':
            return
        while choice.lower() not in ('armor', 'weapon'):
            choice = input("The program doesn't understand you, please try again or type leave: \n")
        if choice.lower() == 'leave':
            return
        if choice.lower() == 'armor':
            self._armor_interaction()
        elif choice.lower() == 'weapon':
            self._weapon_interaction()

    @classmethod
    def _armor_interaction(cls):
        time.sleep(1)
        Shop.show_armor(Shop)
        print(f'Your lvl: {name.lvl}')
        time.sleep(1)
        print(f'Your balance: {name.balance}')
        time.sleep(1)
        armor = input('Just type the name of the armor you would like to buy or leave if you want to leave: \n')
        if armor.lower() == 'leave':
            return
        while armor.lower() not in cls.armor_names:
            armor = input('You must have written something wrong, please try again: ')
            if armor == 'leave':
                return
        model = Shop.sell_armor(Shop, armor)
        if name.balance >= model.price and name.lvl >= model.lvl:
            name.buy_armor(model)
            name.equip_armor(model)
            print(f'You successfully bought and equipped {model.name}, your previous armor is now in your inventory ')
            return
        else:
            print('Sorry, not enough gold or lvl is too low')
            return

    @staticmethod
    def sell_item(name):
        name.sell_item(name)

    @classmethod
    def _weapon_interaction(cls):
        time.sleep(1)
        Shop.show_weapon(Shop)
        print(f'Your lvl: {name.lvl}')
        time.sleep(1)
        print(f'Your balance: {name.balance}')
        time.sleep(1)
        weapon = input('Just type the name of the weapon you would like to buy or leave if you want to leave: \n')
        if weapon.lower() == 'leave':
            return
        while weapon.lower() not in cls.weapon_names:
            weapon = input('You must have written something wrong, please try again: ')
            if weapon == 'leave':
                return
        model = Shop.sell_weapon(Shop, weapon)
        if name.balance >= model.price and name.lvl >= model.lvl:
            name.buy_weapon(model)
            name.equip_weapon(model)
            time.sleep(1)
            print(f'You successfully bought and equipped {model.name}, your previous weapon is now in your inventory ')
            return
        else:
            print('Sorry, not enough gold or lvl is too low')
            return

    def equip_item(self, name):
        if name.lower() in self.armor_names:
            name.equip_armor(name)
        elif name.lower() in self.weapon_names:
            name.equip_weapon(name)


class Interactions(ShopInteraction, InterfaceInteraction):
    pass


