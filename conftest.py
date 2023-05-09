import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver():
    get_driver = webdriver.Chrome()
    get_driver.get("https://stellarburgers.nomoreparties.site/")

    return get_driver

@pytest.fixture()
def rand_name():
    letters_and_digits = string.ascii_letters + string.digits
    length = random.randint(3, 10)
    random_name = ''.join(random.sample(letters_and_digits, length))
    return random_name
@pytest.fixture()
def rand_email():
    letters_and_digits = string.ascii_letters + string.digits
    length = random.randint(3,10)
    random_name = ''.join(random.sample(letters_and_digits, length))
    random_domain = ''.join(random.sample(letters_and_digits, length))
    random_email = random_name + "@" + random_domain + "." + str(random.choice(['net', 'com', 'ua', 'ru', 'org']))
    return random_email

@pytest.fixture()
def rand_password():
    letters_and_digits = string.ascii_letters + string.digits
    length_password = random.randint(6, 15)
    random_password = ''.join(random.sample(letters_and_digits, length_password))
    return random_password

@pytest.fixture()
def invalid_rand_password():
    letters_and_digits = string.ascii_letters + string.digits
    length_password = random.randint(0, 6)
    random_password = ''.join(random.sample(letters_and_digits, length_password))
    return random_password


