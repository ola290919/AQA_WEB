"""
Базовый класс для раздела валют
"""
import random
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class CarrencyPage(BasePage):
    CURRENCY_LIST_DOWN = By.XPATH, '//*[@class="list-inline"]//i[@class="fa-solid fa-caret-down"]'
    ALL_DOLLARS_ON_PAGE = By.XPATH, ('//*[contains(text(),"$") '
                                     'and not(@type="text/javascript") and not(@onclick)]')
    ALL_EURO_ON_PAGE = By.XPATH, '//*[contains(text(),"€")]'
    ALL_POUNDS_ON_PAGE = By.XPATH, '//*[contains(text(),"£")]'



    def click_currencies_list(self):
        self.click_element(self.CURRENCY_LIST_DOWN)

    def choose_random_carrency(self):
        currencies_list = ["€", "$", "£"]
        random_currency = random.choice(currencies_list)
        return random_currency

    def click_random_carrency(self, carrency):
        current_carrency = (By.XPATH,
                            f'//*[@class="list-inline"]'
                            f'//a[@class="dropdown-item" and contains(text(),"{carrency}")]')
        currency_choise = self.get_element(current_carrency)
        self.driver.execute_script("arguments[0].click();", currency_choise)
    def check_random_carrency(self, carrency):
        switched_carrency = f'//*[@class="list-inline"]//strong[contains(text(),"{carrency}")]'
        self.find_visible_element_by_xpath(switched_carrency)

    def check_currency_on_page(self, currency):
        if currency == "$":
            assert len(self.get_elements(self.ALL_POUNDS_ON_PAGE))  == 1, \
                '£ still displayed on page'
            assert len(self.get_elements(self.ALL_EURO_ON_PAGE)) == 1, \
                '€ still displayed on page'
        if currency == "€":
            assert len(self.get_elements(self.ALL_POUNDS_ON_PAGE)) == 1, \
                '£ still displayed on page'
            assert len(self.get_elements(self.ALL_DOLLARS_ON_PAGE)) == 1, \
                '$ still displayed on page'
        if currency == "£":
            assert len(self.get_elements(self.ALL_DOLLARS_ON_PAGE)) == 1, \
                '$ still displayed on page'
            assert len(self.get_elements(self.ALL_EURO_ON_PAGE)) == 1, \
                '€ still displayed on page'
