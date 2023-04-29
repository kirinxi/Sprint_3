from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


def test_login_from_enter_account_button_passed(driver, get_credentials):
    driver.find_element(*Locators.BUTTON_ENTER_IN_ACCOUNT).click()

    driver.find_element(*Locators.INPUT_EMAIL).send_keys(get_credentials.email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(get_credentials.password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 5).until(exp_cond.element_to_be_clickable(Locators.BUTTON_PLACE_AN_ORDER))

    check = driver.find_element(*Locators.BUTTON_PLACE_AN_ORDER).text

    assert check == "Оформить заказ"

def test_login_from_personal_account_passed(driver, get_credentials):
    driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(get_credentials.email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(get_credentials.password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 5).until(exp_cond.element_to_be_clickable(Locators.BUTTON_PLACE_AN_ORDER))

    check = driver.find_element(*Locators.BUTTON_PLACE_AN_ORDER).text

    assert check == "Оформить заказ"

def test_login_button_from_registration_form_passed(driver, get_credentials):
    driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.LINK_REGISTRATION).click()
    driver.find_element(*Locators.LINK_LOGIN_FROM_REGISTRATION).click()
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(get_credentials.email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(get_credentials.password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(exp_cond.element_to_be_clickable(Locators.BUTTON_PLACE_AN_ORDER))

    check = driver.find_element(*Locators.BUTTON_PLACE_AN_ORDER).text

    assert check == "Оформить заказ"

def test_login_from_recovery_link_passed(driver, get_credentials):
    driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.LINK_RECOVERY_PASSWORD).click()
    driver.find_element(*Locators.LINK_LOGIN_FROM_RECOVERY).click()
    driver.find_element(*Locators.INPUT_EMAIL).send_keys(get_credentials.email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(get_credentials.password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()
    WebDriverWait(driver, 5).until(exp_cond.element_to_be_clickable(Locators.BUTTON_PLACE_AN_ORDER))

    check = driver.find_element(*Locators.BUTTON_PLACE_AN_ORDER).text

    assert check == "Оформить заказ"
