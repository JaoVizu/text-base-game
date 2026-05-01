# THE MAIN SCRIPT, HERE WE START AND END GAME
from game import game
import config


while True:
    if config.IS_GAME_OVER: break
    else:
        game()
