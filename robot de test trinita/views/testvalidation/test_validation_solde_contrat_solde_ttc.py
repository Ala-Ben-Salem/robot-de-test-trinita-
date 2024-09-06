from selenium.webdriver.common.by import By
from views.utils.utils import wait_for_element, capture_screenshot, add_rapport_word


def test_validation_solde_contrat_solde_ttc(driver, compteur, somme_ttc):
    print('calcule solde_contrat_solde_ttc ')
    solde_web = wait_for_element(driver, By.XPATH, '//*[@id="main"]/article[1]/div/section[2]/fieldset[1]/div[1]/div[4]/p/span').text.strip()
    solde_web = float(solde_web.replace(',', '.').replace(' ', '').replace('€', ''))
    
    resultat_solde = solde_web - somme_ttc
    print(f"voila la resultat de solde contrat - solde TTC ==> {resultat_solde}")

    if resultat_solde==0:
        msg_s= 'solde TTC egale a la solde de contrat'

    elif resultat_solde >0:
        msg_s = 'solde de contrat superieur a la solde TTC'

    else:
        msg_s = 'la solde TTC superieur a la solde de contrat'
    
    print(msg_s)

    add_rapport_word('rapport', f'voila la resultat de contrat_{compteur+1} de solde contrat {solde_web:.2f} - solde TTC {somme_ttc:.2f} ==> {resultat_solde:.2f} ==> alors '+msg_s, f'screenshots/entrer_dans_contrat_{compteur}.png', compteur)
    
    return resultat_solde