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

# Salva screenshot do painel
time.sleep(2)
mp.save_screenshot("panel.png")

# TODO Clicar em Consistência LOG
consistencia = mp.find_element_by_xpath(
    "/html/body/div[12]/div[2]/span[4]/div[8]"
).click()

# TODO Clicar em LOJA
consLoja = mp.find_element_by_xpath(
    "/html/body/div[12]/div[2]/span[4]/span/div[2]"
).click()
# TODO Digitar data e Loja
constData = mp.find_element_by_xpath(
    "/html/body/div[13]/form/div[2]/div[1]/div[1]/div"
).click()
constData = mp.find_element_by_xpath(
    "/html/body/div[8]/table/tbody/tr[7]/td[1]"
).click()

constLoja = mp.find_element_by_xpath(
    "/html/body/div[13]/form/div[2]/div[1]/div[2]/input"
)
constLoja.send_keys("201")
constLoja.send_keys(Keys.RETURN)

# TODO Clicar em Consistir
time.sleep(2)
consistir = mp.find_element_by_xpath(
    "/html/body/div[13]/form/div[1]/div[3]/div[2]/div[1]"
).click()

# TODO Salvar ScreenShoot
time.sleep(2)
mp.save_screenshot("const.png")

# Encerra o programa
time.sleep(2)
mp.quit()

print("Programa Chegou ao fim")
