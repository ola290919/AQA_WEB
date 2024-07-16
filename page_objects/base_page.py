"""
Базовый класс для всех страниц
"""
import allure
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
        self.logger = self.driver.logger
        self.class_name = type(self).__name__

    def link_with_base_url(self, end_link):
        """Получить ссылку с базовым url"""
        base_url = self.base_url
        link = f'{base_url}/{end_link}'
        return link

    @allure.step("Загружается страница {end_url}")
    def get_page(self, end_url):
        """Загрузить страницу"""
        try:
            self.logger.info("%s: Open page %s/%s" % (self.class_name, self.base_url, end_url))
            self.driver.get(f'{self.base_url}/{end_url}')
        except:
            self.logger.error("%s: Can not open page %s/%s" % (self.class_name, self.base_url, end_url))
            allure.attach(name="failure_screenshot", body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(
                f"Не удалось загрузить страницу: {self.base_url}/{end_url}")

    def get_element(self, locator: tuple, timeout=1):
        """Получить элемент, который видим в dom и видим на странице"""
        try:
            self.logger.debug("%s: Look for element %s" % (self.class_name, locator[1]))
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator))
        except TimeoutException as exc:
            self.logger.error("%s: Can not find element %s" % (self.class_name, locator[1]))
            allure.attach(name="failure_screenshot", body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(
                f"Не дождались видимости элемента: {locator[1]} за {timeout} секунд") from exc

    def get_elements(self, locator: tuple, timeout=1):
        """Получить элементы, которые видимы в dom и на странице"""
        try:
            self.logger.debug("%s: Look for elements %s" % (self.class_name, locator[1]))
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located(locator))
        except TimeoutException as exc:
            self.logger.error("%s: Can not find elements %s" % (self.class_name, locator[1]))
            allure.attach(name="failure_screenshot", body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"Не дождались видимости элементов: {locator[1]} за {timeout} секунд") from exc

    @allure.step("Проверяется титул страницы {title}")
    def check_page_title(self, title, timeout=1):
        """Проверка титула страницы"""
        try:
            self.logger.debug("%s: Check title %s" % (self.class_name, title))
            WebDriverWait(self.driver, timeout).until(EC.title_is(title))
        except TimeoutException as exc:
            self.logger.error("%s: Title is not %s" % (self.class_name, title))
            allure.attach(name="failure_screenshot", body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f"Титул страницы не {title}") from exc

    def click_element(self, locator: tuple):
        """Кликнуть элемент"""
        try:
            self.logger.debug("%s: Click to %s" % (self.class_name, locator[1]))
            ActionChains(self.driver).move_to_element(self.get_element(locator)).click().perform()
        except Exception as exc:
            self.logger.error("%s: Can not click to %s" % (self.class_name, locator[1]))
            allure.attach(name="failure_screenshot", body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(f'Не получилось кликнуть элемент {locator[1]}') from exc

    def input_value(self, locator: tuple, text: str):
        """Заполнить поле"""
        self.logger.debug("%s: Input %s in %s" % (self.class_name, text, locator[1]))
        self.get_element(locator).click()
        self.get_element(locator).clear()
        for l in text:
            self.get_element(locator).send_keys(l)
