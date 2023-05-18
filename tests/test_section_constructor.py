from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators


class TestSectionConstructor:
    def test_clicking_on_constructor_from_order_feed(self, driver):
        driver.find_element(*TestLocators.BUTTON_ORDER_TAPE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUTTON_ORDER_TAPE)))
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        header = driver.find_element(*TestLocators.TITLE_COLLECT_BURGER).text
        assert header == "Соберите бургер", "Не удалось выполнить переход с вкладки 'Лента заказов' на вкладку 'Конструктор'"

    def test_clicking_on_constructor_from_personal_account(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))
        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.EMAIL).send_keys("mariapetrova091996@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.PASSWORD).send_keys("theory120396")
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.BUTTON_CONSTRUCTOR).click()
        header = driver.find_element(*TestLocators.TITLE_COLLECT_BURGER).text
        assert header == "Соберите бургер", "Не удалось выполнить переход с вкладки 'Личный кабинет' на вкладку 'Конструктор'"

    def test_click_on_stellar_burgers_logo(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))
        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.EMAIL).send_keys("mariapetrova091996@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.PASSWORD).send_keys("theory120396")
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.TITLE_COLLECT_BURGER)))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        driver.find_element(*TestLocators.LOGO_STELLAR_BURGER).click()
        header = driver.find_element(*TestLocators.TITLE_COLLECT_BURGER).text
        assert header == "Соберите бургер", "Не удалось выполнить переход в 'Конструктор' по клику на Лого"

    def test_go_section_breads(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUTTON_CONSTRUCTOR)))
        driver.find_element(*TestLocators.TAB_FILLINGS).click()
        no_selected_breads = driver.find_element(*TestLocators.TAB_BREADS_SELECTED_OR_NO_SELECTED).get_attribute(
            'class')
        assert 'tab_tab_type_current__2BEPc' not in no_selected_breads, "Вкладка булки не доступна для клика"

        driver.find_element(*TestLocators.TAB_BREADS).click()
        selected_breads = driver.find_element(*TestLocators.TAB_BREADS_SELECTED_OR_NO_SELECTED).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in selected_breads

    def test_go_section_sauces(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUTTON_CONSTRUCTOR)))
        no_selected_sauces = driver.find_element(*TestLocators.TAB_SAUCES_SELECTED_OR_NO_SELECTED).get_attribute(
            'class')
        assert 'tab_tab_type_current__2BEPc' not in no_selected_sauces
        driver.find_element(*TestLocators.TAB_SAUCES).click()
        selected_sauces = driver.find_element(*TestLocators.TAB_SAUCES_SELECTED_OR_NO_SELECTED).get_attribute("class")
        assert 'tab_tab_type_current__2BEPc' in selected_sauces

    def test_go_section_fillings(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.BUTTON_CONSTRUCTOR)))
        no_selected_fillings = driver.find_element(*TestLocators.TAB_FILLINGS_SELECTED_OR_NO_SELECTED).get_attribute(
            'class')
        assert 'tab_tab_type_current__2BEPc' not in no_selected_fillings
        driver.find_element(*TestLocators.TAB_FILLINGS).click()
        selected_fillings = driver.find_element(*TestLocators.TAB_FILLINGS_SELECTED_OR_NO_SELECTED).get_attribute(
            "class")
        assert 'tab_tab_type_current__2BEPc' in selected_fillings
