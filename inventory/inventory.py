class Inventory:
    def __init__(self, weapon: str = '', ammo: int = 0, items: dict = {} ):
        self.weapon = weapon
        self.ammo = ammo
        self.items = items

    def inspect(self):
        print('****************** YOUR INVENTORY ******************')
        print(f'WEAPON ${self.weapon}')
        print(f'AMMO ${self.ammo}')
        if len(self.items) < 0:
            print(f'ITEMS ${self.items}')
        else:
            print('NAME ------------- QUANTITY')
            for item, qtd in self.items:
                print(f'{item} ---- {qtd}')
        print('*****************************************************')