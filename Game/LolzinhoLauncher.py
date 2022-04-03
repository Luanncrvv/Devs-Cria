from pyautogui import *
import pyautogui
from time import sleep
import keyboard


def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()


def check_screen():
    button_pos = pyautogui.locateOnScreen('PickGame\\ImageLolzinho\\aceitar_partida1080p.png', confidence=0.7)

    if button_pos != None:
        click(button_pos.left, button_pos.top)
        return True
    return False

def pare():

    while True:
        if keyboard.read_key() == "f10":
            print("You pressed p")
            sys.exit()



def main():
    while True:
        if check_screen() or pare():
            print('Aceite a partida')
            sleep(6)

main()