from selenium.webdriver.common.by import By


class PageLocators:
    URL = "https://stellarburgers.nomoreparties.site/"

    PROFILE_URL = 'https://stellarburgers.nomoreparties.site/account/profile'

    LOGIN_PAGE = 'https://stellarburgers.nomoreparties.site/login'

    RESET_PWS_PAGE = 'https://stellarburgers.nomoreparties.site/reset-password'

    RESTORE_PWD_PAGE = 'https://stellarburgers.nomoreparties.site/forgot-password'

    REGISTRATION_URL = 'https://stellarburgers.nomoreparties.site/register'

    # кнопка выхода
    EXIT_BUTTON = By.XPATH, "// button[text() = 'Выход']"

    # кнопка регистрации
    REGISTRATION_BUTTON = By.XPATH, "//main/div/div/p/a[@class='Auth_link__1fOlj']"

    # поле ввода почты
    MAIL = By.XPATH, "//input[@type='text']"

    # кнопка авторизации
    AUTORISATION_BUTTON = By.XPATH, "//form/button[text()='Войти']"

    # поле ввода пароля
    PASSWORD_BUTTON = By.XPATH, "//input[@type='password']"

    # кнопка входа
    ENTRANCE_BUTTON = By.XPATH, "//div/button[text()='Войти в аккаунт']"

    # личный кабинет
    KABINET_LOCATOR = By.XPATH, "//header/nav/a/p"

    # Logo Бургерной
    LOGO_BURGER = By.XPATH, "//div/a[@href='/']"

    # Текст конструктора
    CONSTRUCTOR_TEXT = By.XPATH, "//main/section/h1[1]"

    # кнопка конструктора
    CONSTRUCTOR_LOCATOR = By.XPATH, "//header/nav/ul/li[1]/a/p"

    # кнопка возврата на страницу авторизации
    BACK_TO_LOGIN_BUTTON = By.XPATH, "//div/main/div/div/p/a[@href='/login']"

    # Кнопка восстановления пароля
    RESTORE_PSWD_BUTTON = By.XPATH, "//main/div/div/p/a[@href='/forgot-password']"

    # идентификатор выбранного поля Начинки\Соусы\Булки
    SPIN_BUTTONS_URL = By.XPATH, ("//main/section/div/div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 "
                                  "pr-10 pb-4 pl-10 noselect']")

    # Кнопка 'Начинки'
    SPIN_STUFFINN_BUTTON = By.XPATH, "//main/section/div/div/span[text()='Начинки']"

    # Кнопка 'Соусы'
    SPIN_SOUCES_BUTTON = By.XPATH, "//main/section/div/div/span[text()='Соусы']"

    # Кнопка 'Булки'
    SPIN_BREAD_BUTTON = By.XPATH, "//main/section/div/div/span[text()='Булки']"

    #поле ввода имени в форме Регистрации
    NAME_FIELD_REGISTRASTION = By.XPATH, ("//fieldset[1]/div/div/input[@class='text input__textfield "
                                          "text_type_main-default']")

    #поле ввода почты в форме Регистрации
    EMAIL_FIELD_REGISTRASTION = By.XPATH, ("//fieldset[2]/div/div/input[@class='text input__textfield "
                                           "text_type_main-default']")

    #поле ввода пароля в форме Регистрации
    PWD_FIELD_REGISTRASTION = By.XPATH, ("//fieldset[3]/div/div/input[@class='text input__textfield "
                                         "text_type_main-default']")

    # кнопка Регистрации на форме Регистрации
    REGISTRATION_BUTTON_ON_REGISTR_PAGE = By.XPATH, ("//button[@class='button_button__33qZ0 "
                                                     "button_button_type_primary__1O7Bx "
                                                     "button_button_size_medium__3zxIa']")

    # текст некорректного ввода пароля
    INCORRECT_PWD_TEXT = By.XPATH, "//p[@class='input__error text_type_main-default']"
