from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from click_sender import Navegador

"""Módulo com funções """


def processo_pTerminal():
    firefox = Navegador()
    firefox.find_element_by_xpath("/html/body/div[12]/div[2]/div[4]").click()
    firefox.find_element_by_xpath("/html/body/div[12]/div[2]/span[4]/div[4]").click()
