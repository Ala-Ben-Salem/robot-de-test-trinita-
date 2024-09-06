from selenium.webdriver.common.by import By
from views.utils.utils import wait_for_element, capture_screenshot, add_rapport_word
import time

def rechercher_contrat_ouvert(driver, testvalidation, compteur):
    print('hello recherche contrat ouvert')
    zone_recherch = wait_for_element(driver, By.XPATH, '//*[@id="DataTables_Table_0_filter"]/label/input')
    zone_recherch.send_keys(testvalidation.numero_contrat)
    capture_screenshot(driver, f"rechercher_un_contrat_{compteur}")
    add_rapport_word('rapport', f'entrer pour rechercher un contrat_{compteur+1}', f'screenshots/rechercher_un_contrat_{compteur}.png', compteur)

    time.sleep(1)
    wait_for_element(driver, By.XPATH, f'//a[text()="{testvalidation.numero_contrat}"]').click()
    #wait_for_element(driver, By.XPATH, '//*[@id="main"]/article[1]/div/section[1]/div[3]')
    capture_screenshot(driver, f"entrer_dans_contrat_{compteur}")
    add_rapport_word('rapport', f'entrer dans contrat_{compteur+1}', f'screenshots/entrer_dans_contrat_{compteur}.png', compteur)

    # Check for warning message
    try:
        warning_element = wait_for_element(driver, By.XPATH, '//*[@id="messages"]/div/p')
        time.sleep(1)
        warning_message = warning_element.text
        print(f"Warning message found: {warning_message}")
        
        # Optionally, add the warning message to the Word report
        add_rapport_word('rapport', f'Warning message found: {warning_message}', f'screenshots/entrer_dans_contrat_{compteur}.png', compteur)
        
        return warning_message  # Return the warning message text
    except Exception as e:
        print("No warning message found")
        return None  # Return None if no warning message is found
