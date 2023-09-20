from selenium.webdriver.common.by import By


class MainPageLocators:
    train_lab_logo = (By.CSS_SELECTOR, 'img[alt="Logo"]')
    about_us = [By.XPATH,"//button[contains(text(), 'О нас')]"]  #button[data-original-title="О нас"]
    tasks_button = [By.XPATH, "//button[contains(text(), 'Задания')]"]  #button[data-original-title="Задания"]
    sing_in_button = [By.XPATH, "//button[contains(text(), 'Войти')]"]
    start_way_button = [By.XPATH, "//button[contains(text(), 'Начать путь')]"]
    ask_us_button = [By.XPATH, "//button[contains(text(), 'Задай нам вопрос')]"]
    tooltip_about_us = (By.CSS_SELECTOR, 'a[data-tooltip="здесь будет переход на страницу с информацией о приложении"]')
    #button[data-original-title="О нас"] + div.tooltip > div.tooltip-inner
    tooltip_tasks_button = (By.CSS_SELECTOR, '#basic-navbar-nav > div.nav.me-auto.ms-auto.navbar-nav > a.Header_tooltip__LS513.active')
    #button[data-original-title="Задания"] + div.tooltip > div.tooltip-inner
    tooltip_sing_in = (By.CSS_SELECTOR, "#root > div > div > header div.Banner_col_banner_btn__HaLa-.col-md-4 > a")
    #button[data-original-title="Войти"] + div.tooltip > div.tooltip-inner
    tooltip_ask_us = (By.CSS_SELECTOR, "#root div:nth-child(3) > div > div > div:nth-child(5) > a")
    #button[data-original-title="Задай нам вопрос"] + div.tooltip > div.tooltip-inner

class AuthPageLocators:
    email_input = (By.NAME, 'Registration_input__fHjpg')
