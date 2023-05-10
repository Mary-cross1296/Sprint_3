import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

def test_registration_new_user(driver, rand_email, rand_password, rand_name):
    time.sleep(3)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_PERSONAL_ACCOUNT)))

    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    time.sleep(3)

    driver.find_element(*TestLocators.SIGN_REGISTER).click()
    time.sleep(3)

    #Регистрация нового пользователя
    driver.find_element(*TestLocators.REG_NAME).click()
    driver.find_element(*TestLocators.REG_NAME).send_keys(rand_name)
    driver.find_element(*TestLocators.REG_EMAIL).click()
    driver.find_element(*TestLocators.REG_EMAIL).send_keys(rand_email)
    driver.find_element(*TestLocators.REG_PASSWORD).click()
    driver.find_element(*TestLocators.REG_PASSWORD).send_keys(rand_password)
    time.sleep(2)
    driver.find_element(*TestLocators.REG_BUTTON_REGISTER).click()
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "https://stellarburgers.nomoreparties.site/login", "Новый пользователь не зарегистрирован"

    #Вход с даннымы вновь зарегистрированного пользователя
    time.sleep(2)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.TITLE_LOGIN)))

    driver.find_element(*TestLocators.EMAIL).click()
    driver.find_element(*TestLocators.EMAIL).send_keys(rand_email)
    driver.find_element(*TestLocators.PASSWORD).click()
    driver.find_element(*TestLocators.PASSWORD).send_keys(rand_password)
    driver.find_element(*TestLocators.BUTTON_LOGIN).click()
    time.sleep(2)

    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    time.sleep(3)
    new_email = driver.find_element(*TestLocators.PERSONAL_ACCOUNT_EMAIL).get_attribute("value")
    assert new_email == str.lower(rand_email)


def test_registration_with_invalid_password(driver, rand_name, rand_email, invalid_rand_password):
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_PERSONAL_ACCOUNT)))

    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    time.sleep(3)

    driver.find_element(*TestLocators.SIGN_REGISTER).click()

    #Регистрация нового пользователя
    driver.find_element(*TestLocators.REG_NAME).click()
    driver.find_element(*TestLocators.REG_NAME).send_keys(rand_name)
    driver.find_element(*TestLocators.REG_EMAIL).click()
    driver.find_element(*TestLocators.REG_EMAIL).send_keys(rand_email)
    driver.find_element(*TestLocators.REG_PASSWORD).click()
    driver.find_element(*TestLocators.REG_PASSWORD).send_keys(invalid_rand_password)
    driver.find_element(*TestLocators.REG_BUTTON_REGISTER).click()
    time.sleep(3)
    error_message = driver.find_element(*TestLocators.REG_ERROR_MESSAGE).text
    assert error_message == "Некорректный пароль", "Успешная регистрация пользователя с паролем менее 6 символов"
