from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def catarinense(driver, qtde_divalcon, qtde_litio, qtde_clozapina):
    medicamentos = {"Divalcon" : "https://www.drogariacatarinense.com.br/divalcon-er-c-60-cp-500mg/p",
                    "Lítio" : "https://www.drogariacatarinense.com.br/carbolitium-com-90-comprimidos-revestidos-300mg/p",
                    "Clozapina" : "https://www.drogariacatarinense.com.br/pinazan-25mg-com-30-comprimidos/p"}
    medicamentos_custo = {"Divalcon" : 0,
                        "Lítio" : 0,
                        "Clozapina" : 0}

    # Acessa os sites dos medicamentos
    for medicamento, url in medicamentos.items():
        driver.get(url)
        WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "skuBestPrice"), "R$"))
        
        preco = float(driver.find_element(By.CLASS_NAME, "skuBestPrice").text[3:].replace(",", "."))
        medicamentos_custo[medicamento] = preco

    total = qtde_divalcon * medicamentos_custo["Divalcon"]
    total += qtde_litio * medicamentos_custo["Lítio"]
    total += qtde_clozapina * medicamentos_custo["Clozapina"]

    return f"Catarinense - {total:.2f}"