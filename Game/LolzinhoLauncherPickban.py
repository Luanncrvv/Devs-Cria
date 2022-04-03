from pyautogui import *
import pyautogui
from time import sleep

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def check_aceitar_partida():
    aceitar_partida = pyautogui.locateOnScreen('PickGame\\ImageLolzinho\\aceitar_partida1080p.png')

    if aceitar_partida != None:
        click(aceitar_partida.left, aceitar_partida.top)
        return True
    return False

def check_adclane_ban():
    adc_lane_ban = pyautogui.locateOnScreen('PickGame\\ImageLolzinho\\10.png')   #confidence=0.5

    if adc_lane_ban != None:
        sleep(3)
        click(x=1177, y=148), sleep(0.500); sleep(1) #clica em buscar
        typewrite('Lux', interval=0.300); sleep(1)
        click(x=586, y=236), sleep(0.500); sleep(1) #clica personagem
        click(x=956, y=904), sleep(0.500); sleep(1) #bani
        return True
    return False


def main():
    while True:
        if check_aceitar_partida() or check_adclane_ban():
            sleep(2)
main()