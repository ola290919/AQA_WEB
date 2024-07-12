"""
Класс для всплывающего окна Alert
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertSuccessElement:
    SUCCESS_ALERT = By.XPATH, ('//*[@id="alert"]'
                               '//*[@class="alert alert-success alert-dismissible"]')
    MODIFIED_PRODUCT_TEXT = By.XPATH, ('//*[contains(text(), '
                                       '" Success: You have modified products!")]')
    ADD_PRODUCT_TEXT = By.XPATH, '//*[contains(text(), " Success: You have added")]'

    def __init__(self, browser):
        self.browser = browser
        self.driver, self.base_url = self.browser

    def modified_product(self):
        """Изменение продуктового листа"""
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.SUCCESS_ALERT))
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.MODIFIED_PRODUCT_TEXT))

    def add_product(self):
        """Добавление продукта в корзину или вишлист"""
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.SUCCESS_ALERT))
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(self.ADD_PRODUCT_TEXT))
