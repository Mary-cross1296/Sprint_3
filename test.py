import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

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
    driver.quit()
    assert error_message == "Некорректный пароль", "Успешная регистрация пользователя с паролем менее 6 символов"