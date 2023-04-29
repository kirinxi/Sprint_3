from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

def test_transition_to_personal_account_passed(driver, get_credentials):
    driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(exp_cond.visibility_of_element_located(Locators.LOGIN_HEADER))

    driver.find_element(*Locators.INPUT_EMAIL).send_keys(get_credentials.email)
    driver.find_element(*Locators.INPUT_PASSWORD).send_keys(get_credentials.password)
    driver.find_element(*Locators.BUTTON_LOGIN).click()

    WebDriverWait(driver, 5).until(exp_cond.element_to_be_clickable(Locators.BUTTON_PLACE_AN_ORDER))

    driver.find_element(*Locators.BUTTON_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, 5).until(exp_cond.element_to_be_clickable(Locators.BUTTON_SAVE))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"