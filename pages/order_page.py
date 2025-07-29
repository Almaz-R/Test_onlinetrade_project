from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
import random

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
    # Locators
    order_button = (By.XPATH, "//input[@name='submit']")
    address_field = (By.XPATH, "//textarea[@id='address']")
    order_submit_button = (By.XPATH, "//input[@id='order_step2_submit']")

    def go_to_order(self):
    # Transferring to the ordering page
        actions = ActionChains(self.driver)
        element_1 = self.driver.find_element(*self.order_button)
        actions.move_to_element(element_1).click().perform()
        time.sleep(random.uniform(1.5, 2.0))

    def filling_address(self):
        # Filling address
        self.driver.find_element(*self.address_field).send_keys("Test_street")

    def order_submit(self):
        # Submitting
        self.driver.find_element(*self.order_submit_button).click()