from selenium.webdriver.common.by import By

class TestLocators:
    #Главная страница
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, ".//nav/a/p[text()='Личный Кабинет']" #Кнопка личный кабинет на главной странице
    BUTTON_ORDER_TAPE = By.XPATH, ".//li/a/p[text()='Лента Заказов']" #Кнопка "Лента заказов"
    BUTTON_CONSTRUCTOR = By.XPATH, ".//li/a/p[text()='Конструктор']" #Кнопка "Конструктор"
    BUTTON_LOGIN_ACCOUNT = By.XPATH, ".//main/section[2]/div/button[text()='Войти в аккаунт']" #Кнопка "Войти в аккаунт"
    TITLE_COLLECT_BURGER = By.XPATH, ".//section/h1['Соберите бургер']" #Заголовок "Соберите бургер"
    LOGO_STELLAR_BURGER = By.XPATH, ".//header/nav/div/a" #Логотип Stellar Burger
    TAB_BREADS = By.XPATH, ".//div/span[text() = 'Булки']" #Вкладка "Булки"
    TAB_BREADS_SELECTED_OR_NO_SELECTED = By.XPATH, ".//div/div/span[text() = 'Булки']/.." #Вкладка "Булки" выбрана/не выбрана
    TAB_SAUCES = By.XPATH, ".//div/span[text() = 'Соусы']" #Вкладка "Соусы"
    TAB_SAUCES_SELECTED_OR_NO_SELECTED = By.XPATH, ".//div/div/span[text() = 'Соусы']/.." #Вкладка "Соусы" выбрана/не выбрана
    TAB_FILLINGS = By.XPATH, ".//div/span[text() = 'Начинки']" #Вкладка "Начинки"
    TAB_FILLINGS_SELECTED_OR_NO_SELECTED = By.XPATH, ".//div/div/span[text() = 'Начинки']/.." #Вкладка "Начинки" выбрана/не выбрана

    #Регистрация
    SIGN_LOG_IN = By.XPATH, ".//p/a[text()='Войти']" #Надпись "Войти"
    REG_NAME = By.XPATH, ".//div/label[text() = 'Имя']/following::input" #Поле "Имя"
    REG_EMAIL = By.XPATH, ".//div/label[text() = 'Email']/following::input" #Поле "Email"
    REG_PASSWORD = By.XPATH, ".//div/label[text() = 'Пароль']/following::input" #Поле "Password"
    REG_BUTTON_REGISTER = By.XPATH, ".//form/button[text()='Зарегистрироваться']" #Кнопка "Зарегистрироваться"
    REG_ERROR_MESSAGE = By.XPATH, ".//div/p[text()='Некорректный пароль']" #Сообщение о "Неправильном пароле"

    #Восстановленее пароля
    SIGN_LOG_IN_RESTORE_PASSWORD = By.XPATH, ".//main/div/div/p/a[text()='Войти']" #Надпись войти

    #Авторизация (Вход в аккаунт)
    TITLE_LOGIN = By.XPATH, ".//main/div/h2[text()='Вход']" #Заголовок "Вход"
    EMAIL = By.XPATH, ".//div/label[text()='Email']/following::input" #Поле email
    LABEL_EMAIL = By.XPATH, ".//div/label[text()='Email']" #Подпись поля email
    PASSWORD = By.XPATH, ".//div/label[text()='Пароль']/following::input" #Поле Пароль
    BUTTON_LOGIN = By.XPATH, ".//form/button[text()='Войти']" #Кнопка Войти
    SIGN_REGISTER = By.XPATH, ".//div/p/a[text()='Зарегистрироваться']" #Надпись "Зарегистрироваться"
    SIGN_RESTORE_PASSWORD = \
        By.XPATH, ".//div/p[text()='Забыли пароль?']/a[text()='Восстановить пароль']" #Надпись "Восстановить пароль"

    #Личный кабинет
    PERSONAL_ACCOUNT_EMAIL = By.XPATH, ".//div/label[text()='Логин']/following::input" #Поле Email
    PERSONAL_ACCOUNT_BUTTON_LOGOUT = By.XPATH, ".//ul/li/button[text()='Выход']" #Кнопка "Выход"
