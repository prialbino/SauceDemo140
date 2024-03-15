# 1 - Bibliotecas
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe (optional)
class Test_Produtos():

    # 2.1 - Atributos (campos, valores, etc)
    url = "https://www.saucedemo.com"   #endereco do site alvo

    # 2.2  Funcoes e metodos
    def setup_method(self,method):   #metodo de inicializacao dos testes ; nao preciso do self pq nao uso classe
        self.driver = webdriver.Chrome() #instanciar o objeto do selenium webdriver como chrome(deixamos preparados)            self.driver.implicitly_wait(10)  #define o tempo de espera padrao por elementos por 10sec

    def teardown_method(self,method):   #metodo de finalizacao
        self.driver.quit()  #encerra, destroi o objeto do selenium wedbdriver da memoria          

    def test_selecionar_produto(self):  #metodo de teste
        self.driver.get(self.url)      #abre o navegador
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user") #escreve no campo user-name
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
