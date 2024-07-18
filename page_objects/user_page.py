"""
Базовый класс для пользователя
"""
import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from helpers import random_string, random_email


class UserPage(BasePage):
    INPUT_FIRST_NAME = By.ID, 'input-firstname'
    INPUT_LAST_NAME = By.ID, 'input-lastname'
    INPUT_EMALE = By.ID, 'input-email'
    INPUT_PASSWORD = By.ID, 'input-password'
    CHECKBOX_PRIVACY_POLICY = By.XPATH, '//div[@class="text-end"]//input[@type="checkbox"]'
    BUTTON_CONTINUE = By.XPATH, ('//div[@class="text-end"]'
                                 '//button[@type="submit" and contains(text(), "Continue")]')

    @allure.step("Заполняется форма регистрации")
    def input_user_data(self):
        self.logger.info("%s: Input FIRST_NAME, LAST_NAME, E-MALE, PASSWORD " % (self.class_name))
        self.input_value(self.INPUT_FIRST_NAME, 'Freddy')
        self.input_value(self.INPUT_LAST_NAME, 'Mercury')
        self.input_value(self.INPUT_EMALE, random_email())
        self.input_value(self.INPUT_PASSWORD, random_string())

    @allure.step("Активируется чекбокс согласия с Политикой конфиденциальности")
    def agree_to_the_privacy_policy(self):
        self.logger.info("%s: Click CHECKBOX_PRIVACY_POLICY" % (self.class_name))
        self.click_element(self.CHECKBOX_PRIVACY_POLICY)

    @allure.step("Нажимается кнопка CONTINUE")
    def click_continue_button(self):
        self.logger.info("%s: Click BUTTON_CONTINUE" % (self.class_name))
        self.click_element(self.BUTTON_CONTINUE)
