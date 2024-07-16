"""
Тесты проверки сценариев
"""
import time
import pytest
import allure
from page_objects.admin_page import AdminPage
from page_objects.product_page import ProductPage
from page_objects.currency_page import CarrencyPage
from page_objects.user_page import UserPage
from page_objects.alert_success_element import AlertSuccessElement
from page_objects.alert_confirm_element import AlertConfirmElement
from helpers import get_pages_list


@allure.feature('Authorization/registration')
def test_login_logout_admin(browser):
    """
    Тест покрытия сценария логина-разлогина в админку с проверкой, что логин был выполнен
    """
    admin = AdminPage(browser)
    admin.get_page('administration')
    admin.check_page_title('Administration')
    admin.input_login_admin_form()
    admin.login_admin_account()
    admin.check_page_title('Dashboard')
    admin.logout_admin_account()
    admin.check_page_title('Administration')


@allure.feature('Product')
def test_add_product_in_list_adminpage(browser):
    """
    Тест покрытия сценария добавления нового товара в разделе администратора
    """
    admin = AdminPage(browser)
    admin.get_page('administration')
    admin.input_login_admin_form()
    admin.login_admin_account()
    admin.open_product_list()
    admin.check_page_title('Products')
    admin.click_add_product_button()
    admin.input_new_product()
    admin.click_save_product_button()
    AlertSuccessElement(browser).find_alert()
    AlertSuccessElement(browser).modified_product()


@allure.feature('Product')
def test_delete_product_in_list_adminpage(browser):
    """
    Тест покрытия сценария удаления товара в разделе администратора
    """
    admin = AdminPage(browser)
    admin.get_page('administration')
    admin.input_login_admin_form()
    admin.login_admin_account()
    admin.open_product_list()
    admin.check_page_title('Products')
    admin.delete_product_in_list(1)
    AlertConfirmElement(browser).accept_alert()
    AlertSuccessElement(browser).find_alert()
    AlertSuccessElement(browser).modified_product()


@allure.feature('Product')
def test_add_random_product(browser):
    """
    Тест покрытия сценария добавления в корзину случайного товара с главной страницы
    и проверки, что он появился в корзине
    """
    prod = ProductPage(browser)
    prod.get_page('')
    prod.choose_random_product_on_homepage()
    prod.click_add_to_cart_random_product()
    time.sleep(0.5)
    prod.check_page_title('Your Store')
    AlertSuccessElement(browser).find_alert()
    AlertSuccessElement(browser).add_product()


@allure.feature('Carrency')
def test_switching_currencies(browser):
    """
    Тест покрытия сценария переключения валют из верхнего меню opencart
    """
    currency = CarrencyPage(browser)
    currency.get_page('')
    currency.click_currencies_list()
    current_currency = currency.choose_random_carrency()
    currency.click_random_carrency(current_currency)
    currency.check_random_carrency(current_currency)


@allure.feature('Carrency')
@allure.story('In prices on page')
@pytest.mark.parametrize('url_end', get_pages_list())
def test_check_currencies_on_page(browser, url_end):
    """
    Тест покрытия сценария, что при переключении валют цены на товары меняются
    на главной странице и в каталоге
    """
    currency = CarrencyPage(browser)
    currency.get_page(url_end)
    currency.click_currencies_list()
    current_currency = currency.choose_random_carrency()
    currency.click_random_carrency(current_currency)
    time.sleep(0.5)
    currency.check_currency_on_page(current_currency)


@allure.feature('Authorization/registration')
def test_create_new_user(browser):
    """
    Тест покрытия сценария регистрации нового пользователя в магазине opencart
    """
    user = UserPage(browser)
    user.get_page('en-gb?route=account/register')
    user.input_user_data()
    user.agree_to_the_privacy_policy()
    user.click_continue_button()
    user.check_page_title('Your Account Has Been Created!')
