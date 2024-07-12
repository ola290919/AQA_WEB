"""
Базовый класс для продукта
"""
import random
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ProductPage(BasePage):
    def choose_random_product_on_homepage(self):
        products_link = self.link_with_base_url('en-gb?route=checkout/cart.add')
        all_products = (By.XPATH,
                        (f'//*[@class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-xl-4"]'
                         f'//button[@formaction="{products_link}"]'))
        products = self.get_elements(all_products)
        product = random.choice(products)
        return product

    def click_add_to_cart_random_product(self):
        self.driver.execute_script("arguments[0].click();",
                                   self.choose_random_product_on_homepage())
