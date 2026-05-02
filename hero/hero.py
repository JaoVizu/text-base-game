from enemies.enemy import Enemy
from inventory.inventory import Inventory
from ui_helper import UI
from weapon import Weapon

class Hero:
    def __init__(self,
                 level: int = 0,
                 hp: int = 100,
                 name :str = 'Moramboulous',
                 xp: int = 0,
                 inventory: Inventory = None,
                 equipped_weapon: Weapon = None
                 ):
        self.name = name
        self.level = level
        self.hp = hp
        self.xp = xp
        self.inventory = inventory
        self.equipped_weapon = equipped_weapon

    def gain_xp(self, amount: int):
        self.xp += amount
        print(f'You gained {self.xp} XP!')

    def attack(self, enemy : Enemy ):
        base_dmg = 3
        if self.equipped_weapon:
            total_dmg = base_dmg + self.equipped_weapon.damage
        else:
            total_dmg = base_dmg

        enemy.hp -= total_dmg
        UI.announce(f'You hit for {total_dmg} damage!', UI.SUCCESS)



    def is_alive(self):
        return self.hp > 0