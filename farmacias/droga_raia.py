from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def droga_raia(driver, qtde_divalcon, qtde_litio, qtde_clozapina):
    # Defina as variáveis com os detalhes da sua conta
    url = 'https://raiaextprd.b2clogin.com/raiaextprd.onmicrosoft.com/oauth2/v2.0/authorize?p=B2C_1A_Signin&client_id=31901109-0617-4215-a3d2-67f8e7642685&nonce=defaultNonce&redirect_uri=https%3A%2F%2Fwww.drogaraia.com.br%2Fapi%2Fnext%2Fcallback-login&scope=openid+31901109-0617-4215-a3d2-67f8e7642685&response_type=code+token&prompt=login&channel=site&version=latest&response_mode=query&info=ZGV2aWNl'  # Substitua pelo URL de login
    username = 'username' # Substitua pelo seu username
    password = 'senha' # Substitua por sua senha
    medicamentos = {"Divalcon" : "https://www.drogaraia.com.br/divalcon-er-500mg-60-comprimidos-c1.html",
                    "Lítio" : "https://www.drogaraia.com.br/carbolitium-300mg-com-90-comprimidos-mastigaveis-c1.html?origin=autocomplete",
                    "Clozapina" : "https://www.drogaraia.com.br/pinazan-25-mg-30-comprimidos.html?origin=autocomplete"}
    medicamentos_custo = {"Divalcon" : 0,
                        "Lítio" : 0,
                        "Clozapina" : 0}
    # Navegue até o site de login
    driver.get(url)
    # Localize o campo de username e insira o nome de usuário
    username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "signInName"))) # Substitua pelo ID real do campo
    username_field.send_keys(username)
    # Localize o campo de senha e insira a senha
    password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "password"))) # Substitua pelo ID real do campo
    password_field.send_keys(password)
    # Enviar o formulário
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "next")))
    button.click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Sair']")))
    # Acessa o site do 1 medicamento
    driver.get(medicamentos["Divalcon"])
    try:
        WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "dngqVh"), "R$"))
        preco_elemento = driver.find_element(By.CLASS_NAME, "dngqVh")
        preco = float(preco_elemento.text[3:].replace(",","."))
    except TimeoutException:
        print("O elemento 1 com o preço não apareceu no tempo esperado")
    medicamentos_custo["Divalcon"] = preco
    # Acessa o site do 2 medicamento
    driver.get(medicamentos["Lítio"])
    try:
        WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "cfyfiB"), "R$"))
        preco_elemento = driver.find_element(By.CLASS_NAME, "cfyfiB")
        preco = float(preco_elemento.text[3:].replace(",","."))
    except TimeoutException:
        print("O elemento 2 com o preço não apareceu no tempo esperado")
    medicamentos_custo["Lítio"] = preco
    # Acessa o site do 3 medicamento
    driver.get(medicamentos["Clozapina"])
    try:
        WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "cfyfiB"), "R$"))
        preco_elemento = driver.find_element(By.CLASS_NAME, "cfyfiB")
        preco = float(preco_elemento.text[3:].replace(",","."))
    except TimeoutException:
        print("O elemento 3 com o preço não apareceu no tempo esperado")
    medicamentos_custo["Clozapina"] = preco

    total = qtde_divalcon * medicamentos_custo["Divalcon"]
    total += qtde_litio * medicamentos_custo["Lítio"]
    total += qtde_clozapina * medicamentos_custo["Clozapina"]

    return f"Droga raia - {total:.2f}"