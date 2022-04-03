from pyautogui import *
import pyautogui
from time import sleep

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def check_aceitar_partida():
    aceitar_partida = pyautogui.locateOnScreen('PickGame\\ImageLolzinho\\aceitar_partida1080p.png', confidence=0.7)

    if aceitar_partida != None:
        click(aceitar_partida.left, aceitar_partida.top)
        return True
    return False

"""
def check_declare_champ():
    adc_lane = pyautogui.locateOnScreen('PickGame\\ImageLolzinho\\adc_lane.png', confidence=0.7)
    declare_champ = pyautogui.locateOnScreen('PickGame\\ImageLolzinho\\declare_champ.png', confidence=0.7)

    if adc_lane and declare_champ != None:
        print('é o declara champ')
        return True
    return False
"""
def check_adclane():
    adc_lane = pyautogui.locateOnScreen('PickGame\\ImageLolzinho\\adc_lane.png', confidence=0.7)
    escolha_champ = pyautogui.locateOnScreen('PickGame\\ImageLolzinho\\escolha_champ.png', confidence=0.7)


    if adc_lane and escolha_champ != None:
        print('é o adc lane')
        return True
    return False

def main():

    while True:
        if check_aceitar_partida() or check_adclane():
            #print('Aceite a partida')
            sleep(2)

main()