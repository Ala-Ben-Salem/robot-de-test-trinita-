from selenium.webdriver.common.by import By
from views.utils.utils import wait_for_element, capture_screenshot, add_rapport_word


def login_trinita(driver,login, psw, compteur):
    user_field = wait_for_element(driver, By.XPATH, '//*[@id="id_username"]',timeout=5)
    if user_field:
        user_field.send_keys(login)

        pass_field = wait_for_element(driver, By.XPATH, '//*[@id="id_password"]')
        pass_field.send_keys(psw)

        capture_screenshot(driver, "login_trinita")
        add_rapport_word('rapport', 'login sur trinita', 'screenshots/login_trinita.png',compteur) ########
        wait_for_element(driver, By.XPATH, '//*[@id="submit-id-submit"]').click()
        wait_for_element(driver, By.XPATH, '/html/body/div[1]/div/div/nav[1]/section/ul[1]/li[1]/a')
        capture_screenshot(driver, "home_trinita")
        add_rapport_word('rapport', 'home trinita', 'screenshots/home_trinita.png',compteur) ########
    else:
        print('trinita a ete sauvegarder')