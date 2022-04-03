from pyautogui import *
import pyautogui
from time import sleep

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

def check_aceitar_partida():
    aceitar_partida = pyautogui.locateOnScreen('PickGame\\ImageLolzinho\\aceitar_partida1080p.png', confidence=0.4)

    if aceitar_partida != None:
        click(aceitar_partida.left, aceitar_partida.top)
        return True
    return False

def check_adclane_ban():
    adc_lane_ban = pyautogui.locateOnScreen('PickGame\\ImageLolzinho\\BanaUmCampeao.png', confidence=0.4)

    if adc_lane_ban != None:
        sleep(3)
        click(x=1177, y=148); sleep(0.500); sleep(1) #clica em buscar
        typewrite('Lux', interval=0.300); sleep(1)
        click(x=586, y=236); sleep(0.500) #clica personagem
        click(x=804, y=763); sleep(0.500) #bani
        return True
    return False

def check_adclane_pick():
    adc_lane_pick = pyautogui.locateOnScreen('PickGame\\ImageLolzinho\\EscolhaSeuCampeao.png' or 'PickGame\\ImageLolzinho\\DeclareSeuCampeao.png', confidence=0.4)

    if adc_lane_pick != None:
        sleep(3)
        click(x=971, y=130); sleep(0.500) #clica em buscar
        typewrite('Draven', interval=0.300); sleep(1)
        click(x=483, y=203); sleep(0.500) #clica personagem
        click(x=804, y=763); sleep(0.500) #picka
        return True
    return False

def check_chat():
    chat = pyautogui.locateOnScreen('chat', confidence=0.4)
    if chat != None:
        click(x=135, y=1008); sleep(0.500)
        typewrite('To stremando clã 🦎 \n Da um salve na Twitch: SalamandraLw \n https://www.twitch.tv/salamandralw', interval=0.300); sleep(1)
        return True
    return False

def main():
    while True:
        if check_aceitar_partida() or check_adclane_ban() or check_adclane_pick():
            #print('Aceite a partida')
            sleep(2)
main()