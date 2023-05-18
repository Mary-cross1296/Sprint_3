import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators

class TestAccountLogout:
    def test_sign_out_button_personal_account(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))
        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.EMAIL).send_keys("mariapetrova091996@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.PASSWORD).send_keys("theory120396")
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.PERSONAL_ACCOUNT_BUTTON_LOGOUT)))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON_LOGOUT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))
        text_login = driver.find_element(*TestLocators.TITLE_LOGIN).text
        assert text_login == "Вход"
