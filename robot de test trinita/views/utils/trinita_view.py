from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from views.utils.utils import wait_for_element, capture_screenshot, add_rapport_word

# Set up Selenium WebDriver (using Chrome)
def driver_fonct(profile_path):
    #chrome_options = Options()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument(f"user-data-dir={profile_path}")  #r"user-data-dir=C:\Users\alabe\OneDrive\Bureau\rapport de stage 3B14\robot de test trinita\chrome_profile"
    service = Service(ChromeDriverManager().install())

    #driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    return driver


def open_google_and_search(driver,url):
    driver.get("https://www.google.com")
    search_box = wait_for_element(driver, By.NAME, "q")
    search_box.send_keys(url)
    search_box.send_keys(Keys.RETURN)
    capture_screenshot(driver, "google_search")


def click_trinita_link(driver, url):
    driver.get(url)
    capture_screenshot(driver, "trinita_link")


def close_browser(driver):
    driver.quit()
















'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from views.utils import wait_for_element, capture_screenshot
import time

class TrinitaView:
    def __init__(self):
        # Set up Selenium WebDriver (using Chrome)
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(), options=chrome_options)

    def open_google_and_search(self):
        """Open Google and search for the Trinita website."""
        self.driver.get("https://www.google.com")
        search_box = wait_for_element(self.driver, By.NAME, "q")
        search_box.send_keys("https://dev.back-office.as-solutions.cloud.geoprod.com/")
        search_box.send_keys(Keys.RETURN)
        capture_screenshot(self.driver, "google_search")

    def click_trinita_link(self):
        self.driver.get("https://dev.back-office.as-solutions.cloud.geoprod.com/")
        capture_screenshot(self.driver, "trinita_link")

    def login_trinita(self):
        #user_field=self.driver.find_element(By.XPATH, '//*[@id="id_username"]')
        user_field=wait_for_element(self.driver, By.XPATH, '//*[@id="id_username"]')
        user_field.send_keys("robot_test")

        pass_field=wait_for_element(self.driver, By.XPATH, '//*[@id="id_password"]')
        pass_field.send_keys("Agss21@9!.bn")

        capture_screenshot(self.driver, "login_trinita")
        wait_for_element(self.driver, By.XPATH, '//*[@id="submit-id-submit"]').click()
        wait_for_element(self.driver, By.XPATH, '/html/body/div[1]/div/div/nav[1]/section/ul[1]/li[1]/a')
        capture_screenshot(self.driver, "home_trinita")



    def navigate_to_adherent_section(self):
        """Navigate to the adherent section on the Trinita website."""
        first_button = wait_for_element(self.driver, By.XPATH, '/html/body/div[1]/div/div/nav[1]/section/ul[1]/li[1]/a')
        first_button.click()
        capture_screenshot(self.driver, "first_button_click")

        second_button = wait_for_element(self.driver, By.XPATH, '/html/body/div[1]/div/div/nav[1]/section/ul[1]/li[1]/ul/li[3]/a')
        second_button.click()
        capture_screenshot(self.driver, "second_button_click")

    def close(self):
        """Close the browser."""
        self.driver.quit()
'''