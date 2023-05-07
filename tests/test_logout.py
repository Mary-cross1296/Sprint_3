import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Выход по кнопке «Выйти» в личном кабинете
def test_sign_out_button_personal_account():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, ".//nav/a/p[text()='Личный Кабинет']").click()
    time.sleep(2)

    WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located
                                  ((By.XPATH, ".//form/fieldset[1]/div/div/label[text()='Email']" )))
    driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").click()
    driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys("mariapetrova091996@yandex.ru")
    driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").click()
    driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").send_keys("theory120396")
    driver.find_element(By.XPATH, ".//form/button[text()='Войти']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, ".//nav/a/p[text()='Личный Кабинет']").click()
    time.sleep(2)
    email = driver.find_element(By.XPATH, ".//li[2]/div/div/input").get_attribute('value')
    assert email == "mariapetrova091996@yandex.ru", "Не удалось войти в аккаунт"

    driver.find_element(By.XPATH, ".//main/div/nav/ul/li/button[text()='Выход']").click()
    time.sleep(2)

    WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located
                                  ((By.XPATH, ".//form/fieldset[1]/div/div/label[text()='Email']" )))
    text_login = driver.find_element(By.XPATH, ".//main/div/h2").text
    driver.quit()
    assert text_login == "Вход"
