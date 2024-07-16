"""
Класс для всплывающего окна Alert
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class AlertSuccessElement:
    SUCCESS_ALERT = By.XPATH, ('//*[@id="alert"]'
                               '//*[@class="alert alert-success alert-dismissible"]')
    MODIFIED_PRODUCT_TEXT = By.XPATH, ('//*[contains(text(), '
                                       '" Success: You have modified products!")]')
    ADD_PRODUCT_TEXT = By.XPATH, '//*[contains(text(), " Success: You have added")]'

    def __init__(self, browser):
        self.browser = browser
        self.driver, self.base_url = self.browser
        self.logger = self.driver.logger

    @allure.step("Отображается всплывающее окно")
    def find_alert(self):
        try:
            self.logger.info("AlertSuccessElement: Look for alert")
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(self.SUCCESS_ALERT))
        except TimeoutException as exc:
            self.logger.error("AlertConfirmElement: Can not find element %s" % (self.SUCCESS_ALERT[1]))
            allure.attach(name="failure_screenshot", body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(
                f"Не дождались видимости элемента: {self.SUCCESS_ALERT}") from exc


    @allure.step("Текст всплывающего окна You have modified products!")
    def modified_product(self):
        try:
            self.logger.info("AlertSuccessElement: Text alert: You have modified products!")
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(self.MODIFIED_PRODUCT_TEXT))
        except TimeoutException as exc:
            self.logger.error("AlertSuccessElement: Can not find element %s" %
                              (self.MODIFIED_PRODUCT_TEXT[1]))
            allure.attach(name="failure_screenshot", body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(
                f"Не дождались видимости элемента: {self.MODIFIED_PRODUCT_TEXT}") from exc

    @allure.step("Текст всплывающего окна You have added ...")
    def add_product(self):
        try:
            self.logger.info("AlertSuccessElement: Text alert: You have added ...")
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(self.ADD_PRODUCT_TEXT))
        except TimeoutException as exc:
            self.logger.error("AlertSuccessElement: Can not find element %s" %
                              (self.ADD_PRODUCT_TEXT[1]))
            allure.attach(name="failure_screenshot", body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(
                f"Не дождались видимости элемента: {self.ADD_PRODUCT_TEXT}") from exc
