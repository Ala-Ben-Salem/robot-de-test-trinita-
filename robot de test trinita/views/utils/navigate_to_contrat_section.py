from selenium.webdriver.common.by import By
from views.utils.utils import wait_for_element, capture_screenshot, add_rapport_word
import time


def navigate_to_contrat_section(driver, compteur):
    print('hello contrat')

    first_button = wait_for_element(driver, By.XPATH, '/html/body/div[1]/div/div/nav[1]/section/ul[1]/li[4]/a')
    first_button.click()
    capture_screenshot(driver, "first_button_click_to_went_contrat_section")

    time.sleep(1)
    second_button = wait_for_element(driver, By.XPATH, '/html/body/div[1]/div/div/nav[1]/section/ul[1]/li[4]/ul/li[4]')
    
    second_button.click()

    capture_screenshot(driver, "second_button_click_to_went_contrat_section")
    add_rapport_word('rapport', 'entrer dans l\'espace contrat', 'screenshots/second_button_click_to_went_contrat_section.png', compteur)
