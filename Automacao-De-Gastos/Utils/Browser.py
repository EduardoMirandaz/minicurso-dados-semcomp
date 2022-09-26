import pandas as pd

from selenium import webdriver # Realiza a interação com a página web
from selenium.webdriver.support.select import Select # Seleciona as opções
from selenium.webdriver.common.keys import Keys # Links e teclas
from selenium.webdriver.common.by import By # Procura tags e encontra seletores

class Browser:
    def inicializarBrowser():
        #Instanciando o browser
        path_driver = '/home/draude/Documentos/Desenvolvimento/Minicurso-Semcomp-Dados/Automacao-De-Gastos/driver/chromedriver'
        url = 'https://03felipesampaio.github.io'
        driver = webdriver.Chrome(path_driver)
        driver.get(url)
        driver.maximize_window()
        return driver

