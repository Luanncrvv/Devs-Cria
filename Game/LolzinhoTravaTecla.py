import pyautogui
import pygetwindow
from time import sleep
import mouse

## Esse script é para ser usado em algum momento que vc precisa fazer um pause e sair do pc por alguns instantes
## A automação fica clicando em circular dentro da base infinitamente, fazendo com que não tenha queda dentro do game
## Lembrar de Desbloquear a Camera

def click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()





def Basevermelho():
    mercador_vermelho =  pyautogui.locateOnScreen('PickGame\\ImageLolzinho\\MercadorVermelho.png', confidence=0.5)

    carlinhos = "League of Legends (TM)"; carlinho = pygetwindow.getWindowsWithTitle(carlinhos)[0]; carlinho.activate(); sleep (2)

    if mercador_vermelho != None:

        mouse.move(x=1009, y=221, duration=0.200); sleep(3); pyautogui.mouseDown(button='right'); pyautogui.mouseUp(button='right')
        mouse.move(x=1003, y=416, duration=0.200); sleep(3); pyautogui.mouseDown(button='right'); pyautogui.mouseUp(button='right')
        return True
    return False




def Baseazul():
    mercador_azul =  pyautogui.locateOnScreen('PickGame\\ImageLolzinho\\MercadorAzul.png', confidence=0.5)

    carlinhos = "League of Legends (TM)"; carlinho = pygetwindow.getWindowsWithTitle(carlinhos)[0]; carlinho.activate(); sleep (2)

    if mercador_azul != None:

        mouse.move(x=854, y=716, duration=0.200);  sleep(3); pyautogui.mouseDown(button='right'); pyautogui.mouseUp(button='right')
        mouse.move(x=675, y=520, duration=0.200);  sleep(3); pyautogui.mouseDown(button='right'); pyautogui.mouseUp(button='right')
        return True
    return False

def main():
    while True:
        if Baseazul() or Basevermelho():
            sleep(5)

main()



#mouse.move(x=1656, y=1062, duration=0.200); sleep(3); pyautogui.mouseDown(); pyautogui.mouseUp() #desbloquear tela