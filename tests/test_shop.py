from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.cancel_page import CancelPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.filter_page import FilterPage
from pages.order_page import OrderPage


class TestShop:

    def test_authorization(self, driver):

        profile_icon = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='huab__cell__text orange']")))

        actions = ActionChains(driver)
        actions.move_to_element(profile_icon).perform()

        # Waiting text "Мой профиль"
        try:
            profile_text = WebDriverWait(driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, "//a[@title='Мои профиль']"))
            )
            assert profile_text.is_displayed()
            print("Authorisation is successful")
        except:
            print("Authorisation isn't successful")
            assert False

    def test_product_filter_and_select(self, driver):
        filter = FilterPage(driver)
        filter.apply_filter()

        try:
            text = driver.find_element(By.XPATH, "//a[@title='Перейти в категорию «Телефоны и гаджеты»']").text
            assert text == "Телефоны и гаджеты"
            print("Filter opened")
        except NoSuchElementException:
            print("Filter isn't opened")

        filter.select_category()

        try:
            text = driver.find_element(By.XPATH, "//h1[contains(text(),'Смартфоны')]").text
            assert text == "Смартфоны"
            print("Category is selected")
        except NoSuchElementException:
            print("Category isn't selected")

        filter.select_product()

        try:
            text = driver.find_element(By.XPATH, "//h1[@itemprop='name']").text
            assert text == "Смартфон Samsung Galaxy A16 4/128GB Черный"
            print("Product is selected")
        except NoSuchElementException:
            print("Product isn't selected")

    def test_check_product_page(self, driver):
        driver.get("https://www.onlinetrade.ru/catalogue/smartfony-c13/samsung"
                   "/smartfon_samsung_galaxy_a16_4_128gb_chernyy_sm_a165fzkdcau-4588811.html")
        product = ProductPage(driver)
        product.add_to_cart()

        try:
            text = driver.find_element(By.XPATH, "//h3[contains(text(),'Товар добавлен в корзину')]").text
            assert text == "Товар добавлен в корзину «Основная»"
            print("Product is added to the cart")
        except NoSuchElementException:
            print("Product isn't added to the cart")

        product.close_window()

        try:
            text = driver.find_element(By.XPATH, "//h1[@itemprop='name']").text
            assert text == "Смартфон Samsung Galaxy A16 4/128GB Черный"
            print("Modal window is closed")
        except NoSuchElementException:
            print("Modal window isn't closed")


    def test_check_cart(self, driver):
        cart = CartPage(driver)
        cart.go_to_cart()

        try:
            text = driver.find_element(By.XPATH, "//h1[contains(text(),'Корзина')]").text
            assert text == "Корзина"
            print("Cart opened")
        except NoSuchElementException:
            print("Cart isn't opened")

        try:
            text = driver.find_element(By.XPATH, "//a[@title='Смартфон Samsung Galaxy A16 4/128GB Черный']").text
            assert text == "Смартфон Samsung Galaxy A16 4/128GB Черный"
            print("Product into the cart")
        except NoSuchElementException:
            print("There is no product")

    def test_order_product(self, driver):
        driver.get("https://www.onlinetrade.ru/basket.html?basket_hash=143e9d4293a9486471d36ea32058455e")
        order = OrderPage(driver)
        order.go_to_order()

        try:
            text = driver.find_element(By.XPATH, "//h1[contains(text(),'Оформление заказа')]").text
            assert text == "Оформление заказа"
            print("The ordering page is right")
        except NoSuchElementException:
            print("The ordering page isn't right")

        order.filling_address()

        order.order_submit()

        try:
            text = driver.find_element(By.XPATH, "//h1[contains(text(),'Заказ оформлен!')]").text
            assert text == "Заказ оформлен!"
            print("The ordering page is right")
        except NoSuchElementException:
            print("The ordering page isn't right")

    def test_cancel_order(self, driver):
        driver.get("https://www.onlinetrade.ru/member/orders.html")
        cancel = CancelPage(driver)
        cancel.cancel_order()

        try:
            text = driver.find_element(By.XPATH, "// p[contains(text(), 'Ваш заказ отменяется')]").text
            assert text == "Ваш заказ отменяется"
            print("The order is canceled")
        except NoSuchElementException:
            print("The order isn't canceled")