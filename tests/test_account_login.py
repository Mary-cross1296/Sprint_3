import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Вход по кнопке «Войти в аккаунт» на главной
def test_sign_in_button_log_in():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, ".//main/section[2]/div/button[text()='Войти в аккаунт']").click()
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
    driver.quit()
    assert email == "mariapetrova091996@yandex.ru", "Не удалось войти в аккаунт"


#Вход через кнопку «Личный кабинет»
def test_sign_in_button_personal_account():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, ".//nav/a/p[text()='Личный Кабинет']").click()
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
    driver.quit()
    assert email == "mariapetrova091996@yandex.ru", "Не удалось войти в аккаунт"


#Вход через кнопку в форме регистрации
def test_sign_in_button_in_registration_form():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, ".//main/section[2]/div/button[text()='Войти в аккаунт']").click()
    time.sleep(2)


    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located
                                   ((By.XPATH, ".//form/fieldset[1]/div/div/label[text()='Email']")))
    driver.find_element(By.XPATH, ".//main/div/div/p/a[text()='Зарегистрироваться']").click()
    time.sleep(2)


    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located
                                   ((By.XPATH, ".//main/div/div/p/a[text()='Войти']")))
    driver.find_element(By.XPATH, ".//main/div/div/p/a[text()='Войти']").click()
    time.sleep(2)


    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located
                                   ((By.XPATH, ".//form/fieldset[1]/div/div/label[text()='Email']")))
    driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").click()
    driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys("mariapetrova091996@yandex.ru")
    driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").click()
    driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").send_keys("theory120396")
    driver.find_element(By.XPATH, ".//form/button[text()='Войти']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, ".//nav/a/p[text()='Личный Кабинет']").click()
    time.sleep(2)

    email = driver.find_element(By.XPATH, ".//li[2]/div/div/input").get_attribute('value')
    driver.quit()
    assert email == "mariapetrova091996@yandex.ru", "Не удалось войти в аккаунт"


#Вход через кнопку в форме восстановления пароля
def test_sign_in_button_in_password_recovery_form():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, ".//main/section[2]/div/button[text()='Войти в аккаунт']").click()
    time.sleep(2)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located
                                   ((By.XPATH, ".//form/fieldset[1]/div/div/label[text()='Email']")))

    driver.find_element(By.XPATH,
                        ".//main/div/div/p[2][text()='Забыли пароль?']/a[text()='Восстановить пароль']").click()
    time.sleep(2)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located
                                   ((By.XPATH, ".//main/div/div/p/a[text()='Войти']")))

    driver.find_element(By.XPATH, ".//main/div/div/p/a[text()='Войти']").click()
    time.sleep(2)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located
                                   ((By.XPATH, ".//form/fieldset[1]/div/div/label[text()='Email']")))

    driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").click()
    driver.find_element(By.XPATH, ".//form/fieldset[1]/div/div/input").send_keys("mariapetrova091996@yandex.ru")
    driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").click()
    driver.find_element(By.XPATH, ".//form/fieldset[2]/div/div/input").send_keys("theory120396")
    driver.find_element(By.XPATH, ".//form/button[text()='Войти']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, ".//nav/a/p[text()='Личный Кабинет']").click()
    time.sleep(2)

    email = driver.find_element(By.XPATH, ".//li[2]/div/div/input").get_attribute('value')
    driver.quit()
    assert email == "mariapetrova091996@yandex.ru", "Не удалось войти в аккаунт"



