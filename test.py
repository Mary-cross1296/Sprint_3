import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_go_section_breads():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//header/nav/ul/li/a/p[text()='Конструктор']")))
    driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[3]/span[text() = 'Начинки']").click()
    time.sleep(3)
    not_selected_breads = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[1]").get_attribute('class')
    assert not_selected_breads == "tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect", "Вкладка булки не доступна для клика"

    driver.find_element(By.XPATH, ".//main/section[1]/div/div/span[text() = 'Булки']").click()
    time.sleep(3)
    selected_breads = driver.find_element(By.XPATH, ".//main/section[1]/div[1]/div[1]").\
        get_attribute('class')
    time.sleep(3)
    assert selected_breads == "tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"
    driver.quit()

