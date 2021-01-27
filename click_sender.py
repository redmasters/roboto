from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Firefox:
    """
    Define o drive do selenium com o firefox e inicia a navegação.
    """

    def __init__(self):
        self.firefox = webdriver.Firefox()
        self.url = "http://pdv.mateus/maxipos_backoffice/app"

    def navegar(self):
        self.pause = time.sleep(1)
        self.firefox.get(self.url)

    def login_passwd(self):
        # Username
        self.firefox.find_element_by_xpath(
            '//*[@id="mktform_content"]/div/div[5]/div/div[2]/div[1]/div[2]/input'
        ).send_keys("41806")

        # Password
        self.firefox.find_element_by_xpath(
            '//*[@id="mktform_content"]/div/div[5]/div/div[2]/div[1]/div[3]/input'
        ).send_keys("41806")

        self.firefox.find_element_by_xpath(
            "/html/body/div[13]/form/div[2]/div/div[5]/div/div[2]/div[2]/div[2]/div"
        ).click()

    def painel_terminal(self):
        # Pausa por 2 segundos e vai até o painel terminal.
        self.pause = time.sleep(2)
        self.firefox.find_element_by_xpath("/html/body/div[12]/div[2]/div[4]").click()
        self.firefox.find_element_by_xpath(
            "/html/body/div[12]/div[2]/span[4]/div[4]"
        ).click()

    def sm(self, loja):
        # Entra com o nr da loja
        panel = self.firefox.find_element_by_xpath(
            "/html/body/div[13]/form/div[2]/div[1]/div[1]/div/div[1]/input"
        ).send_keys(loja)
        return panel

    def busca_panel(self):
        enter = self.firefox.find_element_by_xpath(
            "/html/body/div[13]/form/div[2]/div[1]/div[1]/div/div[1]/input"
        ).send_keys(Keys.RETURN)
        return enter

    def screenshot(self, print_name):
        self.pause = time.sleep(2)
        self.firefox.save_screenshot(print_name)

    def consistencia(self):
        # Navega até consistência
        self.firefox.find_element_by_xpath(
            "/html/body/div[12]/div[2]/span[4]/div[8]"
        ).click()
        self.firefox.find_element_by_xpath(
            "/html/body/div[12]/div[2]/span[4]/span/div[2]"
        ).click()
        # Clica no calendário
        self.firefox.find_element_by_xpath(
            "/html/body/div[13]/form/div[2]/div[1]/div[1]/div"
        ).click()

    def pick_data(self, url):
        self.firefox.find_element_by_xpath(url).click()

    def lista_loja(self, loja):
        self.firefox.find_element_by_xpath(
            "/html/body/div[13]/form/div[2]/div[1]/div[2]/input"
        ).send_keys(loja)

        self.firefox.find_element_by_xpath(
            "/html/body/div[13]/form/div[2]/div[1]/div[2]/input"
        ).send_keys(Keys.RETURN)

    def consistir(self):
        self.pause = time.sleep(2)
        self.firefox.find_element_by_xpath(
            "/html/body/div[13]/form/div[1]/div[3]/div[2]/div[1]"
        ).click()

    def sair(self):
        self.pause = time.sleep(2)
        self.firefox.quit()
