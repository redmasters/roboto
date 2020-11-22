from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from PIL import Image

mp = webdriver.Firefox()
mp.get("http://pdv.mateus/maxipos_backoffice/app")
time.sleep(2)

username = mp.find_element_by_xpath(
    '//*[@id="mktform_content"]/div/div[5]/div/div[2]/div[1]/div[2]/input'
).send_keys("41806")

password = mp.find_element_by_xpath(
    '//*[@id="mktform_content"]/div/div[5]/div/div[2]/div[1]/div[3]/input'
).send_keys("41806")
# password.send_keys("41806")

login = mp.find_element_by_xpath(
    "/html/body/div[13]/form/div[2]/div/div[5]/div/div[2]/div[2]/div[2]/div"
).click()

# clicar em Processos
time.sleep(1)
processos = mp.find_element_by_xpath("/html/body/div[12]/div[2]/div[4]").click()

# clicar em Painel Terminal
painel_terminal = mp.find_element_by_xpath(
    "/html/body/div[12]/div[2]/span[4]/div[4]"
).click()

time.sleep(2)

# Digitar 201 e enter
loja = mp.find_element_by_xpath(
    "/html/body/div[13]/form/div[2]/div[1]/div[1]/div/div[1]/input"
)

loja.send_keys("201")
loja.send_keys(Keys.RETURN)

# TODO Verificar PDVS com status 0 - Fechado
# TODO Se TRUE tirar screenshots, caso contrário enviar mensagem de alerta

time.sleep(2)
mp.save_screenshot("panel.png")

# TODO Clicar em Consistência LOG
# TODO Clicar em LOJA
# TODO Digitar data e Loja
# TODO Clicar em Consistir
# TODO Salvar ScreenShoot
