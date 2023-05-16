import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from faker import Faker


def test_registration_with_invalid_password(driver, fake):
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((TestLocators.BUTTON_PERSONAL_ACCOUNT)))
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*TestLocators.SIGN_REGISTER).click()
    driver.find_element(*TestLocators.REG_NAME).click()
    driver.find_element(*TestLocators.REG_NAME).send_keys(fake.name())
    driver.find_element(*TestLocators.REG_EMAIL).click()
    driver.find_element(*TestLocators.REG_EMAIL).send_keys(fake.email())
    driver.find_element(*TestLocators.REG_PASSWORD).click()
    driver.find_element(*TestLocators.REG_PASSWORD).send_keys(fake.password(length=5))
    driver.find_element(*TestLocators.REG_BUTTON_REGISTER).click()
    error = driver.find_element(*TestLocators.REG_ERROR_MESSAGE).text
    assert error == "Некорректный пароль", "Успешная регистрация пользователя с паролем менее 6 символов"
