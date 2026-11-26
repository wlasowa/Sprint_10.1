import pytest
from selenium import webdriver

import urls
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(urls.ROUTES_URL)
    yield browser
    browser.quit()


@pytest.fixture
def main_page(driver):
    return MainPage(driver)


@pytest.fixture
def order_page(driver):
    return OrderPage(driver)
