"""
Тесты проверки элементарного наличия элементов
"""
import allure
from page_objects.base_page import BasePage
from page_objects.find_by_xpath_page import FindPage


@allure.feature('Find element')
def test_find_elements_on_homepage(browser):
    """
    Тест проверки элементарного наличия элементов на Главной странице
    """
    find = FindPage(browser)
    base = BasePage(browser)
    find.get_page('')
    find.find_visible_element_by_xpath('//*[@id ="search"]/button')
    find.find_visible_element_by_xpath('//*[@id ="search"]')
    find.find_visible_element_by_xpath('//*[@id="header-cart"]/div/button')
    find.find_visible_element_by_xpath(
        f'//*[@id="narbar-menu"]'
        f'//*[@href="{base.link_with_base_url('en-gb/catalog/cameras')}"]')
    find.find_visible_element_by_xpath(
        f'/html/body/footer//*[@href="{BasePage(browser).link_with_base_url(
            'en-gb?route=account/newsletter')}"]')


@allure.feature('Find element')
def test_find_elements_on_administration_page(browser):
    """
    Тест проверки элементарного наличия элементов на странице логина в админку /administration
    """
    find = FindPage(browser)
    base = BasePage(browser)
    find.get_page('administration')
    find.find_visible_element_by_xpath('//*[@id="form-login"]/div/button')
    find.find_visible_element_by_xpath('//*[@id="input-username"]')
    find.find_visible_element_by_xpath('//*[@id="input-password"]')
    find.find_visible_element_by_xpath('//*[@id="footer"]//*[@href="https://www.opencart.com"]')
    find.find_visible_element_by_xpath(
        f'//*[@id="header"]//*[@href="{base.link_with_base_url(
            'administration/index.php?route=common/login')}"]')


@allure.feature('Find element')
def test_find_elements_on_registration_page(browser):
    """
    Тест проверки элементарного наличия элементов на
    странице регистрации пользователя (/index.php?route=account/register)
    """
    find = FindPage(browser)
    base = BasePage(browser)
    find.get_page('index.php?route=account/register')
    find.find_visible_element_by_xpath(
        f'//*[@id="column-right"]//*[@href="{base.link_with_base_url(
            'en-gb?route=account/address')}"]')
    find.find_visible_element_by_xpath('//*[@id="form-register"]/div/button')
    find.find_visible_element_by_xpath('//*[@id="input-firstname"]')
    find.find_visible_element_by_xpath('//*[@id="input-password"]')
    find.find_visible_element_by_xpath(
        f'//*[@id="content"]//*[@href="{find.link_with_base_url('en-gb?route=account/login')}"]')


@allure.feature('Find element')
def test_find_elements_on_prodact_page_iphone(browser):
    """
    Тест проверки элементарного наличия элементов на
    странице карточки товара (/en-gb/product/iphone)
    """
    find = FindPage(browser)
    base = BasePage(browser)
    find.get_page('en-gb/product/iphone')
    find.find_visible_element_by_xpath('//*[@id="tab-description"]/p')
    find.find_visible_element_by_xpath('//*[@id="form-product"]/div/button')
    find.find_visible_element_by_xpath('//*[@id="input-quantity"]')
    find.find_visible_element_by_xpath(
        f'//*[@id="content"]//*[@formaction="{base.link_with_base_url(
            'en-gb?route=product/compare.add')}"]')
    find.find_visible_element_by_xpath(
        f'//*[@id="content"]//*[@href="{base.link_with_base_url(
            'image/cache/catalog/demo/iphone_1-800x800.jpg')}"]')


@allure.feature('Find element')
def test_find_elements_on_catalog_page(browser):
    """
    Тест проверки элементарного наличия элементов на
    странице каталога (/en-gb/catalog/smartphone)
    """
    find = FindPage(browser)
    base = BasePage(browser)
    find.get_page('en-gb/catalog/smartphone')
    find.find_visible_element_by_xpath('//*[@id="input-limit"]')
    find.find_visible_element_by_xpath('//*[@id="button-grid"]')
    find.find_visible_element_by_xpath('//*[@id="carousel-banner-0"]')
    find.find_visible_element_by_xpath(
        f'//*[@id="column-left"]'
        f'//*[@href="{base.link_with_base_url('en-gb/catalog/software')}"]')
    find.find_visible_element_by_xpath('//*[@id="compare-total"]')


@allure.feature('Find element')
def test_find_elements_on_product_page_htc(browser):
    """
    Тест проверки элементарного наличия элементов на
    странице карточки товара (/en-gb/product/smartphone/htc-touch-hd)
    """
    find = FindPage(browser)
    base = BasePage(browser)
    find.get_page('en-gb/product/smartphone/htc-touch-hd')
    find.find_visible_element_by_xpath('//*[@id="content"]//*[@href="#tab-review"]')
    find.find_invisible_element_by_xpath(
        '//input[@type="hidden" and @name="product_id" and @value="28"]')
    find.find_visible_element_by_xpath(
        '//li[contains(text(),"Special Features: FM Radio, G-Sensor")]')
    find.find_visible_element_by_xpath(
        f'//*[@class="list-unstyled"]'
        f'//*[@href="{base.link_with_base_url('en-gb?route=information/contact')}"]')
    find.find_visible_element_by_xpath(
        f'//div[@class="btn-group"]'
        f'/button[@formaction="{base.link_with_base_url('en-gb?route=product/compare.add')}"]')
