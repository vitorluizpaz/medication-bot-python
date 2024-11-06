from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def preço_popular(driver, qtde_divalcon, qtde_litio, qtde_clozapina):
    medicamentos = {"Divalcon" : "https://www.precopopular.com.br/divalcon-er-c-60-cp-500mg/p",
                    "Lítio" : "https://www.precopopular.com.br/carbolitium-com-90-comprimidos-revestidos-300mg/p",
                    "Clozapina" : "https://www.precopopular.com.br/pinazan-25mg-com-30-comprimidos/p"}
    medicamentos_custo = {"Divalcon" : 0,
                        "Lítio" : 0,
                        "Clozapina" : 0}

    # Itera pelo site dos medicamentos
    for medicamento, url in medicamentos.items():
        driver.get(url)
        precos_inteiro = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "vtex-product-price-1-x-currencyInteger")))
        precos_inteiro_texto = [elemento.text for elemento in precos_inteiro]
        precos_fracionario = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "vtex-product-price-1-x-currencyFraction")))
        precos_fracionario_texto = [elemento.text for elemento in precos_fracionario]
        precos_concatenados = [float(f"{inteiro}.{fracionario}") for inteiro, fracionario in zip(precos_inteiro_texto, precos_fracionario_texto)]
        medicamentos_custo[medicamento] = precos_concatenados[1]

    total = qtde_divalcon * medicamentos_custo["Divalcon"]
    total += qtde_litio * medicamentos_custo["Lítio"]
    total += qtde_clozapina * medicamentos_custo["Clozapina"]

    return f"Preço popular - {total:.2f}"