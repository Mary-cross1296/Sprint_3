from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLocators:
    #Главная страница
    PERSONAL_ACCOUNT = By.XPATH, ".//nav/a/p[text()='Личный Кабинет']" #Кнопка личный кабинет на главной странице

    #Регистрация



    #Авторизация (Вход в аккаунт)
    TITLE_LOGIN = By.XPATH, ".//main/div/h2[text()='Вход']" #Заголовок "Вход"
    EMAIL = By.XPATH, ".//form/fieldset[1]/div/div/input" #Поле email
    LABEL_EMAIL = By.XPATH, ".//form/fieldset[1]/div/div/label[text()='Email']" #Подпись поля email
    PASSWORD = By.XPATH, ".//form/fieldset[2]/div/div/input" #Поле Пароль
    BUTTON_LOGIN = By.XPATH, ".//form/button[text()='Войти']" #Кнопка Войти
    SIGN_REGISTER = By.XPATH, ".//main/div/div/p/a[text()='Зарегистрироваться']" #Надпись "Зарегистрироваться"
    SIGN_RESTORE_PASSWORD = \
        By.XPATH, ".//main/div/div/p[2][text()='Забыли пароль?']/a[text()='Восстановить пароль']" #Надпись "Восстановить пароль"


    #Личный кабинет
    PERSONAL_ACCOUNT_EMAIL = By.XPATH, ".//li[2]/div/div/input" #Поле Email
    PERSONAL_ACCOUNT_BUTTON_LOGOUT = By.XPATH, ".//main/div/nav/ul/li/button[text()='Выход']" #Кнопка "Выход"


