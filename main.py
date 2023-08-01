
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class BotElegibilidadeAmil():

    def __init__(self, dados):
        self.USUARIO = dados['usuario']
        self.SENHA = dados['senha']
         # Define o número da carteirinha para pesquisa
        self.NUMERO_CARTEIRA = dados['numero_carteira']

        self.URL_BASE = "#######################################"
        self.URL_ELEGIBILIDADE = "###########################################"
        

    def run(self, driver):

        # Acessa o portal da Operadora
        driver.get(self.URL_BASE)
        driver.implicitly_wait(10)
        driver.find_element(By.ID, "finalizar-walktour").click()
        driver.find_element(By.ID, 'login-usuario').send_keys(self.USUARIO)
        driver.find_element(By.ID, 'login-senha').send_keys(self.SENHA)
        driver.find_element(By.CLASS_NAME, 'btn-login').click()

        sleep(5)
        driver.get('##############################################')

        carteirinha_input = driver.find_element(By.ID, 'NaN')
        carteirinha_input.send_keys(self.NUMERO_CARTEIRA)
        carteirinha_input.send_keys(Keys.RETURN)
        
        msg_response = driver.find_element(By.XPATH, '//*[@id="undefined"]/as-info-beneficiario/as-beneficiario-plano/section/div[1]/div[3]/div/p').text
        if msg_response == "Cliente elegível":
            msg_response = "Elegivel"
        else:
            msg_response = "não eleginvel"

        return {'msg_response': msg_response}