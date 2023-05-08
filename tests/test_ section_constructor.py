import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#Переход по клику на «Конструктор» из вкладки "Лента заказов" (без предварительной авторизации)
def test_clicking_on_constructor_from_order_feed():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    driver.find_element(By.XPATH, ".//header/nav/ul/li/a/p[text()='Лента Заказов']").click()
    time.sleep(2)
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located
                                   ((By.XPATH, ".//main/div/h1[text()='Лента заказов']")))
    driver.find_element(By.XPATH, ".//header/nav/ul/li/a/p[text()='Конструктор']").click()
    time.sleep(2)

    header = driver.find_element(By.XPATH, ".//section[1]/h1").text
    assert header == "Соберите бургер", "Не удалось выполнить переход с вкладки 'Лента заказов' на вкладку 'Конструктор'"


# Переход по клику на «Конструктор» из вкладки "Личный кабинет" (с предварительной авторизацией)
def test_clicking_on_constructor_from_personal_account():
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

    driver.find_element(By.XPATH, ".//header/nav/ul/li/a/p[text()='Конструктор']").click()
    time.sleep(2)

    header = driver.find_element(By.XPATH, ".//section[1]/h1").text
    assert header == "Соберите бургер", "Не удалось выполнить переход с вкладки 'Личный кабинет' на вкладку 'Конструктор'"


#Переход по клику на логотип Stellar Burgers из вкладки "Личный кабинет" (с предварительной авторизацией)
def test_click_on_stellar_burgers_logo():
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

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located
                                   ((By.XPATH, ".//form/fieldset[1]/div/div/label[text()='Email']")))
    driver.find_element(By.XPATH, ".//nav/a/p[text()='Личный Кабинет']").click()

    driver.find_element(By.XPATH, ".//header/nav/div/a").click()
    header = driver.find_element(By.XPATH, ".//section[1]/h1").text
    driver.quit()
    assert header == "Соберите бургер", "Не удалось выполнить переход в 'Конструктор' по клику на Лого"


#Переход к разделу «Булки»
def test_go_section_breads():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//header/nav/ul/li/a/p[text()='Конструктор']")))
    driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[3]/span[text() = 'Начинки']").click()
    time.sleep(1)
    no_selected_breads = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[1]").get_attribute('class')
    assert no_selected_breads == "tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect", "Вкладка булки не доступна для клика"

    driver.find_element(By.XPATH, ".//main/section[1]/div/div/span[text() = 'Булки']").click()
    time.sleep(1)
    selected_breads = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[1]").\
        get_attribute('class')
    time.sleep(1)
    assert selected_breads == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"
    driver.quit()

#Переход к разделу «Соусы»
def test_go_section_sauces():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//header/nav/ul/li/a/p[text()='Конструктор']")))
    no_selected_sauces = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[2]").get_attribute('class')

    time.sleep(1)
    assert no_selected_sauces == "tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"

    driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[2]/span[text() = 'Соусы']").click()
    time.sleep(1)
    selected_sauces = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[2]").get_attribute("class")
    assert selected_sauces == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"

#Переход к разделу «Начинки»
def test_go_section_fillings():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//header/nav/ul/li/a/p[text()='Конструктор']")))
    no_selected_sauces = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[3]").get_attribute('class')

    time.sleep(1)
    assert no_selected_sauces == "tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"

    driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[3]/span[text() = 'Начинки']").click()
    time.sleep(1)
    selected_sauces = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[3]").get_attribute("class")
    assert selected_sauces == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"


