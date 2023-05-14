from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLocators:
    #Главная страница
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, ".//nav/a/p[text()='Личный Кабинет']" #Кнопка личный кабинет на главной странице
    BUTTON_ORDER_TAPE = By.XPATH, ".//header/nav/ul/li/a/p[text()='Лента Заказов']" #Кнопка "Лента заказов"
    BUTTON_CONSTRUCTOR = By.XPATH, ".//header/nav/ul/li/a/p[text()='Конструктор']" #Кнопка "Конструктор"
    BUTTON_LOGIN_ACCOUNT = By.XPATH, ".//main/section[2]/div/button[text()='Войти в аккаунт']" #Кнопка "Войти в аккаунт"
    TITLE_COLLECT_BURGER = By.XPATH, ".//section[1]/h1" #Заголовок "Соберите бургер"
    LOGO_STELLAR_BURGER = By.XPATH, ".//header/nav/div/a" #Логотип Stellar Burger
    TAB_BREADS = By.XPATH, ".//main/section[1]/div/div/span[text() = 'Булки']" #Вкладка "Булки"
    TAB_SAUCES = By.XPATH, ".//main/section[1]/div[1]/div[2]/span[text() = 'Соусы']" #Вкладка "Соусы"
    TAB_FILLINGS = By.XPATH, ".//main/section[1]/div[1]/div[3]/span[text() = 'Начинки']" #Вкладка "Начинки"


    #Регистрация
    SIGN_LOG_IN = By.XPATH, ".//main/div/div/p/a[text()='Войти']" #Надпись "Войти"
    REG_NAME = By.XPATH, ".//fieldset[1]/div/div/label[text() = 'Имя']/following::input" #Поле "Имя"
    REG_EMAIL = By.XPATH, ".//fieldset[2]/div/div/label[text() = 'Email']/following::input" #Поле "Email"
    REG_PASSWORD = By.XPATH, ".//fieldset[3]/div/div/input" #Поле "Password"
    REG_BUTTON_REGISTER = By.XPATH, ".//main/div/form/button[text()='Зарегистрироваться']" #Кнопка "Зарегистрироваться"
    REG_ERROR_MESSAGE = By.XPATH, ".//form/fieldset[3]/div/p" #Сообщение о "Неправильном пароле"

    #Восстановленее пароля
    SIGN_LOG_IN_RESTORE_PASSWORD = By.XPATH, ".//main/div/div/p/a[text()='Войти']" #Надпись войти

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



