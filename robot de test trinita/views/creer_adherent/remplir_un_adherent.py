from controllers.adherent_controller import AdherentController
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from views.utils.utils import wait_for_element, capture_screenshot, add_rapport_word
from views.creer_adherent.remplir_telephone import remplir_telephone
from views.creer_adherent.remplir_ville import remplir_ville
from views.creer_adherent.remplir_code_postal import remplir_code_postal
from views.creer_adherent.recherche_adherent_avant_remplir import recherche_adherent_avant_remplir
from views.utils.navigate_to_adherent_section import navigate_to_adherent_section
from selenium.common.exceptions import TimeoutException
from views.creer_contrat.remplir_un_contrat import remplir_un_contrat
from views.utils.ajouter_num_adhe_num_contrat_resultatfeuilleexcel import ajouter_num_adhe_num_contrat_resultatfeuilleexcel
import re
from views.creer_adherent.get_adherent_status import get_adherent_status

excel_path = 'dosexcel/adherent.xlsx'
sheet_adherent = 'adherent'
def remplir_adherent(driver,compteur,adherent):
    ##adherents = AdherentController(excel_path, sheet_adherent).get_adherent_info()
    #for adherent in adherents:
    #compteur=0
    ##adherent= adherents[compteur]

    # rechercher un adherent avant remplir
    recherche_adherent_avant_remplir(driver, adherent,compteur)

    mes_civi = ''
    mes_nom = ''
    mes_naissance = ''
    mes_nom_rue = ''
####################################
    if adherent.civilite is None or not isinstance(adherent.civilite, str) or adherent.civilite.strip() == "":
        mes_civi = 'la civilite n\'a pas acceptée la norme ==> vide. | '
    elif adherent.civilite not in ["Madame", "Monsieur", "Non genré"]:
        mes_civi = 'la civilite n\'a pas creé correctement. | '
    else:
        #remplir civiliter
        combo = wait_for_element(driver, By.ID, "id_title")
        select = Select(combo)
        select.select_by_visible_text(adherent.civilite)
        mes_civi = 'la civilite acceptée la norme. | '
####################################
    #remplir nom
    remplir_nom = wait_for_element(driver, By.XPATH, '//*[@id="id_last_name"]')
    remplir_nom.send_keys(adherent.nom)

    if remplir_nom.get_attribute("value") =='nan':
        mes_nom = 'le champ du nom est invalide ==> vide. | '
    else:
        mes_nom = 'le champ du nom est bien remplir. | '
####################################
    # remplir date de naissance
    try:
        # Convertir la date en chaîne et enlever les espaces
        date_naissance = str(adherent.date_naissance).strip()
    
        # Vérifier le format de la date
        if re.match(r'^\d{2}/\d{2}/\d{4}$', date_naissance):
            remplir_naissance = wait_for_element(driver, By.XPATH, '//*[@id="id_birth_date"]')
            remplir_naissance.send_keys(date_naissance)
            mes_naissance = 'La date de naissance a été remplie avec succès. | '
        else:
            mes_naissance = 'La date de naissance n\'est pas au format requis (dd/mm/yyyy). | '
    except Exception as e:
        mes_naissance = f'Une erreur s\'est produite lors du remplissage de la date de naissance: {str(e)} | '

    print(mes_naissance)

####################################

    capture_screenshot(driver, f"first_fill_screen_adherent_{compteur+1}")
    add_rapport_word('rapport', mes_civi+' '+mes_nom+' '+mes_naissance+f' adherent{compteur+1}', f'screenshots/first_fill_screen_adherent_{compteur+1}.png',compteur) ########
    time.sleep(1)
    # remplir nom de rue
    remplir_nom_rue = wait_for_element(driver, By.XPATH, '//*[@id="id_address_set-0-street_name"]')
    remplir_nom_rue.send_keys(adherent.nom_rue)
    if remplir_nom_rue.get_attribute("value") == 'nan':
        mes_nom_rue = 'le champ du nom de rue est invalide ==> vide. | '
    else:
        mes_nom_rue = 'le champ du nom de rue est bien remplir. | '
    # remplir code postal
    msg_pos= remplir_code_postal(driver, adherent) # fonction pour remplir seulement le code postal
    # remplir ville
    msg_vill = remplir_ville(driver, adherent) # fonction pour remplir seulement le ville
    # remplir telephone
    msg_telephone = remplir_telephone(driver,adherent) # fonction pour remplir seulement le telephone

    capture_screenshot(driver, f"second_fill_screen_adherent_{compteur+1}")
    add_rapport_word('rapport', mes_nom_rue+' '+msg_pos+' '+msg_vill+' '+msg_telephone+f' adherent{compteur+1}', f'screenshots/second_fill_screen_adherent_{compteur+1}.png',compteur) ########

    # submit
    wait_for_element(driver, By.XPATH, '//*[@id="submit-id-submit"]').click()
    # Vérification si l'élément existe avant de prendre la capture d'écran
    try:
        element = wait_for_element(driver, By.XPATH, '//*[@id="delete-adherent-"]/i')
        x='fail'
        if element:
            wait_for_element(driver, By.XPATH, '//*[@id="btn-activate-person activer"]/i').click()
            x= get_adherent_status(driver)
            print(x)
            capture_screenshot(driver, f"submit_successfully_adherent{compteur+1}")
            add_rapport_word('rapport', f'=====>>  SUBMIT ET CREATION ADHERENT {compteur+1} AVEC SUCCES <<=====' , f'screenshots/submit_successfully_adherent{compteur+1}.png',compteur) ########
            numero_adherent = wait_for_element(driver, By.XPATH, '//h3[@data-field="adherent_number"]').text
            #remplir_un_contrat(driver, compteur,adherent,numero_adherent)
        else:
            numero_adherent ='fail'
            add_rapport_word('rapport', f'=====>>  SUBMIT ET CREATION ADHERENT {compteur+1} AVEC ECHEC <<=====' , f'screenshots/submit_successfully_adherent{compteur+1}.png',compteur) ########
            #ajouter_num_adhe_num_contrat_resultatfeuilleexcel('dosexcel/adherent.xlsx', 'resultat', numero_adherent, 'fail', res='KO')

    except TimeoutException:
        print("L'élément 'delete-adherent' n'existe pas, capture ignorée.")
            

    return [x, numero_adherent]

