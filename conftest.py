"""
Фикстура для проекта
"""

import pytest

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.firefox.service import Service as FFService

from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    """
    В функции задаются аргументы командной строки pytest.
    """
    parser.addoption("--browser", default="ch", choices=["ya", "ch", "ff"])
    parser.addoption("--headless", action="store_true")
    parser.addoption("--yadriver", action="store_true",
                     default='C:/Users/mx/Downloads/'
                             'yandexdriver-24.6.0.1874-win64/yandexdriver.exe')
    parser.addoption("--url", default='http://10.0.1.19:8081')


@pytest.fixture()
def browser(request):
    """
    В фикстуре задается браузер, базовый url opencart,
    а также режим headless и путь к yandexdriver.exe для запуска yandex браузера.
    Возвращает драйвер и базовый url.
    """
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    yadriver = request.config.getoption("--yadriver")
    base_url = request.config.getoption("--url")
    if browser_name == "ya":
        options = Options()
        if headless_mode:
            options.add_argument("headless=new")
        service = Service(executable_path=yadriver)
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name == "ch":
        options = Options()
        if headless_mode:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(service=Service(), options=options)
    elif browser_name == "ff":
        options = FFOptions()
        if headless_mode:
            options.add_argument("--headless")
        driver = webdriver.Firefox(service=FFService(), options=options)
    else:
        raise ValueError(f"Browser {browser_name} not supported")
    driver.set_window_size(1920, 1080)

    request.addfinalizer(driver.quit)

    return driver, base_url
