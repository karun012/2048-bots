import os
import random
import traceback

from time import sleep

import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chromedriver = "/Users/karun012/chromedriver/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)
driver.get("file:///Users/karun012/github/2048/game/index.html")

gameOver = driver.find_elements(By.CSS_SELECTOR, ".game-message.game-over")
gameContainer = driver.find_element_by_xpath('//body')
keys = [Keys.ARROW_UP, Keys.ARROW_DOWN, Keys.ARROW_LEFT, Keys.ARROW_RIGHT]

try:
    while len(gameOver) == 0 & gameContainer.is_selected():
        keyToPress = random.choice(keys)
        gameContainer.click()
        gameContainer.send_keys(keyToPress)
        gameOver = driver.find_elements(By.CSS_SELECTOR, ".game-message.game-over")
        sleep(0.2)
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('Oh no!')
    traceback.print_exception(exc_type, exc_value, exc_traceback)
finally:
    driver.quit()
