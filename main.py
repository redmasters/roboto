from drive import Driver
import time

def pausa():
    time.sleep(2)

url = 'http://pdv.mateus/maxipos_backoffice/app'

navegador = Driver()
navegador.go_url(url)
pausa()
navegador.login(****, ****)
pausa()
navegador.painel_terminal()
navegador.painel_consistencia()

# navegador.close()
