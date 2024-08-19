import pyautogui
import subprocess as sp
programName = "write.exe"
fileName = "FuelRelParametrizadoLista.txt"
sp.Popen([programName, fileName])
pyautogui.hotkey('ctrl', 'b')
pyautogui.hotkey('alt', 'F4')

