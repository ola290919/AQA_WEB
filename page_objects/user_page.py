"""
Базовый класс для пользователя
"""
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

    def input_user_data(self):
        self.input_value(self.INPUT_FIRST_NAME, 'Freddy')
        self.input_value(self.INPUT_LAST_NAME, 'Mercury')
        self.input_value(self.INPUT_EMALE, random_email())
        self.input_value(self.INPUT_PASSWORD, random_string())

    def agree_to_the_privacy_policy(self):
        self.click_element(self.CHECKBOX_PRIVACY_POLICY)

    def click_continue_button(self):
        self.click_element(self.BUTTON_CONTINUE)
