
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def load_url(self, url):
        self.driver.get(url)

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def get_css_value(self, locator, value):
        return self.driver.find_element(*locator).value_of_css_property(value)

    def clear_text(self, locator):
        self.get_element(locator).clear()

    def click_on_button(self, locator):
        self.get_element(locator).click()

    def get_text(self, locator):
        return self.get_element(locator).text