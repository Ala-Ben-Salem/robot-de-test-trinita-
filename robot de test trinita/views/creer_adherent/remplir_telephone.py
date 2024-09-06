from views.utils.utils import wait_for_element
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def remplir_telephone(driver, adherent):
    # Vérification du type de téléphone
    if adherent.tel_type is None or not isinstance(adherent.tel_type, str) or adherent.tel_type.strip() == "":
        print('Le type de téléphone n\'a pas accepté la norme ==> vide.')
        msg_type_tel = "Le type de téléphone n'a pas accepté la norme ==> vide. | "
    elif adherent.tel_type not in ["Fixe", "Domicile", "Portable", "Pro", "Fax"]:
        msg_type_tel = "Le type de téléphone n'a pas été créé correctement. | "
        print('Le type de téléphone n\'a pas été créé correctement.')
    else:
        # Remplir le type de téléphone
        remplir_type_telephone = wait_for_element(driver, By.ID, "id_phone_set-0-type")
        select = Select(remplir_type_telephone)
        select.select_by_visible_text(adherent.tel_type)
        print('type de telephone rempli avec succès ')
        msg_type_tel = ' type de telephone rempli avec succès | '

    # Remplir le préfixe
    prefixe_str = str(adherent.prefixe).strip()
    remplir_prefix = wait_for_element(driver, By.XPATH, '//*[@id="id_phone_set-0-country_prefix"]')
    if prefixe_str.isdigit():
        remplir_prefix.clear()
        remplir_prefix.send_keys(adherent.prefixe)
        print("Le préfixe a été rempli avec succès.")
        msg_prefix = ' Le préfixe a été rempli avec succès | '
    else:
        print("Le préfixe est vide ou incorrect mais prendre automatiqument 33. Veuillez vérifier.")
        msg_prefix = ' Le préfixe est vide ou incorrect mais prendre automatiqument 33. Veuillez vérifier | '

    # Remplir le numéro de téléphone
    remplir_numero_tel = wait_for_element(driver, By.XPATH, '//*[@id="id_phone_set-0-number"]')
    if adherent.numero_telephone.startswith(('06', '07')) and len(adherent.numero_telephone) == 10:
        remplir_numero_tel.send_keys(adherent.numero_telephone)
        print("Le numéro de téléphone a été rempli avec succès.")
        msg_numero_tel = ' Le numéro de téléphone a été rempli avec succès. | '
    else:
        print("Le numéro de téléphone est incorrect. Il doit commencer par 06 ou 07 et contenir 10 chiffres.")
        msg_numero_tel = ' Le numéro de téléphone est incorrect. Il doit commencer par 06 ou 07 et contenir 10 chiffres. | '

    return msg_type_tel+msg_prefix+msg_numero_tel