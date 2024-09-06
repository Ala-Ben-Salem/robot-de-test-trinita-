import threading
import time
from controllers.adherent_controller import AdherentController
from controllers.contrat_controller import ContratController
from views.creer_adherent.remplir_un_adherent import remplir_adherent
from views.creer_contrat.remplir_un_contrat import remplir_un_contrat
from views.utils.trinita_view import open_google_and_search, click_trinita_link, close_browser, driver_fonct
from views.utils.page_login_trinita import login_trinita
from views.utils.navigate_to_adherent_section import navigate_to_adherent_section
from controllers.param_controller import ParamController
from views.utils.ajouter_num_adhe_num_contrat_resultatfeuilleexcel import ajouter_num_adhe_num_contrat_resultatfeuilleexcel
from views.creer_contrat.test_validation_solde import test_validation_solde
from views.utils.email_envoyer_rapport import send_email_with_attachment
from rapport.supprimer_fichier import supprimer_fichiers_word
from views.utils.utils import add_rapport_word, capture_screenshot, clear_screenshots_folder
from views.utils.navigate_to_contrat_section import navigate_to_contrat_section
from controllers.testvalidation_controller import TestvalidationController
from views.testvalidation.rechercher_contrat_ouvert import rechercher_contrat_ouvert
from views.testvalidation.somme_table_ventilation import somme_table_ventilation
from views.testvalidation.test_validation_solde_attendre_solde_contrat import test_validation_solde_attendre_solde_contrat
from views.testvalidation.test_validation_solde_contrat_solde_ttc import test_validation_solde_contrat_solde_ttc
from views.testvalidation.update_excel_sheet_testvalidation import update_excel_sheet_testvalidation

def gerer_adherent(adherent, contrat, param, compteur, testvalidation):
        profile_path = f"C:\\Users\\alabe\\OneDrive\\Bureau\\rapport de stage 3B14\\robot de test trinita\\chrome_profile_{compteur}"
        driver = driver_fonct(profile_path)
        open_google_and_search(driver, param.url)
        click_trinita_link(driver, param.url)
        login_trinita(driver, param.login, param.psw, compteur)
        time.sleep(2)
        my_option = param.option
        match my_option:
                case 'creation_adherent':
                        navigate_to_adherent_section(driver,compteur)
                        time.sleep(2)
                        res_remplir_adh = remplir_adherent(driver, compteur, adherent)
                        numero_adherent = res_remplir_adh[1]
                        statut_adher = res_remplir_adh[0]
                        print(numero_adherent)
                        time.sleep(3)
                        if numero_adherent != 'fail':
                                print('creation adherent avec succès')
                                ajouter_num_adhe_num_contrat_resultatfeuilleexcel('dosexcel/adherent.xlsx', 'resultat', numero_adherent=numero_adherent, statut_adherent= statut_adher, numero_contrat='-----------', statut_contrat='----------' ,  res='OK',commentaire='seulement creation adherent !')
                        else:
                                print('creation adherent fail')
                                ajouter_num_adhe_num_contrat_resultatfeuilleexcel('dosexcel/adherent.xlsx', 'resultat', numero_adherent=numero_adherent, statut_adherent= 'fail', numero_contrat='-----------', statut_contrat='----------' , res='KO', commentaire='seulement creation adherent !')
                
                case 'creation_adherent_contrat':
                        navigate_to_adherent_section(driver,compteur)
                        time.sleep(2)
                        res_remplir_adh = remplir_adherent(driver, compteur, adherent)
                        numero_adherent = res_remplir_adh[1]
                        statut_adher = res_remplir_adh[0]
                        print(numero_adherent)
                        time.sleep(3)
                        if numero_adherent == 'fail':
                                print('creation adherent fail donc n\'a pas d\'un creation contrat')
                                ajouter_num_adhe_num_contrat_resultatfeuilleexcel('dosexcel/adherent.xlsx', 'resultat', numero_adherent=numero_adherent,  statut_adherent='fail',numero_contrat='----------' , statut_contrat='----------', res='KO', commentaire='adherent fail donc n\'a pas contrat')
                        else:
                                numero_contrat = remplir_un_contrat(driver, compteur, adherent, numero_adherent, contrat, statut_adher)
                                print(numero_contrat)
                
                case 'creation_adherent_contrat_test':
                        navigate_to_adherent_section(driver, compteur)
                        time.sleep(2)
                        res_remplir_adh = remplir_adherent(driver, compteur, adherent)
                        numero_adherent = res_remplir_adh[1]
                        statut_adher = res_remplir_adh[0]                        
                        print(numero_adherent)
                        time.sleep(3)
                        if numero_adherent == 'fail':
                                print('creation adherent fail donc n\'a pas d\'un creation contrat')
                                ajouter_num_adhe_num_contrat_resultatfeuilleexcel('dosexcel/adherent.xlsx', 'resultat', numero_adherent=numero_adherent,  statut_adherent='fail',numero_contrat='----------' , statut_contrat='----------', res='KO', commentaire='adherent fail donc n\'a pas contrat')
                        else:
                                numero_contrat = remplir_un_contrat(driver, compteur, adherent, numero_adherent, contrat)
                                print(numero_contrat)
                                if numero_contrat != 'fail':
                                        test_validation_solde(driver, compteur, contrat)
                                else:
                                        print("creation contrat fail donc pas de test de validation de solde")
                                        capture_screenshot(driver, f"Echec_Solde__de__contrat{compteur}")
                                        add_rapport_word('rapport', 'creation contrat fail donc pas de test de validation de solde', f'screenshots/Echec_Solde__de__contrat{compteur}.png')
                
                case 'test_validation_ventilation_technique':
                        navigate_to_contrat_section(driver, compteur)
                        print('done contrat section')
                        warning =rechercher_contrat_ouvert(driver, testvalidation, compteur)
                        if warning ==None:
                                somme_ttc = somme_table_ventilation(driver, compteur)
                                print(f"La somme des montants mensuels (TTC) est : {somme_ttc:.2f} €")
                                resutlat_attendre_contrat = test_validation_solde_attendre_solde_contrat(driver, compteur, testvalidation)
                                resutlat_ttc_contrat = test_validation_solde_contrat_solde_ttc(driver, compteur, somme_ttc)
                                update_excel_sheet_testvalidation(resutlat_attendre_contrat, somme_ttc, testvalidation)
                        else:
                                print(warning)
                case _:
                        print('AUCUNE OPTION SOUS CETTE NOM.')
                        return "AUCUNE OPTION SOUS CETTE NOM."
        close_browser(driver)
def main():

        excel_path = 'dosexcel/adherent.xlsx'
        sheet_adherent = 'adherent'
        adherent_controller = AdherentController(excel_path, sheet_adherent)
        sheet_contrat = 'contrat'
        contrat_controller = ContratController(excel_path, sheet_contrat)
        sheet_param = 'param'
        param_controller = ParamController(excel_path, sheet_param)
        sheet_testvalidation = 'testvalidation'
        testvalidation_controller = TestvalidationController(excel_path, sheet_testvalidation)

        try:
                adherents = adherent_controller.get_adherent_info()
                contrats = contrat_controller.get_contrat_info()
                params = param_controller.get_param_info()
                param = params[0]
                testvalidations = testvalidation_controller.get_testvalidation_info()


                threads = []
                #for compteur, testvalidation in enumerate(testvalidations):
                for compteur, adherent in enumerate(adherents):
                        contrat = contrats[compteur] if compteur < len(contrats) else None
                        testvalidation = testvalidations[compteur] if compteur < len(testvalidations) else None
                        thread = threading.Thread(target=gerer_adherent, args=(adherent, contrat, param, compteur, testvalidation))
                        threads.append(thread)
                        thread.start()

                for thread in threads:
                        thread.join()

                send_email_with_attachment(subject="Rapport Final robot de test trinita selenuim", body="Veuillez trouver ci-joint le rapport final.", to_email="bensalem.ala@esprit.tn", attachment_folder="rapport")
                supprimer_fichiers_word("rapport")
                clear_screenshots_folder('screenshots')

                time.sleep(2)

        finally:
                print('enfin hmd')
if __name__ == '__main__':
        main()
