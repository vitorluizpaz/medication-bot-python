from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def panvel(driver, qtde_divalcon, qtde_litio, qtde_clozapina):
    medicamentos = {"Divalcon" : "https://www.panvel.com/panvel/divalcon-er-500mg-60-comprimidos-revestidos-c1/p-829640",
                    "Lítio" : "https://www.panvel.com/panvel/carbolitium-300mg-90-comprimidos-revestidos-c1/p-104504",
                    "Clozapina" : "https://www.panvel.com/panvel/pinazan-25mg-30-comprimidos-c1/p-638040"}
    medicamentos_custo = {"Divalcon" : 0,
                        "Lítio" : 0,
                        "Clozapina" : 0}
    # Acessa os sites dos medicamentos
    for medicamento, url in medicamentos.items():
        driver.get(url)
        WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "deal-price"), "R$"))

        preco = float(driver.find_element(By.CLASS_NAME, "deal-price").text[3:].replace(",", "."))
        medicamentos_custo[medicamento] = preco

    total = qtde_divalcon * medicamentos_custo["Divalcon"]
    total += qtde_litio * medicamentos_custo["Lítio"]
    total += qtde_clozapina * medicamentos_custo["Clozapina"]

    return f"Panvel - {total:.2f}"