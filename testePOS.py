from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


class Navegador:
    def __init__(self, navegador):
        self.navegador = navegador


endereco = "http://pdv.mateus/maxipos_backoffice/app"

ff = webdriver.Firefox()
ff.get(endereco)
