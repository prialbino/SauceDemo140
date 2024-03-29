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
        self.driver.implicitly_wait(5)
        
    def teardown_method(self,method):   #metodo de finalizacao
        self.driver.quit()  #encerra, destroi o objeto do selenium wedbdriver da memoria          

    def test_selecionar_produto(self):  #metodo de teste
        self.driver.get(self.url)      #abre o navegador
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user") #escreve no campo user-name
        self.driver.find_element(By.NAME, "password").send_keys("secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "input.submit-button.btn_action").click()  #click no botao de login

        #transicao de pagina

        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"  #confirma se esta escrito products no elemento
        assert self.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack"  #confirma se e mochila
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == "$29.99" #confirma preco
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".title").text == "Your Cart"
        assert self.driver.find_element(By.ID, "item_4_title_link").text == "Sauce Labs Backpack"
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_price").text == "$29.99"
        assert self.driver.find_element(By.CSS_SELECTOR, ".cart_quantity").text == "1"
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
