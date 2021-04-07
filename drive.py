from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from PIL import ImageGrab

import time
import requests
import datetime


class Driver():
    def __init__(self):
        firefoxOptions = webdriver.FirefoxOptions()
        firefoxOptions.headless = True
        self.navegador = webdriver.Firefox(options=firefoxOptions)
        
    def go_url(self, url):
        self.navegador.get(url)
        
    def close(self):
        self.navegador.quit()
        print("Firefox Closed")
        
    def login(self, usuario, senha):
        username = usuario
        password = senha
        user_box = self.navegador.find_element_by_name("formlogin_txtUsuario")
        password_box= self.navegador.find_element_by_name("formlogin_txtSenha")
        user_box.clear()
        password_box.clear()
        user_box.send_keys(username)
        password_box.send_keys(password)
        time.sleep(2)
        login = self.navegador.find_element_by_xpath("/html/body/div[13]/form/div[2]/div/div[5]/div/div[2]/div[2]/div[2]/div")
        login.click()
        print("Logado!")
        
    def painel_terminal(self):
        loja = 201
        processos = self.navegador.find_element_by_xpath("/html/body/div[12]/div[2]/div[4]")
        processos.click()
        print("Processos")

        painel_terminal = self.navegador.find_element_by_xpath("/html/body/div[12]/div[2]/span[4]/div[4]/div")
        painel_terminal.click()
        print("Painel Terminal")
        time.sleep(2)
        loja_box = self.navegador.find_element_by_xpath("/html/body/div[13]/form/div[2]/div[1]/div[1]/div/div[1]/input")
        loja_box.clear()
        loja_box.send_keys(loja)
        loja_box.send_keys(Keys.RETURN)
        
        # Print do Painel Terminal
        time.sleep(2)
        date = str(datetime.date.today())
        file_name = "panel_%s.png" % date
        # Zooming out
        # self.navegador.find_element_by_tag_name("html").send_keys(Keys.CONTROL + Keys.SUBTRACT)
        screenshot = self.navegador.save_screenshot(file_name)
        print("Print Saved")

        
    def painel_consistencia(self):
        consistencia_log = self.navegador.find_element_by_xpath("/html/body/div[12]/div[2]/span[4]/div[8]/div") 
        consistencia_log.click()
        
    # A ser implementado
    # def status_pdv(self, url):
    #     print("Estado dos PDVs")

    #     status = {}
    #     req = requests.get(url)
    #     page = req.text
    #     soup = BeautifulSoup(page, 'lxml')
    #     estado = soup.find_all_next('span', {'class': 'mktondesktop'})
    #     print(estado)
    #     status['estado'] = estado
    #     print(status)
    #     return status
    