"""
Фикстура для проекта
"""
import datetime
import logging
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="ch", choices=["ya", "ch", "ff"])
    parser.addoption("--headless", action="store_true")
    parser.addoption("--yadriver", action="store_true",
                     default='C:/Users/mx/Downloads/'
                             'yandexdriver-24.6.0.1874-win64/yandexdriver.exe')
    parser.addoption("--url", default='http://10.0.1.11:8081')
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != 'passed':
        item.status = 'failed'
    else:
        item.status = 'passed'


@pytest.fixture()
def browser(request):
    """
    В фикстуре задается браузер, базовый url opencart, уровеь логирования,
    а также режим headless и путь к yandexdriver.exe для запуска yandex браузера.
    Возвращает драйвер и базовый url.
    """
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    yadriver = request.config.getoption("--yadriver")
    base_url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")

    logger = logging.getLogger(request.node.name)
    filename = (f"logs/{request.node.name}.log").replace('/', '_')
    file_handler = logging.FileHandler(f"logs/{filename}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s:%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

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

    driver.logger = logger

    logger.info("Browser %s started" % browser)

    yield driver, base_url

    if request.node.status == "failed":
        allure.attach(name="failure_screenshot", body=driver.get_screenshot_as_png(),
                      attachment_type=allure.attachment_type.PNG)
        allure.attach(name="page_source", body=driver.page_source,
                      attachment_type=allure.attachment_type.HTML)

    def fin():
        driver.quit()
        logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))

    request.addfinalizer(fin)
