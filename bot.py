from time import sleep
import pyautogui as auto
from os import system





positions = ((817, 649), (917, 649), (1017, 649), (1117, 649))
letters = ('a', 's', 'd', 'f')
counter = 0

while True:
    index = counter % 4
    position = positions[index]
    color = auto.pixel(*position)
    if color == (17, 17, 17):
        # auto.press(letters[index])
        auto.moveTo(*position, duration=0.05)
        auto.click()
    sleep(0.05)
    system('cls')
    counter += 1