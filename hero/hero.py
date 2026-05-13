from enemies.enemy import Enemy
import inventory.inventory as Inventory
from ui_helper import UI
from weapon.weapon import Weapon

class Hero:
    def __init__(self,
                 inventory: Inventory,
                 equipped_weapon: Weapon,
                 level: int = 0,
                 hp: int = 100,
                 name :str = 'Moramboulous',
                 base_dmg: int = 3,
                 xp: int = 0,
                 ):
        self.name = name
        self.level = level
        self.hp = hp
        self.base_dmg = base_dmg
        self.xp = xp
        self.inventory = inventory
        self.equipped_weapon = equipped_weapon

    def gain_xp(self, amount: int):
        self.xp += amount
        print(f'You gained {self.xp} XP!')

    def attack(self, enemy : Enemy ):
        if self.equipped_weapon:
            total_dmg = self.base_dmg + self.equipped_weapon.damage
        else:
            total_dmg = self.base_dmg

        enemy.hp -= total_dmg
        UI.announce(f'You hit for {total_dmg} damage!', UI.INFO)

    def inspect_inventory(self):
        self.inventory.inspect()

    def is_alive(self):
        return self.hp > 0