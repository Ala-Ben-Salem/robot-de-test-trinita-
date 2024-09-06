from views.utils.utils import wait_for_element, capture_screenshot, add_rapport_word
from selenium.webdriver.common.by import By
import time
import re


def remplir_date_verification(driver, typedate, xpath, text):
    # remplir Date
    try:
        # Convertir la date en chaîne et enlever les espaces
        date = str(typedate).strip()

        # Vérifier le format de la date
        if re.match(r'^\d{2}/\d{2}/\d{4}$', date):
            remplir_date = wait_for_element(driver, By.XPATH, xpath)
            remplir_date.send_keys(date)
            msg_date = 'La ' + text + ' a été remplie avec succès. | '
        else:
            msg_date = 'La ' + text + ' n\'est pas au format requis (dd/mm/yyyy). | '
    except Exception as e:
        msg_date = f"Une erreur s'est produite lors du remplissage de la {text}: {str(e)} | "
    print(msg_date)
    
    return msg_date
