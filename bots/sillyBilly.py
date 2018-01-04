import random
import sys
import traceback
from time import sleep

from selenium.webdriver.common.keys import Keys

from game import Game

keys = [Keys.ARROW_UP, Keys.ARROW_DOWN, Keys.ARROW_LEFT, Keys.ARROW_RIGHT]

game = Game()
game.start()
try:
    while not game.isOver():
        keyToPress = random.choice(keys)
        game.pressKey(keyToPress)
        sleep(0.2)
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('Oh no!')
    traceback.print_exception(exc_type, exc_value, exc_traceback)
finally:
    game.quit()
