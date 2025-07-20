from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import driver



class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    # Locators
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def load(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        try:
            # self.driver.find_element(*self.username_field).send_keys(username)
            # self.driver.find_element(*self.password_field).send_keys(password)
            # self.driver.find_element(*self.login_button).click()\
            self.wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(username)
            self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(password)
            self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

        except Exception as e:
            print(f"Exceptions: {e}")

    def is_login_fail(self):
        try:
            message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))).text
            return "Epic sadface" in message
        except Exception:
            return False

    def is_login_successful(self):
        return "inventory.html" in self.driver.current_url