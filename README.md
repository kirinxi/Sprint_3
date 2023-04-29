# Sprint_3

## Проект автотестов сервиса Stellar Burgers

1. Фреймворк - Selenium
2. Браузер - Chrome
3. Запуск всех тестов: pytest -v tests 

## Сценарии, покрытые тавтотестами:
* test_registration_page.py - Регистрация в аккаунт
* test_login_page.py - Переход на форму входа в аккаунт
* test_account_profile.py - Аутентификация в личный кабинет
* test_go_to_constructor.py - Переход из личного кабинета в конструктор
* test_logout.py - Выход из аккаунта
* test_constructor.py - Раздел «Конструктор»

## Test Cases:
### Тесты на регистрацию

1. test_registration_with_valid_data_passed - проверяет успешную регистрацию;
2. test_registration_with_empty_user_name_failed - проверяет регистрацию с пустым полем "Имя";
3. test_registration_with_invalid_password_failed - проверяет ошибку для некорректного пароля.

### Тесты на переходы в Личный кабинет

1. test_login_from_enter_account_button_passed - проверяет вход по кнопке «Войти в аккаунт» на главной;
2. test_login_from_personal_account_passed - проверяет вход через кнопку «Личный кабинет»;
3. test_login_button_from_registration_form_passed - проверяет вход через кнопку в форме регистрации;
4. test_login_from_recovery_link_passed - проверяет вход через кнопку в форме восстановления пароля.

### Тест перехода в личный кабинет

1. test_transition_to_personal_account_passed - проверяет вход в «Личный кабинет».

### Тесты перехода из личного кабинета в конструктор

1. test_transfer_to_constructor проверяет переход по клику на «Конструктор»;
2. test_transfer_to_constructor_by_logo проверяет переход по клику на логотип Stellar Burgers.

### Тест выхода из аккаунта

1. test_transition_to_personal_account_passed - проверяет выход по кнопке «Выйти» в личном кабинете.

### Тесты перехода к разделам конструктора

1. test_buns_block_transition_passed - проверяет переход к разделу «Начинки»;
2. test_sauses_block_transition_passed - проверяет переход к разделу «Соусы»;
3. test_toppings_block_transition_passed - проверяет переход к разделу «Булки».

# Спасибо за внимание! :)