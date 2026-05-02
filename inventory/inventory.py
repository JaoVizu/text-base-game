from ui_helper import UI
from weapon.weapon import Weapon


class Inventory:
    def __init__(self, weapon: Weapon = None, ammo: int = 0, items: dict = {} ):
        self.weapon = weapon
        self.ammo = ammo
        self.items = items

    def inspect(self):
        UI.announce('****************** YOUR INVENTORY ******************', UI.GOLD)
        UI.announce(f'WEAPON {str(self.weapon.name)} || DAMAGE {str(self.weapon.damage)}', UI.INFO)
        if len(self.items) == 0:
            UI.announce(f'YOU DONT HAVE ANY ITEMS', UI.ERROR)
        else:
            print('NAME ------------- QUANTITY')
            for item, qtd in self.items:
                print(f'{item} ---- {qtd}')
        UI.announce('*****************************************************', UI.GOLD)

    def want_to_inspect_inventory(self):
        print(self.weapon)
        UI.announce("DO U WANT TO INSPECT YOU INVENTORY? y/s", UI.ERROR)
        choice = input('>>')
        if choice == 'y':
            self.inspect()


