from selenium.webdriver.common.by import By

def get_adherent_status(driver):
    #  l'élément brouillon
    draft_element = driver.find_element(By.ID, "draft-switch")
    #l'élément active
    active_element = driver.find_element(By.ID, "active-switch")
    
    # Vérifier si le statut "Brouillon" est selectionné
    if "secondary" not in draft_element.get_attribute("class"):
        status = draft_element.text.strip()  # Brouillon
    #  statut "Actif" qui est selectionné
    elif "secondary" not in active_element.get_attribute("class"):
        status = active_element.text.strip()  # "Actif"
    else:
        status = "Unknown"

    return status
