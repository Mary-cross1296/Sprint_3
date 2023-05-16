import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
from faker import Faker


def test_go_section_fillings(driver):
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((TestLocators.BUTTON_CONSTRUCTOR)))
    no_selected_fillings = driver.find_element(*TestLocators.TAB_FILLINGS_SELECTED_OR_NO_SELECTED).get_attribute(
        'class')
    time.sleep(1)
    assert 'tab_tab_type_current__2BEPc' not in no_selected_fillings

    driver.find_element(*TestLocators.TAB_FILLINGS).click()
    time.sleep(1)
    selected_fillings = driver.find_element(*TestLocators.TAB_FILLINGS_SELECTED_OR_NO_SELECTED).get_attribute("class")
    assert 'tab_tab_type_current__2BEPc' in selected_fillings