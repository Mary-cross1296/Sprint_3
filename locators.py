from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLocators:
    LC = (By.XPATH, ".//nav/a/p[text()='Личный Кабинет']")
    EMAIL = (By.XPATH, ".//form/fieldset[1]/div/div/input")