class Enemy:
    def __init__(self, name: str, hp: int, damage: int, xp_drop: int):
        self.damage = damage
        self.name = name
        self.hp = hp
        self.xp_drop = xp_drop

    def appear(self):
        print(f'A wild {self.name.upper()} has appeared!')

    def attack(self):
        print(f'{self.name} attacks for {self.damage} damage!')

    def is_alive(self):
        return self.hp > 0

