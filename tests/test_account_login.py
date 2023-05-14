import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
class TestAccountLogin:
    def test_sign_in_button_log_in(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT).click()
        time.sleep(2)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))
        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.EMAIL).send_keys("mariapetrova091996@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.PASSWORD).send_keys("theory120396")

        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        time.sleep(2)
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        time.sleep(2)
        email = driver.find_element(*TestLocators.PERSONAL_ACCOUNT_EMAIL).get_attribute('value')
        assert email == "mariapetrova091996@yandex.ru", "Не удалось войти в аккаунт"

    # Вход через кнопку «Личный кабинет»
    def test_sign_in_button_personal_account(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))
        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.EMAIL).send_keys("mariapetrova091996@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.PASSWORD).send_keys("theory120396")
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        time.sleep(2)
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        time.sleep(2)
        email = driver.find_element(*TestLocators.PERSONAL_ACCOUNT_EMAIL).get_attribute('value')
        assert email == "mariapetrova091996@yandex.ru", "Не удалось войти в аккаунт"

    # Вход через кнопку в форме регистрации
    def test_sign_in_button_in_registration_form(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT).click()
        time.sleep(2)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))
        driver.find_element(*TestLocators.SIGN_REGISTER).click()
        time.sleep(2)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.SIGN_LOG_IN)))
        driver.find_element(*TestLocators.SIGN_LOG_IN).click()
        time.sleep(2)

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))
        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.EMAIL).send_keys("mariapetrova091996@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.PASSWORD).send_keys("theory120396")
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        time.sleep(2)

        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        time.sleep(2)

        email = driver.find_element(*TestLocators.PERSONAL_ACCOUNT_EMAIL).get_attribute('value')
        assert email == "mariapetrova091996@yandex.ru", "Не удалось войти в аккаунт"

    def test_sign_in_button_in_password_recovery_form(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT).click()
        time.sleep(2)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))

        driver.find_element(*TestLocators.SIGN_RESTORE_PASSWORD).click()
        time.sleep(2)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located
                                       ((TestLocators.SIGN_LOG_IN_RESTORE_PASSWORD)))

        driver.find_element(*TestLocators.SIGN_LOG_IN_RESTORE_PASSWORD).click()
        time.sleep(2)
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))

        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.EMAIL).send_keys("mariapetrova091996@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.PASSWORD).send_keys("theory120396")
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        time.sleep(2)

        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        time.sleep(2)

        email = driver.find_element(*TestLocators.PERSONAL_ACCOUNT_EMAIL).get_attribute('value')
        assert email == "mariapetrova091996@yandex.ru", "Не удалось войти в аккаунт"
