from selenium import webdriver


# declare a variável para armazenar o URL a ser visitado
base_url = "https://www.amazon.in"

# declarar variável para armazenar o termo de usuario
user_term = "admin"
pass_term = "admin"

# declara e inicializa variável driver
driver = webdriver.Chrome()

# navegador deve ser carregado na janela maximizada
driver.maximize_window()

'''
O driver deve esperar implicitamente por uma determinada duração, para que o elemento em questão seja carregado.
 Para impor essa configuração, usaremos a função builtin implicitly_wait() do objeto 'driver'.
'''
driver.implicitly_wait(10) # 10 em segundos

# carregar um determinado URL na janela do navegador
driver.get(base_url)

# -- Etapas --
# para inserir o termo de usuario/senha, precisamos localizar a caixa de texto de usuario/senha
userTextBox = driver.find_element_by_id("user-input")
passTextBox = driver.find_element_by_id("password-input")
entrBotton = driver.find_element_by_class_name("standard-btn")

# limpa texto na caixa
userTextBox.clear()
passTextBox.clear()

# inserir o termo de usuário na caixa de texto
userTextBox.send_keys(user_term)
passTextBox.send_keys(pass_term)

# efetua login
entrBotton.click()

# testar se o URL/site correto foi carregado ou não
site = driver.title

# assert "Sensorweb" in site
if site == "Amazon":
    print(">>>>>>>>>  Site encontrado!")
else:
    print(">>>>>>>>>  Por favor verifique o endereço disponibilizado!")

# encerra janela
#driver.close()

# encerra página
#driver.close()
