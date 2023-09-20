import pytest
import database
from pages.main_page import MainPage
import allure

link = "https://alpha.it-roast.com/"


@allure.feature('Home page')
@pytest.fixture(scope="function")
def main_page(browser):
    page = MainPage(browser, link)
    with allure.step('Open Home page'):
        page.open()
    return page


@allure.story('Trainlab logo')
@allure.title('Testing Trainlab logo')
@pytest.mark.logo
def test_logo_is_displayed(main_page):
    with allure.step('Check logo is displayed'):
        assert main_page.logo().is_displayed()


@allure.story('About us button')
@allure.title('Testing about us button')
@pytest.mark.about_us
def test_button_about_us_is_displayed(main_page):
    with allure.step('Check the button about us is displayed'):
        assert main_page.button_about_us().is_displayed()


@allure.story('About us button')
@allure.title('Testing about us button')
@pytest.mark.about_us
def test_button_about_us_text_is_ok(main_page):
    with allure.step('Check that the text of the About Us button is displayed'):
        assert main_page.button_about_us_text() == 'О нас', "Текст не совпадает"


@allure.story('Tasks button')
@allure.title('Testing tasks button')
@pytest.mark.tasks
def test_tasks_button_is_displayed(main_page):
    with allure.step('Check that tasks button is displayed'):
        assert main_page.tasks_button().is_displayed()


@allure.story('Tasks button')
@allure.title('Testing tasks button')
@pytest.mark.tasks
def test_tasks_button_text_is_ok(main_page):
    with allure.step('Check that tasks button text is displayed'):
        assert main_page.tasks_button_text() == 'Задания', "Текст не совпадает"


@allure.story('Sign in button')
@allure.title('Testing sign in button')
@pytest.mark.sing_in
def test_sing_in_button_is_displayed(main_page):
    with allure.step('Check that sign in button is displayed'):
        assert main_page.sing_in_button().is_displayed()


@allure.story('Sign in button')
@allure.title('Testing sign in button')
@pytest.mark.sing_in
def test_sing_in_button_text_is_ok(main_page):
    with allure.step('Check that sign in button text is displayed'):
        assert main_page.sing_in_button_text() == 'Войти', "Текст не совпадает"


@allure.story('Start the journey button')
@allure.title('Testing start the journey button')
@pytest.mark.start_way
def test_start_way_button_is_displayed(main_page):
    with allure.step('Check that start the journey button is displayed'):
        assert main_page.start_way_button().is_displayed()


@allure.story('Start the journey button')
@allure.title('Testing start the journey button')
@pytest.mark.start_way
def test_test_start_way_button_text_is_ok(main_page):
    with allure.step('Check that start the journey button text is displayed'):
        assert main_page.start_way_button_text() == 'Начать путь', "Текст не совпадает"


@allure.story('Ask us button')
@allure.title('Testing Ask us button')
@pytest.mark.ask_us
def test_ask_us_button_is_displayed(main_page):
    with allure.step('Check that Ask us button is displayed'):
        assert main_page.ask_us_button().is_displayed()


@allure.story('Ask us button')
@allure.title('Testing Ask us button')
@pytest.mark.ask_us
def test_test_ask_us_button_text_is_ok(main_page):
    with allure.step('Check that Ask us button text is displayed'):
        assert main_page.ask_us_button_text() == 'Задай нам вопрос', "Текст не совпадает"


@allure.story('About us button')
@allure.title('Testing about us button tooltip')
@pytest.mark.about_us
@pytest.mark.tooltips
def tooltip_about_us(main_page):
    with allure.step('Check that tooltip button about us is displayed'):
        assert main_page.tooltip_about_us() == "здесь будет переход на страницу с информацией о приложении"


@allure.story('Tasks button')
@allure.title('Testing tasks button tooltip')
@pytest.mark.tooltips
def tooltip_tasks(main_page):
    with allure.step('Check that tasks tooltip is displayed'):
        assert main_page.tooltip_tasks_button() == "здесь будет переход на страницу с примерами заданий"


@allure.story('Sign in button')
@allure.title('Testing sign in button tooltip')
@pytest.mark.tooltips
def tooltip_sing_in(main_page):
    assert main_page.tooltip_sing_in() == "здесь будет переход на страницу регистрации"


@allure.story('Ask us button')
@allure.title('Testing Ask us button tooltip')
@pytest.mark.tooltips
def tooltip_ask_us(main_page):
    assert main_page.tooltip_ask_us() == "здесь будет возможно инициировать получение обратной связи"


@allure.story('Database connection')
@allure.title('Testing Database connection')
def test_db(connect_db):
    with allure.step('Проверка выдачи текста из БД по номером 1.9'):
        front_id = 1.9
        connect_db.execute(f"select front_id, text  from frontend_data where front_id = '{front_id}';")
        all_users = connect_db.fetchall()
        print(all_users)

@allure.story('Success banner')
@allure.title('Testing success banner')
def test_success_banner_text_takes_from_bd(browser):  #надо менять структуру
    with allure.step('Take text from database by front id'):
        text_from_database = database.take_text_from_database_by_front_id(1.1)
    with allure.step('Change text in database by front id'):
        database.change_text_in_database_by_front_id(1.1, 'Текст изменен')
    with allure.step('Take text from element on website'):
        new_text_from_website = main_page.success_banner_text()
    with allure.step('Return text to database by front id'):
        database.change_text_in_database_by_front_id(1.1, f"{text_from_database}")
    with allure.step('Check that text for website element takes from database'):
        assert new_text_from_website == 'Текст изменен'

@allure.story('SQL banner')
@allure.title('Testing SQL banner')
def test_sql_banner_is_displayed(browser):
    with allure.step('Check that SQL banner is displayed'):
        assert main_page.sql_banner_is_displayed()


@allure.story('Python banner')
@allure.title('Testing Python banner')
def test_python_banner_is_displayed(browser):
    with allure.step('Check that Python banner is displayed'):
        assert main_page.python_banner_is_displayed()


@allure.story('JavaScript banner')
@allure.title('Testing JavaScript banner')
def test_java_script_banner_is_displayed(browser):
    with allure.step('Check that JavaScript banner is displayed'):
        assert main_page.java_script_banner_is_displayed()