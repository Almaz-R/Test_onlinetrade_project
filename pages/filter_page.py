from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import random
class FilterPage:
    def __init__(self, driver):
        self.driver = driver
    # Locators
    catalog = (By.XPATH, "//div[@class='header__menuLink__icon']")
    product_category = (By.XPATH, "//a[@title='Перейти в категорию «Смартфоны»']")
    product = (By.XPATH, "//a[contains(text(),'Samsung Galaxy A16 4/128GB Черный')]")

    def apply_filter(self):
        self.driver.find_element(*self.catalog).click()
        time.sleep(random.uniform(0.5, 2.0))
    def select_category(self):
        self.driver.find_element(*self.product_category).click()
        time.sleep(random.uniform(1.0, 2.0))
    def select_product(self):
        actions = ActionChains(self.driver)
        element = self.driver.find_element(*self.product)
        actions.move_to_element(element).click().perform()
        time.sleep(random.uniform(1.0, 2.0))