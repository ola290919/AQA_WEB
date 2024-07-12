"""
Класс для всплывающего окна ConfirmAlert
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertConfirmElement:
    def __init__(self, browser):
        self.browser = browser
        self.driver, self.base_url = self.browser
        self.alert = WebDriverWait(self.driver, 2).until(EC.alert_is_present())

    def accept_alert(self):
        self.alert.accept()

    def dismiss_alert(self):
        self.alert.dissmiss()
