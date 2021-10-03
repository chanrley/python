import pyautogui
import time

# pyautogui.alert("O código vai começar. Não use nada do seu computador enquanto o código está rodando")
pyautogui.PAUSE = 1.5
# abrir o google drive no meu computador
pyautogui.press("winleft")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("drive.google.com")
pyautogui.press("enter")

# entrar na minha area de trabalho
pyautogui.hotkey("winleft", "d")

# cliquei no arquivo que eu quero fazer backup e arrastei ele
# como saber em qual posição da tela basta rodar essa linha em outro programa
# print(pyautogui.position())
pyautogui.moveTo(x=1836, y=43)
pyautogui.mouseDown()
pyautogui.moveTo(x=1228, y=765)

# enquanto eu to arrastando eu vou mudar para o google drive
pyautogui.hotkey("alt", "tab")
time.sleep(1)

# largar o arquivo no google drive
pyautogui.mouseUp()

# esperar 5 segundos
time.sleep(5)

pyautogui.alert("o código acabou de rodar. Pode usar seu computador de novo")



