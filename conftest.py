import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import random

@pytest.fixture(scope="function")
def driver():
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    # ЕTurn off saving modal window
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    g = Service("C:\\webdriver\\chromedriver.exe")
    driver = uc.Chrome(options=options)
    driver.implicitly_wait(5)

    # 1. Open cite
    base_url = 'https://www.onlinetrade.ru/'
    driver.get(base_url)
    driver.maximize_window()
    time.sleep(2)

    # 2. Accept cookie
    try:
        cookie_btn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@title="Принять"]'))
        )
        cookie_btn.click()
        time.sleep(random.uniform(1, 2))
    except:
        pass

    # 3. Click "Login"
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='ic__set ic__set__member']"))
    ).click()

    time.sleep(1.5)

    # 4. Filling authorisation forms
    login = "testov@mail.ru"
    password = "1234567QA"

    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='ajax_login_popup_email']"))
    ).send_keys(login)

    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='ajax_login_popup_pass']"))
    ).send_keys(password)

    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@name='submit']"))
    ).click()
    time.sleep(2)
    yield driver
    driver.quit()