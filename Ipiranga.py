import excluir_piranga
import time
import pyautogui
import subprocess
import os
from datetime import datetime, timedelta
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

string = 'refrigerantes'# nome do usuario
options = Options()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\00ipiranga\Piranga"
  })
s = Service('C:\\BrowserDrivers\\chromedriver.exe')
driver = webdriver.Chrome(service=s, options=options)
driver.get("https://web.ipirangaconnect.com.br/SvOutAdmLogIn")
pyautogui.press('tab')
pyautogui.write(''+string.lower())#digita o nome do usuario
pyautogui.press('tab')
pyautogui.write('1234')#senha digitada
pyautogui.press('enter')
time.sleep(10)
#dentro do site
pyautogui.click(1181,187)#vai para o relatorio
time.sleep(10)
pyautogui.click(683,539)#fechar o sistema
time.sleep(10)

folder=r'C:/00ipiranga/Piranga/'
for file_name in os.listdir(folder):
    old_name=folder+file_name
    new_name=folder+'Piranga.xls'
    os.rename(old_name,new_name)
subprocess.call([r'C:\00ipiranga\fl.exe'])
quit()




