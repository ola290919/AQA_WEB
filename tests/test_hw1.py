"""
Тесты проверки наличия элементов и покрытия  сценариев opencart
"""

import random

import pytest

from selenium.webdriver.common.by import By

from helpers import find_visible_element, check_page_title


def test_find_elements_on_homepage(browser):
    """
    Тесты проверки элементарного наличия элементов на Главной странице
    """
    driver = browser[0]
    base_url = browser[1]
    driver.get(base_url)
    find_visible_element('//*[@id ="search"]/button', driver)
    find_visible_element('//*[@id ="search"]', driver)
    find_visible_element('//*[@id="header-cart"]/div/button', driver)
    find_visible_element(f'//*[@id="narbar-menu"]//*[@href="{base_url}/en-gb/catalog/cameras"]',
                         driver)
    find_visible_element(f'/html/body/footer//*[@href="{base_url}/en-gb?route=account/newsletter"]',
                         driver)


def test_find_elements_on_administration_page(browser):
    """
    Тесты проверки элементарного наличия элементов на странице логина в админку /administration
    """
    driver = browser[0]
    base_url = browser[1]
    driver.get(f'{base_url}/administration/')
    find_visible_element('//*[@id="form-login"]/div/button', driver)
    find_visible_element('//*[@id="input-username"]', driver)
    find_visible_element('//*[@id="input-password"]', driver)
    find_visible_element('//*[@id="footer"]//*[@href="https://www.opencart.com"]', driver)
    find_visible_element(f'//*[@id="header"]//*[@href="{base_url}/'
                         f'administration/index.php?route=common/login"]', driver)


def test_find_elements_on_registration_page(browser):
    """
    Тесты проверки элементарного наличия элементов на
    странице регистрации пользователя (/index.php?route=account/register)
    """
    driver = browser[0]
    base_url = browser[1]
    driver.get(f'{base_url}/index.php?route=account/register')
    find_visible_element(
        f'//*[@id="column-right"]//*[@href="{base_url}/en-gb?route=account/address"]', driver)
    find_visible_element('//*[@id="form-register"]/div/button', driver)
    find_visible_element('//*[@id="input-firstname"]', driver)
    find_visible_element('//*[@id="input-firstname"]', driver)
    find_visible_element(f'//*[@id="content"]//*[@href="{base_url}/en-gb?route=account/login"]',
                         driver)


def test_find_elements_on_prodact_page(browser):
    """
    Тесты проверки элементарного наличия элементов на
    странице карточки товара (/en-gb/product/iphone)
    """
    driver = browser[0]
    base_url = browser[1]
    driver.get(f'{base_url}/en-gb/product/iphone')
    find_visible_element('//*[@id="tab-description"]/p', driver)
    find_visible_element('//*[@id="form-product"]/div/button', driver)
    find_visible_element(f'//*[@id="content"]'
                         f'//*[@formaction="{base_url}/en-gb?route=product/compare.add"]', driver)
    find_visible_element('//*[@id="input-quantity"]', driver)
    find_visible_element(f'//*[@id="content"]'
                         f'//*[@href="{base_url}/image/cache/catalog/demo/iphone_1-800x800.jpg"]',
                         driver)


def test_find_elements_on_catalog_page(browser):
    """
    Тесты проверки элементарного наличия элементов на
    странице каталога (/en-gb/catalog/smartphone)
    """
    driver = browser[0]
    base_url = browser[1]
    driver.get(f'{base_url}/en-gb/catalog/smartphone')
    find_visible_element('//*[@id="input-limit"]', driver)
    find_visible_element(f'//*[@id="column-left"]'
                         f'//*[@href="{base_url}/en-gb/catalog/software"]', driver)
    find_visible_element('//*[@id="button-grid"]', driver)
    find_visible_element('//*[@id="carousel-banner-0"]', driver)
    find_visible_element('//*[@id="compare-total"]', driver)


def test_find_elements_on_product_page(browser):
    """
    Тесты проверки элементарного наличия элементов на
    странице карточки товара (/en-gb/product/smartphone/htc-touch-hd)
    """
    driver = browser[0]
    base_url = browser[1]
    driver.get(f'{base_url}/en-gb/product/smartphone/htc-touch-hd')
    find_visible_element('//*[@id="content"]//*[@href="#tab-review"]', driver)
    find_visible_element(f'//*[@class="list-unstyled"]'
                         f'//*[@href="{base_url}/en-gb?route=information/contact"]', driver)
    driver.find_element(By.XPATH, '//input[@type="hidden" and @name="product_id" and @value="28"]')
    find_visible_element(f'//div[@class="btn-group"]/'
                         f'button[@formaction="{base_url}/en-gb?route=product/compare.add"]',
                         driver)
    find_visible_element('//li[contains(text(),"Special Features: FM Radio, G-Sensor")]', driver)


def test_login_logout_admin(browser):
    """
    Тест покрытия сценария логина-разлогина в админку с проверкой, что логин был выполнен
    """
    driver = browser[0]
    base_url = browser[1]
    driver.get(f'{base_url}/administration')
    driver.find_element(By.ID, 'input-username').send_keys('user')
    driver.find_element(By.ID, 'input-password').send_keys('bitnami')
    driver.find_element(By.XPATH, '//*[@id="form-login"]/div/button').click()
    check_page_title('Dashboard', driver)
    find_visible_element('//*[@id="nav-profile"]//*[@alt="John Doe"]', driver)
    driver.find_element(By.XPATH, '//*[@id="nav-logout"]/a').click()
    check_page_title('Administration', driver)


def test_random_product(browser):
    """
    Тест покрытия сценария добавления в корзину случайного товара с главной страницы
    и проверки, что он появился в корзине
    """
    driver = browser[0]
    base_url = browser[1]
    driver.get(base_url)
    products = driver.find_elements(
        By.XPATH,
        f'//*[@class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-xl-4"]'
        f'//button[@formaction="{base_url}/en-gb?route=checkout/cart.add"]')
    product = random.choice(products)
    driver.execute_script("arguments[0].click();", product)
    find_visible_element('//div[@class="alert alert-success alert-dismissible"]', driver)


@pytest.mark.parametrize('url_end', ['', '/en-gb/catalog/mp3-players', '/en-gb/catalog/cameras',
                                     '/en-gb/catalog/smartphone', '/en-gb/catalog/software',
                                     '/en-gb/catalog/tablet', '/en-gb/catalog/component',
                                     '/en-gb/catalog/laptop-notebook', '/en-gb/catalog/desktops'])
def test_switching_currencies(browser, url_end):
    """
    Тест покрытия сценария, что переключении валют цены на товары меняются на главной и в каталоге
    """
    driver = browser[0]
    base_url = browser[1]
    driver.get(f'{base_url}{url_end}')
    driver.find_element(By.XPATH, '//*[@class="list-inline"]'
                                  '//i[@class="fa-solid fa-caret-down"]').click()
    currencies_list = ["€", "$", "£"]
    for curriency in currencies_list:
        curriency_choise = driver.find_element(By.XPATH,
                                               f'//*[@class="list-inline"]//'
                                               f'a[@class="dropdown-item" and contains(text(),'
                                               f'"{curriency}")]')
        driver.execute_script("arguments[0].click();", curriency_choise)
        find_visible_element(f'//*[@class="list-inline"]//strong[contains(text(),"{curriency}")]',
                             driver)
        if curriency == "$":
            assert len(driver.find_elements(By.XPATH, '//*[contains(text(),"£")]')) == 1, \
                '£ still displayed on page'
            assert len(driver.find_elements(By.XPATH, '//*[contains(text(),"€")]')) == 1, \
                '€ still displayed on page'
        if curriency == "€":
            assert len(driver.find_elements(By.XPATH, '//*[contains(text(),"£")]')) == 1, \
                '£ still displayed on page'
            assert len(driver.find_elements(By.XPATH, '//*[contains(text(),"$") '
                                                      'and not(@type="text/javascript")'
                                                      'and not(@onclick)]')) == 1, \
                '$ still displayed on page'
        if curriency == "£":
            assert len(driver.find_elements(By.XPATH, '//*[contains(text(),"$") '
                                                      'and not(@type="text/javascript")'
                                                      'and not(@onclick)]')) == 1, \
                '$ still displayed on page'
            assert len(driver.find_elements(By.XPATH, '//*[contains(text(),"€")]')) == 1, \
                '€ still displayed on page'
