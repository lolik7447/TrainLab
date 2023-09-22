from .base_page import BasePage
from locators import MainPageLocators
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def open(self):
        self.browser.get(self.url)

    def logo(self):
        return self.find_element(*MainPageLocators.train_lab_logo)

    def button_about_us(self):
        return self.find_element(*MainPageLocators.about_us)

    def button_about_us_text(self):
        return self.find_element(*MainPageLocators.about_us).text

    def tasks_button(self):
        return self.find_element(*MainPageLocators.tasks_button)

    def tasks_button_text(self):
        return self.find_element(*MainPageLocators.tasks_button).text

    def sing_in_button(self):
        return self.find_element(*MainPageLocators.sing_in_button)

    def sing_in_button_text(self):
        return self.find_element(*MainPageLocators.sing_in_button).text

    def start_way_button(self):
        return self.find_element(*MainPageLocators.start_way_button)

    def start_way_button_text(self):
        return self.find_element(*MainPageLocators.start_way_button).text

    def ask_us_button(self):
        return self.find_element(*MainPageLocators.ask_us_button)

    def ask_us_button_text(self):
        return self.find_element(*MainPageLocators.ask_us_button).text

    def ask_us_button(self):
        return self.find_element(*MainPageLocators.ask_us_button)

    def ask_us_button_text(self):
        return self.find_element(*MainPageLocators.ask_us_button).text

    def tooltip_about_us(self):
        actions = ActionChains(self)
        actions.move_to_element(*MainPageLocators.tooltip_about_us).perform()
        return self.find_element(*MainPageLocators.tooltip_about_us)

    def tooltip_tasks_button(self):
        actions = ActionChains(self)
        actions.move_to_element(*MainPageLocators.tooltip_tasks_button).perform()
        return self.find_element(*MainPageLocators.tooltip_tasks_button)
    def tooltip_sing_in(self):
        actions = ActionChains(self)
        actions.move_to_element(*MainPageLocators.tooltip_sing_in).perform()
        return self.find_element(*MainPageLocators.tooltip_sing_in)

    def tooltip_ask_us(self):
        actions = ActionChains(self)
        actions.move_to_element(*MainPageLocators.tooltip_ask_us).perform()
        return self.find_element(*MainPageLocators.tooltip_ask_us)

    def success_banner_text(self):
        self.wait_element(MainPageLocators.success_banner_bar)
        return self.find_element(MainPageLocators.success_banner_bar).text



