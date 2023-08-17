from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def find_element(self, by_name, by_val):
        return self.browser.find_element(by_name, by_val)

    def find_elements(self, by_name, by_val):
        return self.browser.find_elements(by_name, by_val)

    def wait_element(self, locator):
        return WebDriverWait(self, 10).until(EC.visibility_of_element_located(locator))

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
