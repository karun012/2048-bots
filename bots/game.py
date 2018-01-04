import os

from selenium import webdriver
from selenium.webdriver.common.by import By

class Game:
    def __init__(self):
        chromedriver = "/Users/karun012/chromedriver/chromedriver"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.gameContainer = None
        print("Created game")

    def start(self):
        print("Starting game")
        self.driver.get("file:///Users/karun012/github/2048/game/index.html")
        self.gameContainer = self.driver.find_element_by_xpath('//body')
        self.gameContainer.click()

    def isOver(self):
        game_over = self.driver.find_elements(By.CSS_SELECTOR, ".game-message.game-over")
        return len(game_over) != 0

    def pressKey(self, key):
        if self.gameContainer is None:
            raise RuntimeError("Maybe you forgot to start the game?")

        self.gameContainer.send_keys(key)

    def quit(self):
        self.driver.quit()
