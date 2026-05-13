import random
import config
import database.game_db as db
import weapon
from battle.Battle import Battle

from enemies.spider import Spider
from hero.hero import Hero
from inventory.inventory import Inventory
from ui_helper import UI
from weapon.weapon import Weapon


weapon = Weapon(name='AXE', damage=2)
inventory = Inventory(weapon=weapon)
hero = Hero(inventory=inventory, equipped_weapon=weapon)


def battle():
    spider = Spider()
    bt_class = Battle(spider, hero)
    bt_class.battle_start()
    UI.clear_console()

# def battle():
#     spider = Spider()
#     print('********** BATTLE STARTED **********')
#
#     while hero.is_alive() and spider.is_alive():
#         #Randomize turn
#         if random.randint(1, 2) == 1:
#             #  HERO'S TURN
#             print(f"{hero.name.upper()} attack - 1 || items - 2")
#             choice = input()
#             if choice != '1' and '2':
#                 print(f"{hero.name.upper()} ATTACK - 1 || ITEMS - 2")
#                 choice = input()
#             if choice == '1':
#                 hero.attack(spider)
#             # This breaks the looping if spider dies from this attack
#             if not spider.is_alive():
#                 break
#         else:
#             # SPIDER'S TURN
#             spider.attack(hero)
#             # This breaks the looping if hero dies from this attack
#             if not hero.is_alive():
#                 break
#
#         # Print status after each round of actions
#         print(f'-> {hero.name} HP: {hero.hp} | {spider.name} HP: {spider.hp}')
#
#     # --- End of Battle Results ---
#     if hero.is_alive():
#         print(f"\nVICTORY! The {spider.name} has been defeated.")
#     else:
#         config.IS_GAME_OVER = True
#         print("\nGAME OVER... You were slain.")

def select_weapon():
    print('To battle those enemies you need a weapon.')
    UI.announce('Take this AXE', UI.INFO)
    hero.equipped_weapon = weapon
    inventory.weapon = weapon

def introduction():
    UI.announce('Welcome to my text based game! Like in the old times!!', UI.GOLD)
    print('Now imagine you are in the medieval era. You\'re just a normal person walking')
    print('But something is wrong in the whole city! People are running and screaming, the sky is grey,'
          ' and in the horizon u see a lot of enemies approaching')
    print('Well, what do u do now?')
    print('First we need to know your hero name, tell me what is it:')
    hero_name = input('Input here your hero name: ')
    hero.name = hero_name.upper()
    db.save_game(hero)
    UI.clear_console()
    UI.announce(f'WELCOME {hero.name.upper()}! Let\'s start your adventure!', UI.SUCCESS)
    print(f'You are at level {hero.level}')


def game():
    #loading exist data
    save_data =db.load_game()

    if save_data:
        hero.level, hero.hp, hero.name, hero.base_dmg, hero.xp = save_data
        UI.announce(f"WELCOME BACK {hero.name.upper()}", UI.SUCCESS)
    else:
        introduction()

    select_weapon()
    UI.clear_console()
    battle()
    UI.clear_console()
    inventory.want_to_inspect_inventory()