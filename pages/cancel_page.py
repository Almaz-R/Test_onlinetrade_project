from selenium.webdriver.common.by import By
import time
import random

class CancelPage:
    def __init__(self, driver):
        self.driver = driver
    # Locators
    extra_info = (By.XPATH, "//a[@title='Подробнее']")
    cancel_order = (By.XPATH, "//a[@title='Отменить заказ']")
    conformation = (By.XPATH, "//a[@title='Отменить выполнение заказа']")


    def cancel_order_action(self):
        self.driver.find_element(*self.extra_info).click()
        time.sleep(2)
        # Cancelling
        self.driver.find_element(*self.cancel_order).click()
        time.sleep(2)
        # Conformation of cancelling
        self.driver.find_element(*self.conformation).click()
        time.sleep(random.uniform(1.0, 3.0))
