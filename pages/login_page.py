from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait = WebDriverWait(driver, 10)
        # self.base_page = BasePage(driver)


    # ----- Locators
    url = "https://www.saucedemo.com/"
    username_field = (By.ID, "user-name")
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")



    def login(self, username, password):
        try:
            self.load_url(self.url)
            self.get_element(self.username_field).send_keys(username)
            self.get_element(self.password_field).send_keys(password)
            self.get_element(self.login_button).click()

        except Exception as e:
            print(f"Exceptions: {e}")

    def is_login_fail(self):
        try:
            message = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))).text
            return "Epic sadface" in message
        except Exception as e:
            print(f"Exceptions: {e}")
            return False

    def is_login_successful(self):
        return "inventory.html" in self.get_current_url()