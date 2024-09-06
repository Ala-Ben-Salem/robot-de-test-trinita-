from views.utils.utils import wait_for_element, capture_screenshot, add_rapport_word
from selenium.webdriver.common.by import By


def recherche_adherent_avant_remplir(driver, adherent,compteur):
    recherche_prenom = wait_for_element(driver, By.XPATH, '//*[@id="id_given_name"]')
    recherche_prenom.clear()
    recherche_prenom.send_keys(adherent.prenom)
    wait_for_element(driver, By.XPATH, '//*[@id="submit-id-submit"]').click()
    capture_screenshot(driver, f"recherche_adherent_{compteur+1}")
    add_rapport_word('rapport', f"recherche un adherent {compteur+1} avant de la creation", f'screenshots/recherche_adherent_{compteur+1}.png',compteur) ########
    
    wait_for_element(driver, By.XPATH, '//*[@id="create-person-button"]').click()
