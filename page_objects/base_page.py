"""
Базовый класс для всех страниц
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:
    """Базовый класс"""
    def __init__(self, browser):
        self.browser = browser
        self.driver, self.base_url = self.browser


    def link_with_base_url(self, end_link):
        """Получить ссылку с базовым url"""
        base_url = self.base_url
        link = f'{base_url}/{end_link}'
        return link

    def get_page(self, end_url):
        """Загрузить страницу"""
        self.driver.get(f'{self.base_url}/{end_url}')

    def find_visible_element_by_xpath(self, locator, timeout=1, by=By.XPATH):
        """
        Поиск по XPATH элемента, который видим в dom и на странице
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, locator)))
        except TimeoutException:
            self.driver.save_screenshot(f"screenshots/{self.driver.session_id}.png")
            raise AssertionError(f"Не дождались видимости элемента: {locator} за {timeout} секунд")

    def find_invisible_element_by_xpath(self, locator, timeout=1, by=By.XPATH):
        """Поиск по XPATH элемента, который видим в dom и не обязательно видим на странице"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            self.driver.save_screenshot(f"screenshots/{self.driver.session_id}.png")
            raise AssertionError(
                f"Не дождались видимости элемента в DOM: {locator} за {timeout} секунд")


    def get_element(self, locator: tuple, timeout=1):
        """Получить элемент, который видим в dom и видим на странице"""
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator))
        except TimeoutException:
            self.driver.save_screenshot(f"screenshots/{self.driver.session_id}.png")
            raise AssertionError(
                f"Не дождались видимости элемента: {locator[1]} за {timeout} секунд")

    def get_elements(self, locator: tuple, timeout=1):
        """Получить элемент, который видим в dom и видим на странице"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator))

    def check_page_title(self, title, timeout=1):
        """Проверка титула страницы"""
        try:
            WebDriverWait(self.driver, timeout).until(EC.title_is(title))
        except TimeoutException:
            self.driver.save_screenshot(f"screenshots/{self.driver.session_id}.png")
            raise AssertionError(f"Титул страницы не {title}")

    def click_element(self, locator: tuple):
        """Кликнуть элемент"""
        ActionChains(self.driver).move_to_element(self.get_element(locator)).click().perform()

    def input_value(self, locator: tuple, text: str):
        """Заполнить поле"""
        self.get_element(locator).click()
        self.get_element(locator).clear()
        for l in text:
            self.get_element(locator).send_keys(l)
