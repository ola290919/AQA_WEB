"""
Базовый класс для продукта
"""
import random
import allure
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ProductPage(BasePage):
    @allure.step("Выбирается случайный продукт на главной странице")
    def choose_random_product_on_homepage(self):
        self.logger.info("%s: Get random product" % (self.class_name))
        products_link = self.link_with_base_url('en-gb?route=checkout/cart.add')
        all_products = (By.XPATH,
                        (f'//*[@class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-xl-4"]'
                         f'//button[@formaction="{products_link}"]'))
        products = self.get_elements(all_products)
        product = random.choice(products)
        return product

    @allure.step("Нажимается кнопка Add to cart для случайного продукта")
    def click_add_to_cart_random_product(self):
        self.logger.info("%s: Click ADD_TO_CART for random product" % (self.class_name))
        self.driver.execute_script("arguments[0].click();",
                                   self.choose_random_product_on_homepage())
