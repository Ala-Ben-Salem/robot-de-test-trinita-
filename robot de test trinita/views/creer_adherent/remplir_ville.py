from views.utils.utils import wait_for_element
from selenium.webdriver.common.by import By
import time
import math


def remplir_ville(driver, adherent):
    wait_for_element(driver, By.XPATH, '//*[@id="select2-id_address_set-0-city-container"]').click()
    remplir_ville = wait_for_element(driver, By.XPATH, '/html/body/span/span/span[1]/input')
    remplir_ville.send_keys(adherent.ville)
    time.sleep(1)
    first_option_v = wait_for_element(driver, By.XPATH, '//*[@id="select2-id_address_set-0-city-results"]/li[1]')
    first_option_v.click()

    # Vérifier la valeur du champ de code postal
    selected_option = wait_for_element(driver, By.XPATH, '//*[@id="select2-id_address_set-0-city-container"]')
    selected_text = selected_option.get_attribute("textContent")
    msg_ville = ''
    if selected_text == '---------':
        if isinstance(adherent.ville, float) and not math.isnan(adherent.ville):
            print("Échec de la sélection de la première option de la ville. ==> s'écrire avec erreur ou n\'a pas compatible avec code postal")
            msg_ville = ' | la ville s\'ecrire avec erreur ou n\'a pas compatible avec code postal | '
        elif isinstance(adherent.ville, str) and adherent.ville:
            print("Échec de la sélection de la première option de la ville. ==> s'écrire avec erreur , n\'a pas compatible avec code postal")
            msg_ville = ' | la ville s\'ecrire avec erreur ou n\'a pas compatible avec code postal | '
        else:
            print("L'élément de sélection de la ville n'a pas été trouvé. ==> vide")
            msg_ville = ' | la ville n\'a pas été trouvé. ==> vide | '
    else:
        print("La première option de la ville a été sélectionnée avec succès.")
        msg_ville = ' | la ville a été sélectionnée avec succès | '

    return msg_ville