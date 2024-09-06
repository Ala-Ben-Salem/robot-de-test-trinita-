from views.utils.utils import wait_for_element, capture_screenshot, add_rapport_word
from selenium.webdriver.common.by import By
import time
from controllers.contrat_controller import ContratController
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from views.utils.ajouter_num_adhe_num_contrat_resultatfeuilleexcel import ajouter_num_adhe_num_contrat_resultatfeuilleexcel
import math
import re
from views.creer_contrat.remplir_date_verification import remplir_date_verification
from views.creer_contrat.get_active_status_contrat import get_active_status
excel_path = 'dosexcel/adherent.xlsx'
sheet_contrat = 'contrat'
def remplir_un_contrat(driver, compteur, adherent, numero_adherent, contrat, statut_adher):
    numero_contract = 'fail'

    #wait_for_element(driver, By.XPATH, '//*[@id="btn-activate-person activer"]/i').click()
    time.sleep(1)
    wait_for_element(driver, By.XPATH, '//*[@id="btn-create-contract"]').click()
    capture_screenshot(driver, f"first_step_to_creat_contract_adherent{compteur+1}")
    msg1 = "premier etape: activation adherent avant la création d\'un contrat"
    add_rapport_word('rapport', msg1+' '+f'{compteur+1}' , f'screenshots/first_step_to_creat_contract_adherent{compteur+1}.png', compteur)
###############################################################################
    # Vérifier si le champ 'assureur' est correct
    if contrat.assureur is None or not isinstance(contrat.assureur, str) or contrat.assureur.strip() == "":
        print('Le champ assureur est vide ou incorrect.')
        msg_assureur = "Le champ 'assureur' est vide | "
    elif contrat.assureur not in ["CFDP (Assurance)", "EMOA (Assurance)", "MADP (Assurance)", "MMC (Assurance)", "Mutuelle Mutest (Assurance)"]:
        print('L\'assureur spécifié n\'est pas reconnu. |')
        msg_assureur = "L'assureur spécifié n'est pas reconnu ==> s'ecrire avec erreur. | "
    else:
    # Remplir le champ assureur
        remplir_assureur = wait_for_element(driver, By.ID, "id_insurance")
        if remplir_assureur.tag_name == "select":
            select1 = Select(remplir_assureur)
            select1.select_by_visible_text(contrat.assureur)
            print('L\'assureur a été sélectionné avec succès.')
            msg_assureur = "L'assureur a été sélectionné avec succès. | "
        else:
            print('L\'élément trouvé n\'est pas un <select>.')
            msg_assureur = "L'élément trouvé n'est pas un <select>. | "

###############################################################################
    # Remplir Apporteur d'affaire
    try:
        # Click on the Apporteur d'affaire dropdown
        wait_for_element(driver, By.XPATH, '//*[@id="select2-id_insurance_broker-container"]').click()
    
        # Enter the apporteur d'affaire value
        remplir_Apporteur_affaire = wait_for_element(driver, By.XPATH, '/html/body/span/span/span[1]/input')
        remplir_Apporteur_affaire.send_keys(contrat.apporteur_affaire)
    
        # Select the highlighted option

        fin_click_app = wait_for_element(driver, By.XPATH, '//*[@id="select2-id_insurance_broker-results"]/li[contains(@class, "select2-results__option--highlighted")]')
        time.sleep(2)
        if fin_click_app.is_displayed() and fin_click_app.is_enabled() and remplir_Apporteur_affaire.get_attribute("value")!= 'nan':
            fin_click_app.click()
    
        # Verify the selected Apporteur d'affaire
        selected_option = wait_for_element(driver, By.XPATH, '//*[@id="select2-id_insurance_broker-container"]')
        selected_text = selected_option.get_attribute("textContent")
        msg_apporteur = ''
        if selected_text == '---------':
                print("L'élément de sélection de l'apporteur d'affaire n'a pas été trouvé. ==> vide")
                msg_apporteur = ' | l\'apporteur d\'affaire n\'a pas été trouvé. ==> vide | '
        else:
            print("L'apporteur d'affaire a été sélectionné avec succès.")
            msg_apporteur = ' | l\'apporteur d\'affaire a été sélectionné avec succès | '
    except Exception as e:
        print(f"Une erreur s'est produite lors du remplissage de l'Apporteur d'affaire: pas valide")
        msg_apporteur = ' | l\'apporteur d\'affaire s\'écrit avec erreur ou n\'est pas valide | '

    ###############################################################################################
    #  remplir gamme
    if "succès" in msg_apporteur:
        try:
            wait_for_element(driver, By.XPATH, '//*[@id="div_id_product_range"]/span/span[1]/span').click()
            remplir_gamme = wait_for_element(driver, By.XPATH, '/html/body/span/span/span[1]/input')
            time.sleep(2)
            remplir_gamme.send_keys(contrat.gamme)
            time.sleep(1)

            first_option_gamme = wait_for_element(driver, By.XPATH, '//*[@id="select2-id_product_range-results"]/li[1]')
            time.sleep(3)
            if first_option_gamme.is_displayed() and first_option_gamme.is_enabled() and remplir_gamme.get_attribute("value")!= 'nan':#contrat.gamme is not None:#
                first_option_gamme.click()

            select_text_gamme =wait_for_element(driver, By.XPATH, '//*[@id="div_id_product_range"]/span/span[1]/span').get_attribute("textContent")
            if select_text_gamme == '---------':
                if contrat.gamme is None or (isinstance(contrat.gamme, float) and math.isnan(contrat.gamme)):
                    print("L'élément de sélection de gamme n'a pas été trouvé. ==> vide")
                    msg_gamme = ' | Gamme n\'a pas été trouvé. ==> vide | '
                else:
                    print('Gamme s\'ecrire avec erreur')
                    msg_gamme = 'Gamme s\'ecrire avec erreur | '
            else:
                print("Gamme a été sélectionné avec succès.")
                msg_gamme = ' | Gamme a été sélectionné avec succès | '
        except Exception as e:
            print(f"Une erreur s'est produite lors du remplissage de gamme: {str(e)}")
            msg_gamme = ' | Gamme s\'écrit avec erreur ou n\'est pas valide | '

    else:
        print('Remplissage de gamme annulé car Apporteur d\'affaire n\'a pas été rempli correctement.==> car c\'est sont proportionnel')
        msg_gamme = 'Remplissage de gamme annulé car Apporteur d\'affaire n\'a pas été rempli correctement.==> car c\'est sont proportionnel | '

######################################################################################################
    # remplir type de vente
    if contrat.type_vente is None or not isinstance(contrat.type_vente, str) or contrat.type_vente.strip() == "":
        print('Le champ type de vente est vide.')
        msg_type_vente = "Le champ 'type de vente' est ==> vide | "
    elif contrat.type_vente not in ["Vente face à face", "Vente à distance sollicité par le client", "Vente à distance prospection conseiller"]:
        print('Le type de vente spécifié n\'est pas reconnu.=> s\'ecrire avec erreur. MAIS par defaur Vente face à face s\'exisite |')
        msg_type_vente = "Le type de vente spécifié n'est pas reconnu ==> s'écrire avec erreur. MAIS par defaur Vente face à face s\'exisite | "
    else:
        # Remplir le champ type de vente
        remplir_type_vente = wait_for_element(driver, By.ID, "id_sale_type")
        if remplir_type_vente.tag_name == "select":
            select2 = Select(remplir_type_vente)
            select2.select_by_visible_text(contrat.type_vente)
            print('Le type de vente a été sélectionné avec succès.')
            msg_type_vente = "Le type de vente a été sélectionné avec succès. | "
        else:
            print('L\'élément trouvé n\'est pas un <select>.')
            msg_type_vente = "L'élément trouvé n'est pas un <select>. | "

######################################################################################################
    capture_screenshot(driver, f"first_fill_contract_adherent{compteur+1}")
    add_rapport_word('rapport',msg_assureur+ ' '+msg_apporteur+' '+msg_gamme+' '+msg_type_vente+ f' ==> contrat {compteur+1}' , f'screenshots/first_fill_contract_adherent{compteur+1}.png', compteur)
############################################################################################################
    msg_date_souscription = remplir_date_verification(driver, contrat.date_souscription, '//*[@id="id_signature_date"]', 'date de souscription')
    msg_date_effective = remplir_date_verification(driver, contrat.date_effective, '//*[@id="id_effective_date"]', 'date de effective')

    r"""
#remplir Date de souscription
    try:
        # Convertir la date en chaîne et enlever les espaces
        date_souscription = str(contrat.date_souscription).strip()
    
        # Vérifier le format de la date
        if re.match(r'^\d{2}/\d{2}/\d{4}$', date_souscription):
            remplir_date_souscription = wait_for_element(driver, By.XPATH, '//*[@id="id_signature_date"]')
            remplir_date_souscription.send_keys(date_souscription)
            msg_date_souscription = 'La date de souscription a été remplie avec succès. | '
        else:
            msg_date_souscription = 'La date de souscription n\'est pas au format requis (dd/mm/yyyy). | '
    except Exception as e:
        msg_date_souscription = f"Une erreur s'est produite lors du remplissage de la date de souscription: {str(e)} | "
    print(msg_date_souscription)

    # remplir Date effective
    try:
        # Convertir la date en chaîne et enlever les espaces
        date_effective = str(contrat.date_effective).strip()
        # Vérifier le format de la date
        if re.match(r'^\d{2}/\d{2}/\d{4}$', date_effective):
            remplir_date_effective = wait_for_element(driver, By.XPATH, '//*[@id="id_effective_date"]')
            remplir_date_effective.send_keys(date_effective)
            msg_date_effective = "La date effective a été remplie avec succès. | "
        else:
            msg_date_effective = "La date effective n'est pas au format requis (dd/mm/yyyy). | "
    except Exception as e:
        msg_date_effective = f"Une erreur s'est produite lors du remplissage de la date effective: {str(e)} | "
    print(msg_date_effective)
    """
    
    
    time.sleep(1)
    capture_screenshot(driver, f"second_fill_contract_adherent{compteur+1}")
    add_rapport_word('rapport',msg_date_souscription+' '+msg_date_effective+ f' ==> contrat {compteur+1}' , f'screenshots/second_fill_contract_adherent{compteur+1}.png', compteur)

    #####################  if all above are right so we can continuous else we can't ############################
    if "succès" in msg_assureur and  "succès" in msg_apporteur and "succès" in msg_gamme and "succès" in msg_date_souscription and "succès" in msg_date_effective:
        # click the first valider contrat
        wait_for_element(driver, By.XPATH, '//*[@id="submit-id-submit"]').click()

        ################## information paiement  #########################
        # Mode de fractionnement
        if contrat.mode_fractionnement is None or not isinstance(contrat.mode_fractionnement, str) or contrat.mode_fractionnement.strip() == "":
            print('Le champ mode de fractionnement est vide.')
            msg_fractionnement = "Le champ 'mode de fractionnement' est vide. | "
        elif contrat.mode_fractionnement not in ["Mensuel"]:
            print("Le mode de fractionnement spécifié n'est pas reconnu. |")
            msg_fractionnement = "Le mode de fractionnement spécifié n'est pas reconnu ==> s'écrire avec erreur. | "
        else:
            # Remplir le champ mode de fractionnement
            remplir_mode_fractionnement = wait_for_element(driver, By.ID, "id_mode_splitting")
            if remplir_mode_fractionnement.tag_name == "select":
                select3 = Select(remplir_mode_fractionnement)
                select3.select_by_visible_text(contrat.mode_fractionnement)
                print("Le mode de fractionnement a été sélectionné avec succès.")
                msg_fractionnement = "Le mode de fractionnement a été sélectionné avec succès. | "
            else:
                print("L'élément trouvé n'est pas un <select>.")
                msg_fractionnement = "L'élément trouvé n'est pas un <select>. | "

        #####################################################################################
        # Jour de prélèvement
        if contrat.jour_prelevement is None or not isinstance(contrat.jour_prelevement, str) or contrat.jour_prelevement.strip() == "":
            print("Le champ jour de prélèvement est vide.")
            msg_prelevement = "Le champ 'jour de prélèvement' est vide. | "
        elif contrat.jour_prelevement not in ['05', '08', '12']:
            print("Le jour de prélèvement spécifié n'est pas reconnu. |")
            msg_prelevement = "Le jour de prélèvement spécifié n'est pas reconnu ==> s'écrire avec erreur. | "
        else:
            remplir_jour_prelevement = wait_for_element(driver, By.ID, "id_withdrawal_day")
            # Remplir le champ jour de prélèvement
            if remplir_jour_prelevement.tag_name == "select":
                select4 = Select(remplir_jour_prelevement)
                select4.select_by_visible_text(contrat.jour_prelevement)
                print("Le jour de prélèvement a été sélectionné avec succès.")
                msg_prelevement = "Le jour de prélèvement a été sélectionné avec succès. | "
            else:
                print("L'élément trouvé n'est pas un <select>.")
                msg_prelevement = "L'élément trouvé n'est pas un <select>. | "

        ######################################################################################
        # Mode de paiement
        if contrat.mode_paiement is None or not isinstance(contrat.mode_paiement, str) or contrat.mode_paiement.strip() == "":
            print('Le champ mode de paiement est vide MAIS prendre par defaut Prélèvement automatique.')
            msg_mode_paiement = "Le champ 'mode de paiement' est vide MAIS prendre par defaut Prélèvement automatique  | "
        elif contrat.mode_paiement not in ["Prélèvement automatique", "En espèces", "Chèque", "Carte de crédit", "Paypal", "ANV", "Virement bancaire", "Dérogation"]:  # Replace with actual options
            print('Le mode de paiement spécifié n\'est pas reconnu.')
            msg_mode_paiement = "Le mode de paiement spécifié n'est pas reconnu ==> s'écrire avec erreur. | "
        else:
            # Remplir le champ mode de paiement
            remplir_mode_paiement = wait_for_element(driver, By.ID, "id_payment_mode")
            if remplir_mode_paiement.tag_name == "select":
                select5 = Select(remplir_mode_paiement)
                select5.select_by_visible_text(contrat.mode_paiement)
                print('Le mode de paiement a été sélectionné avec succès.')
                msg_mode_paiement = "Le mode de paiement a été sélectionné avec succès. | "
            else:
                print('L\'élément trouvé n\'est pas un <select>.')
                msg_mode_paiement = "L'élément trouvé n'est pas un <select>. | "

        #####################################################################################

        capture_screenshot(driver, f"third_fill_contract_adherent{compteur+1}")
        add_rapport_word('rapport', msg_fractionnement+' '+msg_prelevement+' '+msg_mode_paiement+ f' ==> contrat {compteur+1}', f'screenshots/third_fill_contract_adherent{compteur+1}.png', compteur)


        # checkbox Ajouter un nouvel IBAN
        try:
            checkbox = wait_for_element(driver, By.XPATH, '//*[@id="id_add_iban"]')
            if not checkbox.is_selected():
                checkbox.click()
                # remplir IBAN
                ########################################################################
                # Validation for a French IBAN
                if contrat.iban is None or not isinstance(contrat.iban, str) or contrat.iban.strip() == "":
                    print('Le champ IBAN est vide.')
                    msg_iban = "Le champ 'IBAN' est vide | "
                elif not re.match(r'^FR\d{12}[A-Z0-9]{11}\d{2}$', contrat.iban.strip()):
                    print('Le format de l\'IBAN spécifié n\'est pas valide pour un IBAN français.')
                    msg_iban = "Le format de l'IBAN spécifié n'est pas valide pour un IBAN français ==> s'écrire avec erreur. | "
                else:
                    # Remplir le champ IBAN
                    remplir_iban = wait_for_element(driver, By.XPATH, '//*[@id="id_new_iban"]')
                    remplir_iban.send_keys(contrat.iban)
                    print('L\'IBAN a été renseigné avec succès.')
                    msg_iban = "L'IBAN a été renseigné avec succès. | "
                ##################################################################################
                time.sleep(1)
                # remplir Banque
                wait_for_element(driver, By.XPATH, '//*[@id="select2-id_new_bank-container"]').click()
                remplir_new_banque = wait_for_element(driver, By.XPATH, '/html/body/span/span/span[1]/input')
                remplir_new_banque.send_keys(contrat.banque)
                fin_click_valid_banque = wait_for_element(driver, By.XPATH, '//*[@id="select2-id_new_bank-results"]/li[1]')
                time.sleep(2)
                fin_click_valid_banque.click()
                time.sleep(1)
                # Nom du titulaire du compte
                remplir_nom_tutilaire = wait_for_element(driver, By.XPATH, '//*[@id="id_new_bank_acc_account_holder_first_name"]')
                remplir_nom_tutilaire.send_keys(adherent.nom)
                if remplir_nom_tutilaire.get_attribute("value") =='nan':
                    msg_nom = 'le champ du nom est invalide ==> vide. | '
                else:
                    msg_nom = 'le champ du nom est bien remplir. | '
                print(msg_nom)
                # prenom du titulaire du compte
                remplir_prenom_tutilaire = wait_for_element(driver, By.XPATH, '//*[@id="id_new_bank_acc_account_holder_last_name"]')
                remplir_prenom_tutilaire.send_keys(adherent.prenom)
                if remplir_prenom_tutilaire.get_attribute("value") =='nan':
                    msg_prenom = 'le champ du prenom est invalide ==> vide. | '
                else:
                    msg_prenom = 'le champ du prenom est bien remplir. | '
                print(msg_prenom)
                time.sleep(3)

        except Exception as e:
            print(f"Une erreur s'est produite lors de l'interaction avec la checkbox 'Ajouter un nouvel IBAN': {str(e)}")
        capture_screenshot(driver, f"last_fill_contract_adherent{compteur+1}")
        add_rapport_word('rapport', msg_iban+' '+msg_nom+' '+msg_prenom+ f' ==> contrat {compteur+1}' , f'screenshots/last_fill_contract_adherent{compteur+1}.png', compteur)

        # submit contrat final
        wait_for_element(driver, By.XPATH, '//*[@id="submit-id-submit"]').click()

        feuille_contrat= wait_for_element(driver, By.XPATH, '//*[@id="btn-draft-to-pending-contract"]/i')
        
        if feuille_contrat:
            x=get_active_status(driver)
            capture_screenshot(driver, f"DONE_contract_adherent{compteur+1}")
            add_rapport_word('rapport', f'==========>> CREATION CONTRAT {compteur+1} AVEC SUCCES <<===========', f'screenshots/DONE_contract_adherent{compteur+1}.png', compteur)
            numero_contract = wait_for_element(driver, By.XPATH, '//span[@id="contract-number"]').text
            print(f"num contrat ==> {numero_contract}")
            ajouter_num_adhe_num_contrat_resultatfeuilleexcel('dosexcel/adherent.xlsx', 'resultat', numero_adherent=numero_adherent, statut_adherent= statut_adher, numero_contrat=numero_contract,statut_contrat=x , res='OK', commentaire='création adherent et contrat avec succés')
    
            #Ajouter le souscripteur principal en tant qu'assuré
            wait_for_element(driver, By.XPATH, '//*[@id="main"]/article[1]/div/section[2]/fieldset[3]/a').click()
            # remplir Produit
            remplir_produit = wait_for_element(driver, By.ID, "id_product")
            select6 = Select(remplir_produit)
            select6.select_by_value('43')

            wait_for_element(driver, By.XPATH, '//*[@id="submit-id-submit"]').click()

            wait_for_element(driver, By.XPATH, '//*[@id="main"]/article[1]/div/section[2]/fieldset[3]/div/div/table/tbody/tr/td[12]/small/a')
            element_besoin = driver.find_element(By.XPATH, '//*[@id="subscriber-fieldset"]')
            driver.execute_script("arguments[0].scrollIntoView(true);", element_besoin)
            capture_screenshot(driver, f"ajouter_Assures_contract_adherent{compteur+1}")

            # bouton pre_valider
            #wait_for_element(driver, By.XPATH, '//*[@id="btn-draft-to-pending-contract"]').click()
        else:
            ajouter_num_adhe_num_contrat_resultatfeuilleexcel('dosexcel/adherent.xlsx', 'resultat', numero_adherent=numero_adherent, statut_adherent=statut_adher, numero_contrat='fail', statut_contrat='fail', res='KO', commentaire='création adherent et contrat')
            capture_screenshot(driver, f"capture_fail_contract_adherent{compteur+1}")
            add_rapport_word('rapport', f'il y a des ou un champ(s) vide(s) ou IBAN existe déjà sous un autre nom ==> donc il ne peut pas creer un contrat {compteur+1}', f'screenshots/capture_fail_contract_adherent{compteur+1}.png', compteur)
    else:
        add_rapport_word('rapport', f'il y a des ou un champ(s) vide(s) ==> donc il ne peut pas suivre les procédures de la creation contrat {compteur+1}',  f'screenshots/second_fill_contract_adherent{compteur+1}.png', compteur)
    return numero_contract