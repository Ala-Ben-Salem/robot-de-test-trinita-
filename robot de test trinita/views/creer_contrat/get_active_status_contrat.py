from selenium.webdriver.common.by import By

def get_active_status(driver):
    # Récupérer les éléments correspondant aux statuts
    refused_element = driver.find_element(By.ID, "refused-switch")
    draft_element = driver.find_element(By.ID, "draft-switch")
    pending_element = driver.find_element(By.ID, "pending-switch")
    open_element = driver.find_element(By.ID, "open-switch")
    closed_element = driver.find_element(By.ID, "closed-switch")

    # Initialiser la variable status à None
    status = None

    # Vérifier quel statut est actif en vérifiant l'absence de la classe "secondary"
    if "secondary" not in refused_element.get_attribute("class"):
        status = refused_element.text.strip()  # "Refusé"
    elif "secondary" not in draft_element.get_attribute("class"):
        status = draft_element.text.strip()  # "Brouillon"
    elif "secondary" not in pending_element.get_attribute("class"):
        status = pending_element.text.strip()  # "Pré validé"
    elif "secondary" not in open_element.get_attribute("class"):
        status = open_element.text.strip()  # "Ouvert"
    elif "secondary" not in closed_element.get_attribute("class"):
        status = closed_element.text.strip()  # "Fermé"

    # Retourner le statut actif
    return status

