import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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

