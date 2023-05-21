import pytest
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Registration:
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1200,1500")
    browser = webdriver.Chrome(options=options)
    browser.get("https://stellarburgers.nomoreparties.site/")
    yield browser
    browser.quit()

@pytest.fixture
def get_valid_user_data():
    random_numbers = random.randint(100, 999)
    return Registration(f"Irina_Gorbacheva_9{random_numbers}@gmail.com", "123456", "Ирина")

@pytest.fixture
def get_invalid_password_data():
    return Registration("meowmeow@mail", "12345", "Irina")

@pytest.fixture
def get_empty_username_data():
    random_numbers = random.randint(100, 999)
    return Registration(f"Irina_Gorbacheva_9{random_numbers}@gmail.com", "123456", "   ")

class Credentials:
	def __init__(self, email, password):
		self.email = email
		self.password = password
@pytest.fixture
def get_credentials():
	return Credentials("irinagorbacheva9_999@yandex.ru", "123456")

