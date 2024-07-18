"""
Фикстура для проекта
"""
import os
import random
import time
import datetime
import logging
import pytest
import allure
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.edge.options import Options as EdOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox"])
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", default='http://10.0.1.11:8081')
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--mobile", action="store_true")
    parser.addoption("--vnc", action="store_true")
    parser.addoption("--logs", action="store_true")
    parser.addoption("--bv")


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
    base_url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    executor_url = f'http://{executor}:4444/wd/hub'
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    logs = request.config.getoption("--logs")
    mobile = request.config.getoption("--mobile")

    logger = logging.getLogger(request.node.name)
    filename = (f"logs/{request.node.name}.log").replace('/', '_')
    file_handler = logging.FileHandler(f"logs/{filename}.log")
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(name)s:%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if browser_name == "chrome":
        options = Options()
        if headless_mode:
            options.add_argument("headless=new")
    elif browser_name == "firefox":
        options = FFOptions()
        if headless_mode:
            options.add_argument("--headless")
    else:
        raise ValueError(f"Browser {browser_name} not supported")

    caps = {
        "browserName": browser_name,
        "browserVersion": version,
        "selenoid:options": {
            "enableVNC": vnc,
            "name": request.node.name,
            "enableLog": logs
        },
        "acceptInsecureCerts": True
    }

    for k, v in caps.items():
        options.set_capability(k, v)

    driver = webdriver.Remote(command_executor=executor_url, options=options)

    if not mobile:
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
