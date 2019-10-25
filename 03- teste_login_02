import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Meusite(unittest.TestCase):
   # declara variavel url
   base_url = "ESCREVER O LINK NO SITE AQUI"
   # declara variavel caixa de usuario e senha
   user = "admin"
   passw = "senha"

   # PRIMEIRAS CONDICOES
   def setUp(self):
       # declara e inicializa o driver do navegador
       self.driver = webdriver.Chrome()

       # o navegador abre a janela maxmizado
       self.driver.maximize_window()

       # O driver deve esperar implicitamente por uma determinada duração,
       # para que o elemento em questão seja carregado.
       # Para impor essa configuração, usaremos a função builtin implicitly_wait() do objeto 'driver'.
       self.driver.implicitly_wait(10)

   def test_login(self):
       driver = self.driver
       # add url ao navegador
       self.driver.get(self.base_url)

       # define identificacao da caixa de usuario em html
       boxUser = self.driver.find_element_by_id("user-input") # MODIFICAR
       boxPass = self.driver.find_element_by_id("password-input") # MODIFICAR


       # limpa caixa de usuario/senha
       boxUser.clear()
       boxPass.clear()

       # add o termo de usuario/senha
       boxUser.send_keys(self.user)
       boxUser.send_keys(Keys.RETURN)
       boxPass.send_keys(self.passw)

       # clica botao entrar
       self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/form/table/tbody/tr[2]/td[3]/input").click() # MODIFICAR


   #def tearDown(self):
       # encerra pagina
       #self.driver.close()


if __name__ == "__main__":
   unittest.main()
