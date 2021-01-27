from PIL import Image
import time


"""Módulo que controla manipulação e captura de imagens"""


class CapturaImages:
    def __init__(self, firefox):
        self.firefox = firefox

    def print(self, print_name):
        # Salva print na pasta do programa
        self.pausa = time.sleep(2)
        self.firefox.save_screenshot(print_name)
