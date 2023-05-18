import pytest
from faker import Faker
from selenium import webdriver

@pytest.fixture
def driver():
    get_driver = webdriver.Chrome()
    get_driver.get("https://stellarburgers.nomoreparties.site/")
    yield get_driver
    get_driver.quit()

@pytest.fixture
def fake():
    faker = Faker()
    return faker
