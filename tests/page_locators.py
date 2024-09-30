from selenium.webdriver.common.by import By


class PageLocators:


    # кнопка выхода
    EXIT_BUTTON = By.XPATH, "//button[text()='Выход']"

    # кнопка регистрации
    REGISTRATION_BUTTON = By.XPATH, "//a[@href='/register']"

    # поле ввода почты
    MAIL = By.XPATH, "//input[@type='text']"

    # кнопка авторизации
    AUTORISATION_BUTTON = By.XPATH, "//button[text()='Войти']"

    # поле ввода пароля
    PASSWORD_BUTTON = By.XPATH, "//input[@type='password']"

    # кнопка входа
    ENTRANCE_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']"

    # личный кабинет
    KABINET_LOCATOR = By.XPATH, "//header/nav/a/p"

    # Logo Бургерной
    LOGO_BURGER = By.XPATH, "//a[@href='/']"

    # Текст конструктора
    CONSTRUCTOR_TEXT = By.XPATH, "//h1[@class='text text_type_main-large mb-5 mt-10']"

    # кнопка конструктора
    CONSTRUCTOR_LOCATOR = By.XPATH, "//a[@href='/']/p[@class='AppHeader_header__linkText__3q_va ml-2']"

    # кнопка возврата на страницу авторизации
    BACK_TO_LOGIN_BUTTON = By.XPATH, "//a[@href='/login']"

    # Кнопка восстановления пароля
    RESTORE_PSWD_BUTTON = By.XPATH, "//a[@href='/forgot-password']"

    # идентификатор выбранного поля Начинки\Соусы\Булки
    SPIN_BUTTONS_URL = By.XPATH, ("//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 "
                                  "pr-10 pb-4 pl-10 noselect']")

    # Кнопка 'Начинки'
    SPIN_STUFFINN_BUTTON = By.XPATH, "//span[text()='Начинки']"

    # Кнопка 'Соусы'
    SPIN_SOUCES_BUTTON = By.XPATH, "//span[text()='Соусы']"

    # Кнопка 'Булки'
    SPIN_BREAD_BUTTON = By.XPATH, "//span[text()='Булки']"

    #поле ввода имени в форме Регистрации
    NAME_FIELD_REGISTRASTION = By.XPATH, ("//*[text()='Имя']/following-sibling::input")

    #поле ввода почты в форме Регистрации
    EMAIL_FIELD_REGISTRASTION = By.XPATH, ("//*[text()='Email']/following-sibling::input")

    #поле ввода пароля в форме Регистрации
    PWD_FIELD_REGISTRASTION = By.XPATH, ("//input[@type='password']")

    # кнопка Регистрации на форме Регистрации
    REGISTRATION_BUTTON_ON_REGISTR_PAGE = By.XPATH, ("//button[@class='button_button__33qZ0 "
                                                     "button_button_type_primary__1O7Bx "
                                                     "button_button_size_medium__3zxIa']")

    # текст некорректного ввода пароля
    INCORRECT_PWD_TEXT = By.XPATH, "//p[@class='input__error text_type_main-default']"
