import pytest
from selenium import webdriver
from data import PageUrls


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get(PageUrls.URL)
    yield driver
    driver.quit()
