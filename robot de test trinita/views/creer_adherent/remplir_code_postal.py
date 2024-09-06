from views.utils.utils import wait_for_element
from selenium.webdriver.common.by import By
import time



def remplir_code_postal(driver, adherent):
    wait_for_element(driver, By.XPATH, '//*[@id="select2-id_address_set-0-zip_code-container"]').click()
    remplir_code_postal = wait_for_element(driver, By.XPATH, '/html/body/span/span/span[1]/input')
    remplir_code_postal.send_keys(adherent.code_postal)
    time.sleep(1)
    first_option_cp = wait_for_element(driver, By.XPATH, '//*[@id="select2-id_address_set-0-zip_code-results"]/li')
    first_option_cp.click()

    msg_code_postal = ''
    # Vérifier la valeur du champ de code postal
    selected_option = wait_for_element(driver, By.XPATH, '//*[@id="select2-id_address_set-0-zip_code-container"]')
    
    if selected_option:
        selected_text = selected_option.get_attribute("textContent").strip()
        # Vérifier si selected_text est numérique avant de le convertir en entier
        if selected_text.isdigit():
            selected_text = int(selected_text)

            if selected_text == adherent.code_postal:
                print('La première option du code postal a été sélectionnée avec succès.')
                msg_code_postal = ' | code postal a été sélectionné avec succès | '
            else:
                print('Échec de la sélection de la première option du code postal.')
                msg_code_postal = ' | code postal s\'est écrit avec erreur donc n\'a pas compatible avec ville | '
        elif adherent.code_postal is None:
            print('Le texte sélectionné n\'est pas un code postal valide.')
            msg_code_postal = ' | code postal est vide | '
        else:
            print('Le texte sélectionné n\'est pas un code postal valide hhh.')
            msg_code_postal = ' | code postal est ecrire avec lettre donc le champ rest vide | '
    else:
        print('L\'élément de sélection du code postal n\'a pas été trouvé.')
        msg_code_postal = ' | code postal n\'a pas été trouvé. | '


    return msg_code_postal