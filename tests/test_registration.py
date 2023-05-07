import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_registration_new_user():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Личный Кабинет")))

    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    time.sleep(3)

    driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()

    #Генерация рандомных значений
    #Email и имя пользователя
    letters_and_digits = string.ascii_letters + string.digits
    length = random.randint(3,10)
    rand_name = ''.join(random.sample(letters_and_digits, length)) #Переменная используется также для поля "Имя"
    rand_domain = ''.join(random.sample(letters_and_digits, length))
    rand_email = rand_name + "@" + rand_domain + "." + str(random.choice(['net', 'com', 'ua', 'ru', 'org']))

    #Генерация пароля
    length_password = random.randint(6, 15)
    rand_password = ''.join(random.sample(letters_and_digits, length_password))

    #Регистрация нового пользователя
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").click()
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(rand_name)
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").click()
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(rand_email)
    driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").click()
    driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys(rand_password)
    time.sleep(2)
    driver.find_element(By.XPATH, ".//main/div/form/button[text()='Зарегистрироваться']").click()
    time.sleep(2)
    current_url = driver.current_url
    assert current_url == "https://stellarburgers.nomoreparties.site/login", "Новый пользователь не зарегистрирован"

    #Вход с даннымы вновь зарегистрированного пользователя
    time.sleep(2)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located
                                   ((By.XPATH, ".//main/div/h2[text()='Вход']")))

    driver.find_element(By.XPATH, ".//main/div/form/fieldset[1]/div/div/input[@name='name']").click()
    driver.find_element(By.XPATH, ".//main/div/form/fieldset[1]/div/div/input[@name='name']").send_keys(rand_email)
    driver.find_element(By.XPATH, ".//main/div/form/fieldset[2]/div/div/input[@name='Пароль']").click()
    driver.find_element(By.XPATH, ".//main/div/form/fieldset[2]/div/div/input[@name='Пароль']").send_keys(rand_password)
    driver.find_element(By.XPATH, ".//main/div/form/button[text()='Войти']").click()
    time.sleep(3)
    current_url = driver.current_url
    driver.quit()
    assert current_url == "https://stellarburgers.nomoreparties.site/" , \
        "Не удалось осуществить вход с данными нового пользователя"


def test_registration_with_invalid_password():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Личный Кабинет")))

    driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
    time.sleep(3)

    driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()

    #Генерация рандомных значений
    #Email и имя пользователя
    letters_and_digits = string.ascii_letters + string.digits
    length = random.randint(3,10)
    rand_name = ''.join(random.sample(letters_and_digits, length)) #Переменная используется также для поля "Имя"
    rand_domain = ''.join(random.sample(letters_and_digits, length))
    rand_email = rand_name + "@" + rand_domain + "." + str(random.choice(['net', 'com', 'ua', 'ru', 'org']))

    #Генерация пароля
    length_password = random.randint(0, 6)
    rand_password = ''.join(random.sample(letters_and_digits, length_password))

    #Регистрация нового пользователя
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").click()
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys(rand_name)
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").click()
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(rand_email)
    driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").click()
    driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys(rand_password)
    time.sleep(2)
    driver.find_element(By.XPATH, ".//main/div/form/button[text()='Зарегистрироваться']").click()
    error_message = driver.find_element(By.XPATH, ".//form/fieldset[3]/div/p").text
    assert error_message == "Некорректный пароль", "Успешная регистрация пользователя с паролем менее 6 символов"
