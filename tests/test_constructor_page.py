from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators

def test_buns_block_transition_passed(driver, get_credentials):
    driver.find_element(*Locators.BLOCK_SAUSES).click()
    WebDriverWait(driver, 5).until(exp_cond.visibility_of_element_located(Locators.HEADER_BUNS))
    driver.find_element(*Locators.BLOCK_BUNS).click()
    WebDriverWait(driver, 5).until(exp_cond.element_to_be_clickable(Locators.HEADER_BUNS))

    assert driver.find_element(*Locators.HEADER_BUNS).text == 'Булки'

def test_sauses_block_transition_passed(driver, get_credentials):
    driver.find_element(*Locators.BLOCK_SAUSES).click()
    WebDriverWait(driver, 10).until(exp_cond.visibility_of_element_located(Locators.HEADER_SAUSES))

    assert driver.find_element(*Locators.HEADER_SAUSES).text == 'Соусы'

def test_toppings_block_transition_passed(driver, get_credentials):
    driver.find_element(*Locators.BLOCK_TOPPINGS).click()
    WebDriverWait(driver, 5).until(exp_cond.visibility_of_element_located(Locators.HEADER_TOPPINGS))

    assert driver.find_element(*Locators.HEADER_TOPPINGS).text == 'Начинки'

