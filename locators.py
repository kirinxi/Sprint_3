from selenium.webdriver.common.by import By
class Locators:

    # Локаторы для тестирования формы регистрации
    BUTTON_PERSONAL_ACCOUNT = By.XPATH, '//p[contains(text(), "Личный Кабинет")]'    # Кнопка «Личный Кабинет»
    LINK_REGISTRATION = By.XPATH, '//a[contains(text(), "Зарегистрироваться")]'    # Ссылка на форму регистации
    INPUT_NAME = By.XPATH, '//*[text()="Имя"]/following-sibling::input'    # Поле ввода имени
    INPUT_EMAIL = By.XPATH, '//*[text()="Email"]/following-sibling::input'    # Поле ввода почты
    INPUT_PASSWORD = By.XPATH, '//*[text()="Пароль"]/following-sibling::input'    # Поле ввода пароля
    BUTTON_REGISTRATION = By.XPATH, '//*[contains(@class, "button_button_type_primary")]'    # Кнопка "Зарегистрироваться"
    ERROR_REGISTRATION = By.XPATH, '//*[contains(text(), "Некорректный пароль")]'    # Ошибка регистрации
    LOGIN_HEADER = By.XPATH, '//*[contains(text(), "Вход")]'    # Заголовок формы авторизации "Вход"
    REGISTRATION_HEADER = By.XPATH, '//*[contains(text(), "Регистрация")]'

    # Локаторы для тестирования входа в аккаунт
    BUTTON_ENTER_IN_ACCOUNT = By.XPATH, '//*[contains(text(), "Войти в аккаунт")]'    # Кнопка "Войти в аккаунт"
    INPUT_EMAIL = By.XPATH, '//*[text()="Email"]/following-sibling::input'    #Поле ввода логина/почты
    INPUT_PASSWORD = By.XPATH, '//*[text()="Пароль"]/following-sibling::input'    # Поле ввода пароля
    BUTTON_LOGIN = By.XPATH, '// *[contains(text(), "Войти")]'    # Кнопка "Войти"
    BUTTON_PLACE_AN_ORDER = By.XPATH, '//*[contains(text(), "Оформить заказ")]'    # Кнопка "Оформить заказ"
    LINK_LOGIN_FROM_REGISTRATION = By.XPATH, \
        '//*[contains(text(), "Войти")]'    # Ссылка на форму аутентификации с формы регистрации
    LINK_RECOVERY_PASSWORD = By.LINK_TEXT, 'Восстановить пароль'    # Ссылка Восстановления пароля
    LINK_LOGIN_FROM_RECOVERY = By.LINK_TEXT, 'Войти'    # Ссылка "Войти" со страницы "Восстановления пароля"
    BUTTON_SAVE = By.XPATH, '//button[contains(text(), "Сохранить")]'    # Кнопка Сохранить в Личном кабинете

    # Локаторы для тестирования выхода из аккаунта
    BUTTON_LOGOUT = By.XPATH, '//button[contains(text(), "Выход")]'    # Кнопка Выхода их аккаунта

    # Локаторы для тестирования переходов между страницами
    BUTTON_CONSTRUCTOR = By.XPATH, '//p[contains(text(), "Конструктор")]'    # Кнопка перехода в Конструктор
    BLOCK_BUNS = By.XPATH, '//span[contains(text(), "Булки")]'    # Кнопка перехода к разделу "Булки"
    HEADER_BUNS = By.XPATH, '//h2[contains(text(), "Булки")]'    # Текст текущего раздела товаров - "Булки"
    BLOCK_SAUSES = By.XPATH, '//span[contains(text(), "Соусы")]'    # Кнопка перехода к разделу "Соусы"
    HEADER_SAUSES = By.XPATH, '//h2[contains(text(), "Соусы")]'  # Текст текущего раздела товаров - "Соусы"
    BLOCK_TOPPINGS = By.XPATH, '//span[contains(text(), "Начинки")]'    # Кнопка перехода к разделу "Начинки"
    HEADER_TOPPINGS = By.XPATH, '//h2[contains(text(), "Начинки")]'  # Текст текущего раздела товаров - "Начинки"
