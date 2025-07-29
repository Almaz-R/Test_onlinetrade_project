from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import random

class CartPage:
    def __init__(self, driver):
        self.driver = driver
    # Locators
    cart_button = (By.XPATH, "//span[@class='ic__set ic__set__multicartWhite']")

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()
        time.sleep(random.uniform(1.0, 2.0))

