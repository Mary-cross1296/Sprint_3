from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
class TestAccountLogin:
    def test_sign_in_button_log_in(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))
        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.EMAIL).send_keys("mariapetrova091996@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.PASSWORD).send_keys("theory120396")
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(
            (TestLocators.BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.PERSONAL_ACCOUNT_EMAIL)))
        email = driver.find_element(*TestLocators.PERSONAL_ACCOUNT_EMAIL).get_attribute('value')
        assert email == "mariapetrova091996@yandex.ru", "Не удалось войти в аккаунт"

    def test_sign_in_button_personal_account(self, driver):
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))
        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.EMAIL).send_keys("mariapetrova091996@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.PASSWORD).send_keys("theory120396")
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((TestLocators.BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((TestLocators.PERSONAL_ACCOUNT_EMAIL)))
        email = driver.find_element(*TestLocators.PERSONAL_ACCOUNT_EMAIL).get_attribute('value')
        assert email == "mariapetrova091996@yandex.ru", "Не удалось войти в аккаунт"

    def test_sign_in_button_in_registration_form(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))
        driver.find_element(*TestLocators.SIGN_REGISTER).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.SIGN_LOG_IN)))
        driver.find_element(*TestLocators.SIGN_LOG_IN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))
        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.EMAIL).send_keys("mariapetrova091996@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.PASSWORD).send_keys("theory120396")
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((TestLocators.BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.PERSONAL_ACCOUNT_EMAIL)))
        email = driver.find_element(*TestLocators.PERSONAL_ACCOUNT_EMAIL).get_attribute('value')
        assert email == "mariapetrova091996@yandex.ru", "Не удалось войти в аккаунт"

    def test_sign_in_button_in_password_recovery_form(self, driver):
        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))
        driver.find_element(*TestLocators.SIGN_RESTORE_PASSWORD).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located
                                       ((TestLocators.SIGN_LOG_IN_RESTORE_PASSWORD)))
        driver.find_element(*TestLocators.SIGN_LOG_IN_RESTORE_PASSWORD).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((TestLocators.LABEL_EMAIL)))
        driver.find_element(*TestLocators.EMAIL).click()
        driver.find_element(*TestLocators.EMAIL).send_keys("mariapetrova091996@yandex.ru")
        driver.find_element(*TestLocators.PASSWORD).click()
        driver.find_element(*TestLocators.PASSWORD).send_keys("theory120396")
        driver.find_element(*TestLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable((TestLocators.BUTTON_PERSONAL_ACCOUNT)))
        driver.find_element(*TestLocators.BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (TestLocators.PERSONAL_ACCOUNT_EMAIL)))
        email = driver.find_element(*TestLocators.PERSONAL_ACCOUNT_EMAIL).get_attribute('value')
        assert email == "mariapetrova091996@yandex.ru", "Не удалось войти в аккаунт"
