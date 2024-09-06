from selenium.webdriver.common.by import By
from views.utils.utils import wait_for_element, capture_screenshot, add_rapport_word
import time
from bs4 import BeautifulSoup   # pip install beautifulsoup4


def somme_table_ventilation(driver, compteur):
    print('helo ventilation')
    wait_for_element(driver, By.XPATH, '//*[@id="main"]/article[1]/div/section[2]/div[5]/ul/li[1]/a').click()

    capture_screenshot(driver, f"ventilation_technique_contrat_{compteur}")
    add_rapport_word('rapport', f'ventilation technique contrat_{compteur+1}', f'screenshots/ventilation_technique_contrat_{compteur}.png', compteur)

    time.sleep(3)

    # Extraire le contenu HTML du tableau
    #table_html = driver.find_element(By.XPATH, xpath_table).get_attribute('outerHTML')
    table_html = wait_for_element(driver, By.XPATH, "//div[@id='year_2024']").get_attribute('outerHTML')

    # Parser le contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(table_html, 'html.parser')
    
    # Extraire les montants TTC
    montant_ttc_cells = soup.select('td:nth-child(5)')
    
    # Calculer la somme des montants TTC
    somme_ttc = sum(float(cell.text.strip().replace('€', '').replace(',', '.')) for cell in montant_ttc_cells)
    
    element_besoin = driver.find_element(By.XPATH, '//*[@id="pricing_tab"]/ul/li[1]/a')
    driver.execute_script("arguments[0].scrollIntoView(true);", element_besoin)
    time.sleep(5)

    capture_screenshot(driver, f"calcul_ventilation_technique_contrat_{compteur}")
    add_rapport_word('rapport', f'calcul ventilation technique contrat_{compteur+1} ==> {somme_ttc:.2f} €', f'screenshots/calcul_ventilation_technique_contrat_{compteur}.png', compteur)


    return somme_ttc

