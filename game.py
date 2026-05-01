import random

import config
from enemies.enemy import Enemy
from enemies.spider import Spider
from hero.hero import Hero
from inventory.inventory import Inventory

hero = Hero()
inventory = Inventory()


def battle():
    spider = Spider()
    print('********** BATTLE STARTED **********')

    while hero.is_alive() or spider.is_alive():
        print(f"{hero.name} attack - 1 || items - 2")
        choice = input()
        if choice == '1':
            print(f'{hero.name} HP {hero.hp}')
            print(f'{spider.name} HP {spider.hp}')
            #Randomize who attacks first
            #1 for hero ||| 2 for enemy
            if random.randint(1, 2) == 1:
                #hero attack
                hero.attack(spider)
            else:
                #enemy attack
                spider.attack(hero)

def select_weapon():
    print('To battle those enemies you need a weapon.')
    print('Take this BOW and 5 ARROWS')
    inventory.weapon = 'BOW'
    inventory.ammo = 5

def introduction():
    print('Welcome to my text based game! Like in the old times!!')
    print('Now imagine you are in the medieval era. You\'re just a normal person walking')
    print('But something is wrong in the whole city! People are running and screaming, the sky is grey,'
          ' and in the horizon u see a lot of enemies approaching')
    print('Well, what do u do now?')
    print('First we need to know your hero name, tell me what is it:')
    hero_name = input('Input here your hero name: ')
    hero.name = hero_name
    print(f'WELCOME {hero.name.upper()}! Let\'s start your adventure!')
    print(f'You are at level {hero.level}')


def game():
    introduction()
    select_weapon()
    battle()