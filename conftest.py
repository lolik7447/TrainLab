import pytest
import allure
import psycopg2
from sshtunnel import SSHTunnelForwarder
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_chrome
from selenium.webdriver.firefox.options import Options as Options_ff
import database_connection


@pytest.fixture(scope='function')
def browser(browser_options, host_options):
    if browser_options == 'ff' and host_options == 'server':
        with allure.step(f'Rune Firefox and {host_options}'):
            options = Options_ff()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
            driver_browser = webdriver.Firefox(options=options)

    elif browser_options == 'ff':
        with allure.step('Rune Firefox'):
            driver_browser = webdriver.Firefox()
            driver_browser.maximize_window()

    elif host_options == 'server':
        with allure.step(f'Rune Chrome with {host_options}'):
            options = Options_chrome()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
            driver_browser = webdriver.Chrome(options=options)

    else:
        with allure.step('Rune Chrome'):
            driver_browser = webdriver.Chrome()
            driver_browser.maximize_window()
    driver_browser.implicitly_wait(10)
    yield driver_browser
    driver_browser.quit()


@pytest.fixture(scope='function')
def connect_db(host_options):
    if host_options == 'server':
        with allure.step(f'Run a database connection from {host_options}'):
            con = psycopg2.connect(
                host=database_connection.host,
                port=database_connection.port,
                user=database_connection.username,
                password=database_connection.password,
                database=database_connection.database
            )
            curs = con.cursor()
            yield curs
            curs.close()

    else:
        with allure.step(f'Run a database connection from {host_options}'):
            with SSHTunnelForwarder(
                    (database_connection.bd_ip, database_connection.ssh_port),
                    ssh_username=database_connection.ssh_username,
                    ssh_private_key=database_connection.ssh_private_key,
                    remote_bind_address=(
                            database_connection.host,
                            database_connection.port)) as server:
                server.start()
                con = psycopg2.connect(
                    host='localhost',
                    port=server.local_bind_port,
                    user=database_connection.username,
                    password=database_connection.password,
                    database=database_connection.database
                )
                curs = con.cursor()
                yield curs
                curs.close()
                server.close()


def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        action='store',
        default='chrome',
        help='Укажите значение браузера, поумолчанию Chrome'
    )
    parser.addoption(
        '--host',
        action='store',
        default='localhost',
        help='Укажите вариант запуска тестов с хоста, по умолчанию localhost.'
    )


@pytest.fixture(scope='session')
def browser_options(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='session')
def host_options(request):
    return request.config.getoption('--host')
