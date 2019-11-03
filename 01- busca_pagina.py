from selenium import webdriver


base_url = "https://www.amazon.in"

# declara e inicializa variável do driver
driver = webdriver.Chrome()

# navegador é carregado na janela maximizada
driver.maximize_window()

'''
O driver deve esperar implicitamente por uma determinada duração, para que o elemento em questão seja carregado.
 Para impor essa configuração, usaremos a função builtin implicitly_wait () do objeto 'driver'.
'''
driver.implicitly_wait(10)  # 10 em segundos

# carregar um determinado URL na janela do navegador
driver.get(base_url)

# testar se o URL/site correto foi carregado ou não
site = driver.title
#assert "Sensorweb" in site
if site == "Amazon":
    print(">>>>>>>>>  Site encontrado!")
else:
    print(">>>>>>>>>  Por favor verifique o endereço disponibilizado!")

# encerra a janela
driver.close()
