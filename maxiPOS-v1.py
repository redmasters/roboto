from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

from PIL import Image

# Define navegador
navegador = webdriver.Firefox()


# Define Endereço
def endereco(url):
    navegador.get(url)


# Pausas
def pausa(num):
    time.sleep(num)


# Login e Senha
def username(login):
    navegador.find_element_by_xpath(
        '//*[@id="mktform_content"]/div/div[5]/div/div[2]/div[1]/div[2]/input'
    ).send_keys(login)


def passwd(senha):
    navegador.find_element_by_xpath(
        '//*[@id="mktform_content"]/div/div[5]/div/div[2]/div[1]/div[3]/input'
    ).send_keys(senha)


# Clica em 'entrar' na tela de login
def login_click():
    navegador.find_element_by_xpath(
        "/html/body/div[13]/form/div[2]/div/div[5]/div/div[2]/div[2]/div[2]/div"
    ).click()


# Navega até processos e clica em Painel Terminal
def processo_pTerminal():
    navegador.find_element_by_xpath("/html/body/div[12]/div[2]/div[4]").click()
    navegador.find_element_by_xpath("/html/body/div[12]/div[2]/span[4]/div[4]").click()


def sm(loja):
    panel = navegador.find_element_by_xpath(
        "/html/body/div[13]/form/div[2]/div[1]/div[1]/div/div[1]/input"
    ).send_keys(loja)
    return panel


def busca_panel():
    enter = navegador.find_element_by_xpath(
        "/html/body/div[13]/form/div[2]/div[1]/div[1]/div/div[1]/input"
    ).send_keys(Keys.RETURN)
    return enter


def consistenca(url):
    # Navega até consistência
    navegador.find_element_by_xpath(url).click()


# Clica em Loja
def click_loja(url):
    navegador.find_element_by_xpath(url).click()


# Click calendário
def click_calendario(url):
    navegador.find_element_by_xpath(url).click()


def seleciona_data(url):
    navegador.find_element_by_xpath(url).click()


def lista_loja(loja):
    lista = navegador.find_element_by_xpath(
        "/html/body/div[13]/form/div[2]/div[1]/div[2]/input"
    ).send_keys(loja)
    return lista


def clica_loja(url):
    enter = navegador.find_element_by_xpath(url).send_keys(Keys.RETURN)
    return enter


def consistir(url):
    navegador.find_element_by_xpath(url).click()


# Execução do programa
# Abre o navegador com o endereço
endereco("http://pdv.mateus/maxipos_backoffice/app")
pausa(2)

# Loga no sistema
username("41806")
passwd("41806")
login_click()  # Clica no botão de login

pausa(1)

# Expora o menu
# Clica em Processos
# Painel Terminal
processo_pTerminal()
pausa(1)

# Digita 201 e 'enter'
sm(201)  # Loja
busca_panel()
pausa(2)

# Printa Painel
navegador.save_screenshot("panel.png")

# Consistir
# Navega até consistência e clica
consistenca("/html/body/div[12]/div[2]/span[4]/div[8]")
click_loja("/html/body/div[12]/div[2]/span[4]/span/div[2]")

# Clica no calendário e seleciona data
click_calendario("/html/body/div[13]/form/div[2]/div[1]/div[1]/div")

seleciona_data("/html/body/div[8]/table/tbody/tr[7]/td[5]")  # TODO
# Automatizar seleção de data, resolver problema de 'obscure' data

# Seleciona loja
lista_loja(201)
clica_loja("/html/body/div[13]/form/div[2]/div[1]/div[2]/input")

pausa(2)


# Consistir
consistir("/html/body/div[13]/form/div[1]/div[3]/div[2]/div[1]")
pausa(5)

# Printa Consistência
navegador.save_screenshot("const.png")
pausa(2)

# Fecha o navegador
navegador.quit()

# Desliga PDVs
# os.system("dsesliga_pdvs")

# Programa Termina
print("Programa chegou ao fim")
