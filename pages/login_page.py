from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import random

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def authorisation(self, login_email, password):

    # Filling login field
        login_field = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ajax_login_popup_email']")))
        login_field.send_keys(login_email)
        time.sleep(random.uniform(1.0, 2.0))
        print("Input login")

    # Filling password field
        password_field = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='ajax_login_popup_pass']")))
        password_field.send_keys(password)
        time.sleep(random.uniform(1.0, 2.0))
        print("Input password")

    # Submitting
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@name='submit']")))
        login_button.click()
        time.sleep(random.uniform(1.0, 2.5))
        print("Input password")
