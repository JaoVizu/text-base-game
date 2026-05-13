from random import randint
from unittest import case

import config
from enemies.enemy import Enemy
from hero.hero import Hero
from ui_helper import UI


class Battle:
    def __init__(self, enemy_instance: Enemy, player_instance: Hero):
        self.enemy_instance= enemy_instance
        self.player_instance = player_instance
        pass

    def verify_if_player_and_enemy_is_alive(self)   :
        return self.player_instance.is_alive() and self.enemy_instance.is_alive()

    def get_player_choice(self, choice):
        match choice:
            case '1':
                self.player_instance.attack(self.enemy_instance)
            case '2':
                self.player_instance.inspect_inventory()
            case _: #Default case
                UI.announce(f"{self.player_instance.name.upper()}'1 - ATTACK", UI.INFO)
                UI.announce(f"{self.player_instance.name.upper()}'2 - ITEMS", UI.INFO)

    def battle_start(self):
        while self.verify_if_player_and_enemy_is_alive():
            if randint(1,2) == 1:
                #HERO'S TURN
                UI.announce(f"{self.player_instance.name.upper()}'s turn", UI.ERROR)
                UI.announce("1 - ATTACK", UI.INFO)
                UI.announce("2 - ITEMS", UI.INFO)
                choice = input()
                self.get_player_choice(choice)
                if not self.enemy_instance.is_alive():
                    return
            else:
                #SPIDER'S TURN
                self.enemy_instance.attack(self.player_instance)
                if not self.player_instance.is_alive():
                    break

            UI.announce(f'-> {self.player_instance.name} HP: {self.player_instance.hp} | {self.enemy_instance.name} HP: {self.enemy_instance.hp}', UI.INFO)

        # --- End of Battle Results ---
        if self.player_instance.is_alive():
            UI.announce(f"\nVICTORY! The {self.enemy_instance.name} has been defeated.", UI.SUCCESS)
        else:
            config.IS_GAME_OVER = True
            UI.announce("\nGAME OVER... You were slain.", UI.ERROR)





