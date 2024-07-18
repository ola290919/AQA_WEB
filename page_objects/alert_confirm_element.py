"""
Класс для всплывающего окна ConfirmAlert
"""
import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertConfirmElement:
    def __init__(self, browser):
        self.browser = browser
        self.driver, self.base_url = self.browser
        self.logger = self.driver.logger
        with allure.step("Отображается окно Are you sure?"):
            self.logger.info("AlertConfirmElement: Open alert: Are you sure?")
            self.alert = WebDriverWait(self.driver, 2).until(EC.alert_is_present())

    @allure.step("Нажимается ОК в окне Are you sure?")
    def accept_alert(self):
        self.logger.info("AlertConfirmElement: Click OK")
        self.alert.accept()

    @allure.step("Нажимается ОТМЕНА в окне Are you sure?")
    def dismiss_alert(self):
        self.logger.info("AlertConfirmElement: Click NO")
        self.alert.dissmiss()
