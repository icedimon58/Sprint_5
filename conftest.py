import pytest
from selenium import webdriver
from tests.page_locators import PageLocators


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(PageLocators.URL)
    yield driver
    driver.quit()
