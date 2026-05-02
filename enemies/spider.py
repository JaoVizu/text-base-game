from random  import randint

from enemies.enemy import Enemy
from hero.hero import Hero
from ui_helper import UI


class Spider(Enemy):

    def __init__(self):
        #Using super to fill the parents class requirements
        super().__init__(name='Spider', hp=10, damage=3, xp_drop=randint(1, 10))

    def attack(self, hero: Hero):
        hero.hp -= self.damage
        UI.announce(f'{self.name.upper()} attacked you, your HP is now {hero.hp}', UI.ERROR)
