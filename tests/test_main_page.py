import pytest
from pages.main_page import MainPage


link = "https://alpha.it-roast.com/"


@pytest.fixture(scope="function")
def main_page(browser):
    page = MainPage(browser, link)
    page.open()
    return page


@pytest.mark.logo
def test_logo_is_displayed(main_page):
    assert main_page.logo().is_displayed()


@pytest.mark.about_us
def test_button_about_us_is_displayed(main_page):
    assert main_page.button_about_us().is_displayed()

@pytest.mark.about_us
def test_button_about_us_text_is_ok(main_page):
    assert main_page.button_about_us_text() == 'О нас', "Текст не совпадает"


@pytest.mark.tasks
def test_tasks_button_is_displayed(main_page):
    assert main_page.tasks_button().is_displayed()

@pytest.mark.tasks
def test_tasks_button_text_is_ok(main_page):
    assert main_page.tasks_button_text() == 'Задания', "Текст не совпадает"


@pytest.mark.sing_in
def test_sing_in_button_is_displayed(main_page):
    assert main_page.sing_in_button().is_displayed()

@pytest.mark.sing_in
def test_sing_in_button_text_is_ok(main_page):
    assert main_page.sing_in_button_text() == 'Войти', "Текст не совпадает"


@pytest.mark.start_way
def test_start_way_button_is_displayed(main_page):
    assert main_page.start_way_button().is_displayed()

@pytest.mark.start_way
def test_test_start_way_button_text_is_ok(main_page):
    assert main_page.start_way_button_text() == 'Начать путь', "Текст не совпадает"


@pytest.mark.ask_us
def test_ask_us_button_is_displayed(main_page):
    assert main_page.ask_us_button().is_displayed()

@pytest.mark.ask_us
def test_test_ask_us_button_text_is_ok(main_page):
    assert main_page.ask_us_button_text() == 'Задай нам вопрос', "Текст не совпадает"


@pytest.mark.tooltips
def tooltip_about_us(main_page):
    assert main_page.tooltip_about_us() == "здесь будет переход на страницу с информацией о приложении"

@pytest.mark.tooltips
def tooltip_about_us(main_page):
    assert main_page.tooltip_tasks_button() == "здесь будет переход на страницу с примерами заданий"

@pytest.mark.tooltips
def tooltip_sing_in(main_page):
    assert main_page.tooltip_sing_in() == "здесь будет переход на страницу регистрации"

@pytest.mark.tooltips
def tooltip_ask_us(main_page):
    assert main_page.tooltip_ask_us() == "здесь будет возможно инициировать получение обратной связи"

def test_db(connect_db):
    front_id = 1.9
    connect_db.execute(f"select front_id, text  from frontend_data where front_id = '{front_id}';")
    all_users = connect_db.fetchall()
    print(all_users)

