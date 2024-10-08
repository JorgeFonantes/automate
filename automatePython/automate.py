import time
import pyautogui

pyautogui.PAUSE = 0.6   
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.press("win")
time.sleep(0.9)
pyautogui.write("firefox") #pode ser qualquer navegador contando q esteja instalado na sua máquina
pyautogui.press("enter")
time.sleep(1.0)
pyautogui.click(x=415, y=60)
pyautogui.write(link)
time.sleep(0.3)
pyautogui.press("enter")
time.sleep(3.0)
pyautogui.click(x=458, y=372)
pyautogui.write("email.test@enterprise.com") # pode ser qualquer email aqui esse é apenas para testes
pyautogui.press("tab")
pyautogui.write("1234567890")
pyautogui.press("tab")
pyautogui.press("enter")

# até aqui ele já consegue se logar sozinho, pode ocorrer alguns erros dependendo da sua máquina e do seu monitor

import pandas as pd

tabela = pd.read_csv("products.csv")

time.sleep(5)

for linha in tabela.index:
    pyautogui.click(x=505, y=251)
    codigo = tabela.loc[linha, "codigo"]
 
    pyautogui.write(str(codigo))
    
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
   
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    
    pyautogui.press("enter") 
    
    pyautogui.scroll(5000)
    








