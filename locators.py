from selenium.webdriver.common.by import By


class Locators:
    # Переход в ЛК с главной
    PERSONAL_ACCOUNT  = (By.XPATH, "//p[text() = 'Личный Кабинет']")
    #Заголовок логина
    ENTRANCE_HEADER = (By.XPATH, ".//h2[text()='Вход']")
   #Кнопка регистрации
    REGISTRATION_BUTTON = (By.XPATH, "//a[text()='Зарегистрироваться']")
    #Заголовок регистрации
    REGISTRATION_HEADER = (By.XPATH, ".//h2[text()='Регистрация']")
#Поле ввода имени
    NAME_INPUT_FIELD = (By.XPATH, "//label[text()='Имя']/following-sibling::*")
#Поле ввода емайл
    EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::*")
    #Поле ввода пароля
    PASSWORD_INPUT_FIELD = (By.XPATH, "//label[text()='Пароль']/following-sibling::*")
#Ошибка заполнения формы регистрации
    INPUT_ERROR = (By.CLASS_NAME, "input__error")
#Подтверждение регистрации
    CONFIRM_REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # регистрации на форме регистрации
#Вход зарегистрированного пользователя
    BUTTON_ENTER = (By.XPATH, "//button[text()='Войти']")
   #Создание заказа
    BUTTON_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")

#Кнопка "Войти в аккаунт"
    BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")
#Кнопка восстановления пароля
    BUTTON_RESTORE_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")
#Заголовок восстановления пароля
    HEADER_RESTORE_PASSWORD = (By.XPATH, ".//h2[text()='Восстановление пароля']")
#Кнопка входа в аккаунт со страницы восстановления
    BUTTON_ENTER_ACCOUNT_FROM_RESTORE = (By.XPATH, "//a[text()='Войти']")
#Заголовок В ЛК
    HEADER_ACCOUNT_PROFILE = (By.XPATH, ".//a[@href='/account/profile']")
#Кнопка выхода из аккаунта
    BUTTON_EXIT_ACCOUNT = (By.XPATH, "//button[text()='Выход']")
#Кнопка конструктор
    MENU_CONSTRUCTOR = (By.XPATH, "//p[text() = 'Конструктор']")
#Логотип Stellar Burgers
    LOGO = (By.XPATH, "//*[@class='AppHeader_header__logo__2D0X2']")

#Заголовок формы заказа
    ORDER_HEADER = (By.XPATH, ".//h1[text()='Соберите бургер']")
#Кнопка соусы
    BUTTON_SAUCES = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Соусы']")
#Заголовок соусы
    HEADER_SAUCES = (By.XPATH, ".//h2[text()='Соусы']")
#Кнопка начинки
    BUTTON_FILLINGS = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Начинки']")
#Заголовок начинки
    HEADER_FILLINGS = (By.XPATH, ".//h2[text()='Начинки']")
#Кнопка булки
    BUTTON_BUNS = (By.XPATH, ".//span[@class='text text_type_main-default' and text()='Булки']")
#Заголовок булки
    HEADER_BUNS = (By.XPATH, ".//h2[text()='Булки']")