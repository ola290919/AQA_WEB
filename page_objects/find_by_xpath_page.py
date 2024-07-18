"""
Класс для тестов элементарного поиска элементов по XPATH
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from page_objects.base_page import BasePage

class FindPage(BasePage):
    @allure.step("Поиск видимого в dom и на странице элемента {locator} по XPATH")
    def find_visible_element_by_xpath(self, locator, timeout=1, by=By.XPATH):
        """
        Поиск по XPATH элемента, который видим в dom и на странице
        """
        try:
            self.logger.info("%s: Look for element %s" % (self.class_name, locator))
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((by, locator)))
        except TimeoutException as exc:
            self.logger.error("%s: Can not find element %s" % (self.class_name, locator))
            allure.attach(name="failure_screenshot", body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(
                f"Не дождались видимости элемента: {locator} за {timeout} секунд") from exc

    @allure.step("Поиск видимого в dom элемента {locator} по XPATH")
    def find_invisible_element_by_xpath(self, locator, timeout=1, by=By.XPATH):
        """Поиск по XPATH элемента, который видим в dom и не обязательно видим на странице"""
        try:
            self.logger.info("%s: Look for element %s" % (self.class_name, locator))
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, locator)))
        except TimeoutException as exc:
            self.logger.error("%s: Can not find element %s" % (self.class_name, locator))
            allure.attach(name="failure_screenshot", body=self.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError(
                f"Не дождались видимости элемента в DOM: {locator} за {timeout} секунд") from exc