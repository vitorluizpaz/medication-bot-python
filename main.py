from selenium import webdriver

from farmacias.droga_raia import droga_raia
from farmacias.panvel import panvel
from farmacias.preço_popular import preço_popular
from farmacias.sao_joao import sao_joao
from farmacias.catarinense import catarinense

while True:
    try:
        a = int(input("Digite o número de caixas de Depakote: "))
        b = int(input("Digite o número de caixas de Lítio: "))
        c = int(input("Digite o número de caixas de Pinazan: "))
    except:
        print("Digite apenas valores inteiros!")
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
        print("---------------------------------------------------------------")
        print(catarinense(driver, a, b, c))
        # print(droga_raia(driver, a, b, c)) # Necessita de um login e senha.
        print(panvel(driver, a, b, c))
        print(preço_popular(driver, a, b, c))
        print(sao_joao(driver, a, b, c))
        print("---------------------------------------------------------------")
        driver.quit()
        break