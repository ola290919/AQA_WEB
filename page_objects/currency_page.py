"""
Базовый класс для раздела валют
"""
import random
import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CarrencyPage(BasePage):
    CURRENCY_LIST_DOWN = By.XPATH, '//*[@class="list-inline"]//i[@class="fa-solid fa-caret-down"]'
    ALL_DOLLARS_ON_PAGE = By.XPATH, ('//*[contains(text(),"$") '
                                     'and not(@type="text/javascript") and not(@onclick)]')
    ALL_EURO_ON_PAGE = By.XPATH, '//*[contains(text(),"€")]'
    ALL_POUNDS_ON_PAGE = By.XPATH, '//*[contains(text(),"£")]'

    @allure.step("Открывается список список валют в верхнем меню")
    def click_currencies_list(self):
        self.logger.info("%s: Click currencies list" % (self.class_name))
        self.click_element(self.CURRENCY_LIST_DOWN)

    @allure.step("Выбирается случайная валюта")
    def choose_random_carrency(self):
        currencies_list = ["€", "$", "£"]
        random_currency = random.choice(currencies_list)
        self.logger.info("%s: Random carrency is %s" % (self.class_name, random_currency))
        return random_currency

    @allure.step("Нажимается кнопка случайной валюты {carrency} в верхнем меню")
    def click_random_carrency(self, carrency):
        self.logger.info("%s: CLick %s in currencies list" % (self.class_name, carrency))
        current_carrency = (By.XPATH,
                            f'//*[@class="list-inline"]'
                            f'//a[@class="dropdown-item" and contains(text(),"{carrency}")]')
        currency_choise = self.get_element(current_carrency)
        self.driver.execute_script("arguments[0].click();", currency_choise)

    @allure.step("Проверяется, что валюта в верхнем меню переключилась на {carrency}")
    def check_random_carrency(self, carrency):
        self.logger.info("%s: Check random currency %s" % (self.class_name, carrency))
        switched_carrency = (By.XPATH,
                             f'//*[@class="list-inline"]//strong[contains(text(),"{carrency}")]')
        self.get_element(switched_carrency)

    @allure.step("Проверяется, что валюта на странице переключилась")
    def check_currency_on_page(self, currency):
        self.logger.info("%s: Check random currency in prices on page" % (self.class_name))
        if currency == "$":
            assert len(self.get_elements(self.ALL_POUNDS_ON_PAGE)) == 1, '£ still displayed on page'
            assert len(self.get_elements(self.ALL_EURO_ON_PAGE)) == 1, '€ still displayed on page'
        if currency == "€":
            assert len(self.get_elements(self.ALL_POUNDS_ON_PAGE)) == 1, '£ still displayed on page'
            assert len(self.get_elements(self.ALL_DOLLARS_ON_PAGE)) == 1, \
                '$ still displayed on page'
        if currency == "£":
            assert len(self.get_elements(self.ALL_DOLLARS_ON_PAGE)) == 1, \
                '$ still displayed on page'
            assert len(self.get_elements(self.ALL_EURO_ON_PAGE)) == 1, '€ still displayed on page'
