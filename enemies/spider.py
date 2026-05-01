from enemies.enemy import Enemy
from hero.hero import Hero


class Spider(Enemy):

    def __init__(self):
        #Using super to fill the parents class requirements
        super().__init__(name='Spider', hp=10, damage=3)

    def attack(self, hero: Hero):
        hero.hp -= self.damage
        print(f'{self.name} attacked you, your HP is now {hero.hp}')