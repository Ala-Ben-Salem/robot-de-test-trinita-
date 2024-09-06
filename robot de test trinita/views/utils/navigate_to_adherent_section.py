from selenium.webdriver.common.by import By
from views.utils.utils import wait_for_element, capture_screenshot, add_rapport_word
import time


def navigate_to_adherent_section(driver, compteur):
    first_button = wait_for_element(driver, By.XPATH, '/html/body/div[1]/div/div/nav[1]/section/ul[1]/li[1]/a')
    first_button.click()
    capture_screenshot(driver, "first_button_click")

    time.sleep(1)
    second_button = wait_for_element(driver, By.XPATH, '/html/body/div[1]/div/div/nav[1]/section/ul[1]/li[1]/ul/li[3]/a')
    
    # utuliser JavaScript pour cliqueé
    driver.execute_script("arguments[0].click();", second_button)
    
    capture_screenshot(driver, "second_button_click")
    add_rapport_word('rapport', 'entrer dans l\'espace de creation adherent', 'screenshots/second_button_click.png', compteur)
