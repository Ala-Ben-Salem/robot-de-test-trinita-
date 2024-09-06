from selenium.webdriver.common.by import By
from views.utils.utils import wait_for_element, capture_screenshot, add_rapport_word


def test_validation_solde(driver, compteur, contrat):
    solde_attendre = contrat.solde_attendre
    solde_web = wait_for_element(driver, By.XPATH, '//*[@id="main"]/article[1]/div/section[2]/fieldset[1]/div[1]/div[4]/p/span').text.strip()
    solde_web = float(solde_web.replace(',', '').replace(' ', '').replace('€', ''))
    resultat_solde = solde_web - solde_attendre
    print(f"voila la resultat ==> {resultat_solde}")

    if resultat_solde==0:
        msg_s= 'solde attendre egale a la solde de contrat'

    elif resultat_solde >0:
        msg_s = 'solde de contrat superieur a la solde attendre'

    else:
        msg_s = 'la solde attendre superieur a la solde de contrat'
    
    print(msg_s)
    
    capture_screenshot(driver, f"Solde__de__contrat{compteur}")
    add_rapport_word('rapport', f'voila la resultat ==> {resultat_solde} ==> alors '+msg_s, f'screenshots/Solde__de__contrat{compteur}.png', compteur)

    return resultat_solde