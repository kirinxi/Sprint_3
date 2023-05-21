from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

def test_registration_with_valid_data_passed(driver, get_valid_user_data):
    driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.LINK_REGISTRATION).click()

    driver.find_element(*Locators.INPUT_NAME).send_keys(get_valid_user_data.name)
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(get_valid_user_data.email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(get_valid_user_data.password)
    driver.find_element(*Locators.BUTTON_REGISTRATION).click()

    WebDriverWait(driver, 5).until(exp_cond.visibility_of_element_located(Locators.LOGIN_HEADER))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

def test_registration_with_empty_user_name_failed(driver, get_empty_username_data):
    driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.LINK_REGISTRATION).click()

    driver.find_element(*Locators.INPUT_NAME).send_keys(get_empty_username_data.name)
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(get_empty_username_data.email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(get_empty_username_data.password)
    driver.find_element(*Locators.BUTTON_REGISTRATION).click()

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"

def test_registration_with_invalid_password_failed(driver, get_invalid_password_data):
    driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.LINK_REGISTRATION).click()

    driver.find_element(*Locators.INPUT_NAME).send_keys(get_invalid_password_data.name)
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(get_invalid_password_data.email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(get_invalid_password_data.password)
    driver.find_element(*Locators.BUTTON_REGISTRATION).click()

    WebDriverWait(driver, 5).until(exp_cond.presence_of_element_located(Locators.ERROR_REGISTRATION))

    error_message = driver.find_element(*Locators.ERROR_REGISTRATION)

    assert error_message.text == "Некорректный пароль"