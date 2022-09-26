import pandas as pd

from selenium import webdriver # Realiza a interação com a página web
from selenium.webdriver.support.select import Select # Seleciona as opções
from selenium.webdriver.common.keys import Keys # Links e teclas
from selenium.webdriver.common.by import By # Procura tags e encontra seletores

#Instanciando o browser
path_driver = '/home/draude/Documentos/Desenvolvimento/Minicurso-Semcomp-Dados/Automacao-De-Gastos/driver/chromedriver'
url = 'https://03felipesampaio.github.io'
driver = webdriver.Chrome(path_driver)
driver.get(url)
driver.maximize_window()


# Mapeamentos
    # LoginPage
fieldUser = '//*[@id="usuario"]'
fieldPassword = '//*[@id="senha"]'
btnEnter = '//*[@id="btn-entrar"]'

#####################################
#              LoginSteps           #
#####################################
    # Login Input Steps
login_box = driver.find_element("xpath", fieldUser)
login_box.click()
login_box.send_keys('eduardo@gmail.com')

    # Password Input Steps
password_box = driver.find_element("xpath", fieldPassword)
password_box.click()
password_box.send_keys('123')

    # Password Input Steps
enter_button = driver.find_element("xpath", btnEnter)
enter_button.click()

# Captando o saldo:
saldo_xpath = r'/html/body/div[1]/div[1]/p'
saldo = driver.find_element("xpath", saldo_xpath).text
print("Saldo: %s" %saldo)

# Filtrando as transações por mês:
periodo_xpath = r'//*[@id="periodo"]'
dropdown_element = driver.find_element("xpath",periodo_xpath)
dropdown_element.click()
periodo = Select(dropdown_element)
periodo.select_by_visible_text("Mês atual")



#Captando as linhas da tabelas:
linhas = driver.find_elements("xpath","/html/body/div[2]/table/tbody/tr")
tamanho_tabela = len(linhas)
print(linhas)


# Obtendo as colunas da tabela
cols = []
for i in range(1,4):
	xpath_col = r'/html/body/div[2]/table/tbody/tr[1]/th[{}]'
	xpath_col = xpath_col.format(i)
	conteudo_celula = driver.find_element("xpath",xpath_col)
	conteudo_celula = conteudo_celula.text
	cols.append(conteudo_celula)

# Obtendo as linhas da tabela
conteudo_linhas = []
for linha in linhas:
    for i in range(2, tamanho_tabela+1):
        celulas_linha = []
        for x in range(1,4):
            xpath_celula = '/html/body/div[2]/table/tbody/tr[{}]/td[{}]'
            xpath_celula = xpath_celula.format(i,x)
            conteudo_celula = driver.find_element("xpath",xpath_celula)
            conteudo =  conteudo_celula.text
            celulas_linha.append(conteudo)
        conteudo_linhas.append(celulas_linha)

# Inserindo os dados da tabela no arquivo csv
data = pd.DataFrame(conteudo_linhas)
data_csv = data.to_csv('transacoes.csv',columns=cols,index=False)

# Fechando o driver
driver.quit()


