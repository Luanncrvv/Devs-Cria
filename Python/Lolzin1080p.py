import os
import pygetwindow
from pymsgbox import *
from time import sleep
from pyautogui import click , press

# Automação manual para colocar o lol em 1080p
# Requisitos, monitor principal tem que estar na resolução em 1080p, caso contrario devera alterar as coordenadas
# Se atentar nos sleep(2) cada pc abri configurações e launcher do lol num tempo especifico

os.startfile ("ms-settings:taskbar"); sleep (2)

click(x=407, y=769); sleep (2) # clica na opção Comportamentos da barra de tarefas

click(x=392, y=886); sleep (2) # Clica em Ocultar automaticamente a barra de tarefas

press("winleft"); sleep (2) # clica no botao do windows

click(x=572, y=628); sleep (20) # clica no lolzinho   ##editar as coordenadas para clicar no atalho do lol certo


alert(text='A Rito Gomes Abriu ?', title='É o tiltas 😡', button='OK'); sleep(2) #Gera uma mensagem na tela

carlinhos = "Configurações"; carlinho = pygetwindow.getWindowsWithTitle(carlinhos)[0]; carlinho.activate(); sleep (2) # coloca a janela de "Configurações" em primeiro plano

click(x=392, y=886); sleep (2) # Clica em Ocultar automaticamente a barra de tarefas

carlinho.close() # Fecha a "Configurações"



#Coordenadas para colocar em 1080p
"""click(x=1692,y=108) # Clica na engrenagem

sleep (2)

click(x=1234,y=303) # Clica na area das opções

sleep (2)

press('down', presses=4)

sleep (2)

click(x=849,y=665) # Clica no tamanho de janela

sleep (2)

click(x=898,y=833) # Clica no tamanho de janela selecionada

sleep (2)

click(x=963,y=965) # Clica no pronto"""




#validador = 'É o tiltas 😡'
#windows = pygetwindow.getWindowsWithTitle(validador)[0]
#windows.activate()