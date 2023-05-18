import pytest
import random
import string
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
