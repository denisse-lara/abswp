#!/usr/bin/python
# 2048bot.py - Plays the game 2048 automatically
# following the strategy up,right,down,left

import sys, time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

# wait for the page to before playing
time.sleep(3)

game = browser.find_element(by=By.CSS_SELECTOR, value='body')
keySequence = (
    Keys.ARROW_UP,
    Keys.ARROW_RIGHT,
    Keys.ARROW_DOWN,
    Keys.ARROW_LEFT
)

seq = 0
gameOver = None
while not gameOver:
    game.send_keys(keySequence[seq])
    seq = (seq+1) % len(keySequence)

    try:
        gameOver = browser.find_element(
            by=By.CSS_SELECTOR,
            value='.game-over'
        )
    except:
        continue

score = browser.find_element(by=By.CSS_SELECTOR, value='.score-container')
print("Score: %s"%score.text)
