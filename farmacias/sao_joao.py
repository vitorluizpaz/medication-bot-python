from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def sao_joao(driver, qtde_divalcon, qtde_litio, qtde_clozapina):
    medicamentos = {"Divalcon" : "https://www.saojoaofarmacias.com.br/divalcon-er-500mg-60-comprimidos-revestidos-abbott--c1--100020345/p",
                    "Lítio" : "https://www.saojoaofarmacias.com.br/carbolitium-300mg-90-comprimidos---c1--10029477/p",
                    "Clozapina" : "https://www.saojoaofarmacias.com.br/pinazan-25mg-30-comprimidos-cristalia--c1--100001961/p"}
    medicamentos_custo = {"Divalcon" : 0,
                        "Lítio" : 0,
                        "Clozapina" : 0}

    # Itera pelo site dos medicamentos
    for medicamento, url in medicamentos.items():
        driver.get(url)
        precos_inteiro = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "sjdigital-custom-apps-5-x-currencyInteger")))
        preco_inteiro = precos_inteiro[1].text
        precos_fracionario = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "sjdigital-custom-apps-5-x-currencyFraction")))
        preco_fracionario = precos_fracionario[1].text
        preco = float(".".join([preco_inteiro, preco_fracionario]))
        medicamentos_custo[medicamento] = preco

    total = qtde_divalcon * medicamentos_custo["Divalcon"]
    total += qtde_litio * medicamentos_custo["Lítio"]
    total += qtde_clozapina * medicamentos_custo["Clozapina"]

    return f"São João - {total:.2f}"