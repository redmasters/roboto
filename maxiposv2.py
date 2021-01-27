from click_sender import Firefox
from image_functions import CapturaImages
from PIL import Image

import os

# TODO: Utilizar o MCV;
# TODO: Automatizar data;
# TODO: Verificar erros de consistência;
# TODO: Um programa integado que pergunta quais PDVs desligarão e
# quais ficarão ligados;

"""
Ferramenta para auxiliar na consistência automática dos PDVs, auxiliando no processo de fechamento.
Visando a total automatização do processo.
"""


def consistir():
    # Inicia o processo de consistência.
    # Painel Terminal
    loja = 201
    firefox = Firefox()
    firefox.navegar()
    firefox.login_passwd()
    firefox.painel_terminal()
    firefox.sm(loja)
    firefox.busca_panel()
    firefox.screenshot("painel.png")
    # Painel de Consistência
    firefox.consistencia()
    firefox.pick_data("/html/body/div[8]/table/tbody/tr[8]/td[3]")
    firefox.lista_loja(loja)
    firefox.consistir()
    firefox.screenshot("const.png")
    # Fecha o firefox
    firefox.sair()
    # Desliga os PDVs
    desligando = True
    while desligando:
        desliga = input("\nDesliga todos os PDVs?")
        desliga = input("s/n ?")
        if desliga == "n":
            break
        else:
            os.system("desliga_pdvs")
            desligando = False


consistir()
