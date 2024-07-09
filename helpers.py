"""
Вспомогательные функции для тестов
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def find_visible_element(locator, driver, timeout=1, by=By.XPATH):
    """
    Функция поиска по XPATH элемента, который видим в dom и на странице
    """
    try:
        # WebDriverWait(driver, timeout).until(EC.title_is((title)))
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))
    except TimeoutException:
        driver.save_screenshot(f"screenshots/{driver.session_id}.png")
        raise AssertionError(f"Не дождались видимости элемента: {locator} за {timeout} секунд")

def check_page_title(title, driver, timeout=1):
    """
    Функция проверки титула страницы
    """
    try:
        t = WebDriverWait(driver, timeout).until(EC.title_is(title))
    except TimeoutException:
        driver.save_screenshot(f"screenshots/{driver.session_id}.png")
        raise AssertionError(f"Титул страницы {t} вместо {title}")