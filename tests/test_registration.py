import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from faker import Faker

class TestRegistration:
    def test_registration_new_user(self, driver, fake):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.SIGN_REGISTER)))
        driver.find_element(*TestLocators.SIGN_REGISTER).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.REG_NAME)))

        name = fake.name()
        email = fake.email()
        password = fake.password(length=random.randint(6, 12))

        driver.find_element(*TestLocators.REG_NAME).click()
        driver.find_element(*TestLocators.REG_NAME).send_keys(name)
        driver.find_element(*TestLocators.REG_EMAIL).click()
        driver.find_element(*TestLocators.REG_EMAIL).send_keys(email)
        driver.find_element(*TestLocators.REG_PASSWORD).click()
        driver.find_element(*TestLocators.REG_PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.REG_BUTTON_REGISTER).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.TITLE_LOGIN)))
        current_url = driver.current_url
        assert current_url == "https://stellarburgers.nomoreparties.site/login", "Новый пользователь не зарегистрирован"

        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.EMAIL).send_keys(email)
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.PASSWORD).send_keys(password)
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.PERSONAL_ACCOUNT_EMAIL)))
        new_email = driver.find_element(*TestLocators.PERSONAL_ACCOUNT_EMAIL).get_attribute("value")
        assert new_email == str.lower(email)

    def test_registration_with_invalid_password(self, driver, fake):
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
