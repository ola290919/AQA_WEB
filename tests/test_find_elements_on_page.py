"""
Тесты проверки элементарного наличия элементов
"""
from page_objects.base_page import BasePage


def test_find_elements_on_homepage(browser):
    """
    Тест проверки элементарного наличия элементов на Главной странице
    """
    base = BasePage(browser)
    base.get_page('')
    base.find_visible_element_by_xpath('//*[@id ="search"]/button')
    base.find_visible_element_by_xpath('//*[@id ="search"]')
    base.find_visible_element_by_xpath('//*[@id="header-cart"]/div/button')
    base.find_visible_element_by_xpath(
        f'//*[@id="narbar-menu"]//*[@href="{base.link_with_base_url('en-gb/catalog/cameras')}"]')
    base.find_visible_element_by_xpath(
        f'/html/body/footer//*[@href="{base.link_with_base_url(
            'en-gb?route=account/newsletter')}"]')


def test_find_elements_on_administration_page(browser):
    """
    Тест проверки элементарного наличия элементов на странице логина в админку /administration
    """
    base = BasePage(browser)
    base.get_page('administration')
    base.find_visible_element_by_xpath('//*[@id="form-login"]/div/button')
    base.find_visible_element_by_xpath('//*[@id="input-username"]')
    base.find_visible_element_by_xpath('//*[@id="input-password"]')
    base.find_visible_element_by_xpath('//*[@id="footer"]//*[@href="https://www.opencart.com"]')
    base.find_visible_element_by_xpath(
        f'//*[@id="header"]//*[@href="{base.link_with_base_url(
            'administration/index.php?route=common/login')}"]')


def test_find_elements_on_registration_page(browser):
    """
    Тест проверки элементарного наличия элементов на
    странице регистрации пользователя (/index.php?route=account/register)
    """
    base = BasePage(browser)
    base.get_page('index.php?route=account/register')
    base.find_visible_element_by_xpath(
        f'//*[@id="column-right"]//*[@href="{base.link_with_base_url(
            'en-gb?route=account/address')}"]')
    base.find_visible_element_by_xpath('//*[@id="form-register"]/div/button')
    base.find_visible_element_by_xpath('//*[@id="input-firstname"]')
    base.find_visible_element_by_xpath('//*[@id="input-password"]')
    base.find_visible_element_by_xpath(
        f'//*[@id="content"]//*[@href="{base.link_with_base_url('en-gb?route=account/login')}"]')


def test_find_elements_on_prodact_page_iphone(browser):
    """
    Тест проверки элементарного наличия элементов на
    странице карточки товара (/en-gb/product/iphone)
    """
    base = BasePage(browser)
    base.get_page('en-gb/product/iphone')
    base.find_visible_element_by_xpath('//*[@id="tab-description"]/p')
    base.find_visible_element_by_xpath('//*[@id="form-product"]/div/button')
    base.find_visible_element_by_xpath('//*[@id="input-quantity"]')
    base.find_visible_element_by_xpath(
        f'//*[@id="content"]//*[@formaction="{base.link_with_base_url(
            'en-gb?route=product/compare.add')}"]')
    base.find_visible_element_by_xpath(
        f'//*[@id="content"]//*[@href="{base.link_with_base_url(
            'image/cache/catalog/demo/iphone_1-800x800.jpg')}"]')


def test_find_elements_on_catalog_page(browser):
    """
    Тест проверки элементарного наличия элементов на
    странице каталога (/en-gb/catalog/smartphone)
    """
    base = BasePage(browser)
    base.get_page('en-gb/catalog/smartphone')
    base.find_visible_element_by_xpath('//*[@id="input-limit"]')
    base.find_visible_element_by_xpath('//*[@id="button-grid"]')
    base.find_visible_element_by_xpath('//*[@id="carousel-banner-0"]')
    base.find_visible_element_by_xpath(
        f'//*[@id="column-left"]//*[@href="{base.link_with_base_url('en-gb/catalog/software')}"]')
    base.find_visible_element_by_xpath('//*[@id="compare-total"]')


def test_find_elements_on_product_page_htc(browser):
    """
    Тест проверки элементарного наличия элементов на
    странице карточки товара (/en-gb/product/smartphone/htc-touch-hd)
    """
    base = BasePage(browser)
    base.get_page('en-gb/product/smartphone/htc-touch-hd')
    base.find_visible_element_by_xpath('//*[@id="content"]//*[@href="#tab-review"]')
    base.find_invisible_element_by_xpath(
        '//input[@type="hidden" and @name="product_id" and @value="28"]')
    base.find_visible_element_by_xpath(
        '//li[contains(text(),"Special Features: FM Radio, G-Sensor")]')
    base.find_visible_element_by_xpath(
        f'//*[@class="list-unstyled"]'
        f'//*[@href="{base.link_with_base_url('en-gb?route=information/contact')}"]')
    base.find_visible_element_by_xpath(
        f'//div[@class="btn-group"]'
        f'/button[@formaction="{base.link_with_base_url('en-gb?route=product/compare.add')}"]')
