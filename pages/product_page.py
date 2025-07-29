from selenium.webdriver.common.by import By
import time
import random

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
    # Locators
    adding_button = (By.XPATH, "//a[@title='Купить Смартфон Samsung Galaxy A16 4/128GB Черный']")
    close_modal_window = (By.XPATH, "//div[@class='js__animateCover']//a[@title='Закрыть окно']")

    def add_to_cart(self):
        self.driver.execute_script("window.scrollTo(0, 200);")
        time.sleep(random.uniform(1.0, 2.0))
        self.driver.find_element(*self.adding_button).click()
        time.sleep(random.uniform(1.5, 2.0))

    def close_window(self):
    # closing modal window
        self.driver.find_element(*self.close_modal_window).click()
        time.sleep(random.uniform(1.0, 2.0))