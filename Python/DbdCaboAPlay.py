from pyautogui import *
import pyautogui
from time import sleep


def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()


def check_screen():
    killer = pyautogui.locateOnScreen('Game\\DbdKiller.png', confidence=0.4)

    if killer != None:
        pyautogui.press('Enter')
        pyautogui.typewrite('TwitchTv: SalamandraLw')
        sleep(2)
        pyautogui.press('Enter')
        return True
    return False


def main():
    while True:
        if check_screen():
            print('Mandou a Live')
            sleep(300)


main()
