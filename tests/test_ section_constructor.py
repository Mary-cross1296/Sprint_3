import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


#Переход по клику на «Конструктор» из вкладки "Лента заказов" (без предварительной авторизации)
def test_clicking_on_constructor_from_order_feed(driver):
    driver.find_element(*TestLocators.BUTTON_ORDER_TAPE).click()
    time.sleep(2)

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_ORDER_TAPE)))
    driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
    time.sleep(2)

    header = driver.find_element(*TestLocators.TITLE_COLLECT_BURGER).text
    assert header == "Соберите бургер", "Не удалось выполнить переход с вкладки 'Лента заказов' на вкладку 'Конструктор'"
    driver.quit()


# Переход по клику на «Конструктор» из вкладки "Личный кабинет" (с предварительной авторизацией)
def test_clicking_on_constructor_from_personal_account(driver):
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))
    driver.find_element(*TestLocators.EMAIL).click()
    driver.find_element(*TestLocators.EMAIL).send_keys("mariapetrova091996@yandex.ru")
    driver.find_element(*TestLocators.PASSWORD).click()
    driver.find_element(*TestLocators.PASSWORD).send_keys("theory120396")
    driver.find_element(*TestLocators.BUTTON_LOGIN).click()
    time.sleep(2)
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    time.sleep(2)

    driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
    time.sleep(2)

    header = driver.find_element(*TestLocators.TITLE_COLLECT_BURGER).text
    assert header == "Соберите бургер", "Не удалось выполнить переход с вкладки 'Личный кабинет' на вкладку 'Конструктор'"
    driver.quit()


#Переход по клику на логотип Stellar Burgers из вкладки "Личный кабинет" (с предварительной авторизацией)
def test_click_on_stellar_burgers_logo(driver):
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL )))
    driver.find_element(*TestLocators.EMAIL).click()
    driver.find_element(*TestLocators.EMAIL).send_keys("mariapetrova091996@yandex.ru")
    driver.find_element(*TestLocators.PASSWORD).click()
    driver.find_element(*TestLocators.PASSWORD).send_keys("theory120396")
    driver.find_element(*TestLocators.BUTTON_LOGIN).click()
    time.sleep(2)

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.TITLE_COLLECT_BURGER)))
    driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
    time.sleep(2)

    driver.find_element(*TestLocators.LOGO_STELLAR_BURGER).click()
    time.sleep(2)
    header = driver.find_element(*TestLocators.TITLE_COLLECT_BURGER).text
    assert header == "Соберите бургер", "Не удалось выполнить переход в 'Конструктор' по клику на Лого"
    driver.quit()


#Переход к разделу «Булки»
def test_go_section_breads(driver):
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_CONSTRUCTOR)))
    driver.find_element(*TestLocators.TAB_FILLINGS).click()
    time.sleep(1)
    no_selected_breads = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[1]").get_attribute('class')
    assert no_selected_breads == "tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect", "Вкладка булки не доступна для клика"

    driver.find_element(*TestLocators.TAB_BREADS).click()
    time.sleep(1)
    selected_breads = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[1]").\
        get_attribute('class')
    time.sleep(1)
    assert selected_breads == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"
    driver.quit()


#Переход к разделу «Соусы»
def test_go_section_sauces(driver):
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_CONSTRUCTOR)))
    no_selected_sauces = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[2]").get_attribute('class')

    time.sleep(1)
    assert no_selected_sauces == "tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"

    driver.find_element(*TestLocators.TAB_SAUCES).click()
    time.sleep(1)
    selected_sauces = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[2]").get_attribute("class")
    assert selected_sauces == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"
    driver.quit()


#Переход к разделу «Начинки»
def test_go_section_fillings(driver):
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.BUTTON_CONSTRUCTOR)))
    no_selected_sauces = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[3]").get_attribute('class')

    time.sleep(1)
    assert no_selected_sauces == "tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"

    driver.find_element(*TestLocators.TAB_FILLINGS).click()
    time.sleep(1)
    selected_sauces = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[3]").get_attribute("class")
    assert selected_sauces == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"
    driver.quit()

