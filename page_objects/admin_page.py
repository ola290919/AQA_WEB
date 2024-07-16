"""
Базовый класс для раздела администратора
"""
import  allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage
from helpers import random_string


class AdminPage(BasePage):
    INPUT_USERNAME = By.ID, 'input-username'
    INPUT_PASSWORD = By.ID, 'input-password'
    BUTTON_LOGIN = By.XPATH, '//*[@id="form-login"]/div/button[@type="submit"]'
    BUTTON_LOGOUT = By.XPATH, '//*[@id="nav-logout"]/a'
    ADMIN_PROFILE = By.XPATH, '//*[@id="nav-profile"]//*[@alt="John Doe"]'
    BUTTON_OPEN_CATALOG = By.XPATH, '//*[@id="menu-catalog"]/a[@href="#collapse-1"]'
    BUTTON_PRODUCTS_IN_CATALOG = By.XPATH, '//*[@id="collapse-1"]/li/a[contains(text(),"Products")]'
    BUTTON_ADD_PRODACT = By.XPATH, ('//*[@id="content"]//*[@class="float-end"]'
                                    '/a[@class="btn btn-primary"]')
    INPUT_PRODUCT_NAME = By.ID, 'input-name-1'
    INPUT_META_TAG_TITLE = By.ID, 'input-meta-title-1'
    BUTTON_SAVE_PRODUCT = By.XPATH, ('//*[@id="content"]//div[@class="float-end"]'
                                     '/button[@form="form-product"]')
    TAB_DATA_PRODUCT = By.XPATH, '//*[@id="form-product"]//a[@href="#tab-data"]'
    TAB_SEO_PRODUCT = By.XPATH, '//*[@id="form-product"]//a[@href="#tab-seo"]'
    INPUT_MODEL_PRODUCT = By.ID, 'input-model'
    INPUT_KEYWORD_PRODUCT = By.ID, 'input-keyword-0-1'
    CHECKBOX_PRODUCT = By.XPATH, ('//*[@class="table table-bordered table-hover"]'
                                  '//input[@type="checkbox"]')
    BUTTON_DELETE_PRODUCT = By.XPATH, ('//*[@id="content"]'
                                       '//*[@class="float-end"]/button[@class="btn btn-danger"]')


    @allure.step("Заполняется форма авторизации админа")
    def input_login_admin_form(self):
        self.logger.info("%s: Input USERNAME and PASSWORD" % (self.class_name))
        self.input_value(self.INPUT_USERNAME, 'user')
        self.input_value(self.INPUT_PASSWORD, 'bitnami')

    @allure.step("Нажимается кнопка LOGIN и проверяется профиль админа")
    def login_admin_account(self):
        self.logger.info("%s: Click BUTTON_LOGIN and check ADMIN_PROFILE" % (self.class_name))
        self.click_element(self.BUTTON_LOGIN)
        self.get_element(self.ADMIN_PROFILE)

    @allure.step("Нажимается кнопка LOGOUT")
    def logout_admin_account(self):
        self.logger.info("%s: Click BUTTON_LOGOUT" % (self.class_name))
        self.click_element(self.BUTTON_LOGOUT)

    @allure.step("Открывается список продуктов админа")
    def open_product_list(self):
        self.logger.info("%s: Open CATALOG in side bar and click BUTTON_PRODUCTS" % (self.class_name))
        self.click_element(self.BUTTON_OPEN_CATALOG)
        product_button = self.get_element(self.BUTTON_PRODUCTS_IN_CATALOG)
        self.driver.execute_script("arguments[0].click();", product_button)

    @allure.step("Нажимается кнопка + (добавить новый продукт)")
    def click_add_product_button(self):
        self.logger.info("%s: Click BUTTON_ADD_PRODACT" % (self.class_name))
        self.click_element(self.BUTTON_ADD_PRODACT)

    @allure.step("Заполняются обязательные поля для нового продукта")
    def input_new_product(self):
        self.logger.info("%s: Input PRODUCT_NAME, META_TAG_TITLE, "
                         "MODEL_PRODUCT and KEYWORD_PRODUCT" % (self.class_name))
        self.input_value(self.INPUT_PRODUCT_NAME, '1New Product')
        self.input_value(self.INPUT_META_TAG_TITLE, 'Meta Tag Title New Product')
        self.click_element(self.TAB_DATA_PRODUCT)
        self.input_value(self.INPUT_MODEL_PRODUCT, 'New Product Model')
        self.click_element(self.TAB_SEO_PRODUCT)
        self.input_value(self.INPUT_KEYWORD_PRODUCT, random_string())

    @allure.step("Нажимается кнопка SAVE")
    def click_save_product_button(self):
        self.logger.info("%s: Click BUTTON_SAVE_PRODUCT" % (self.class_name))
        self.click_element(self.BUTTON_SAVE_PRODUCT)

    @allure.step("Активируется чекбокс для {index}-го продукта и нажимается кнопка DELETE")
    def delete_product_in_list(self, index):
        self.logger.info("%s: Click %s CHECKBOX_PRODUCT "
                         "and click BUTTON_DELETE_PRODUCT " % (self.class_name, index))
        self.get_elements(self.CHECKBOX_PRODUCT)[index].click()
        self.click_element(self.BUTTON_DELETE_PRODUCT)
