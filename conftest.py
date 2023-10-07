import pytest
import allure
import psycopg2
from sshtunnel import SSHTunnelForwarder
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_chrome
from selenium.webdriver.firefox.options import Options as Options_ff
import os

host = os.environ['HOST']
user = os.environ['USER']
password = os.environ['PASSWORD']
database = os.environ['DATABASE']
bd_ip = os.environ['BD_IP']
ssh_port = int(os.environ['SSH_PORT'])
ssh_username = os.environ['SSH_USERNAME']
ssh_private_key = os.environ['SSH_PRIVATE_KEY']
remote_bind_address = (os.environ['HOST'], int(os.environ['PORT']))
port = int(os.environ['PORT'])




@pytest.fixture(scope='function')
def browser(browser_options, host_options):
    if browser_options == 'ff' and host_options == 'server':
        with allure.step(f'Run Firefox and {host_options}'):
            options = Options_ff()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
            driver_browser = webdriver.Firefox(options=options)

    elif browser_options == 'ff':
        with allure.step('Run Firefox'):
            options = Options_ff()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
            driver_browser = webdriver.Firefox(options=options)

    elif host_options == 'server':
        with allure.step(f'Run Chrome with {host_options}'):
            options = Options_chrome()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
            driver_browser = webdriver.Chrome(options=options)

    else:
        with allure.step('Run Chrome'):
            options = Options_chrome()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--window-size=1920x1080")
            driver_browser = webdriver.Chrome(options=options)
    driver_browser.implicitly_wait(10)
    yield driver_browser
    driver_browser.quit()


@pytest.fixture(scope='function')
def connect_db(host_options):
    if host_options == 'server':
        with allure.step(f'Run a database connection from {host_options}'):
            con = psycopg2.connect(
                host,
                port,
                user,
                password,
                database
            )
            curs = con.cursor()
            yield curs
            curs.close()

    else:
        with allure.step(f'Run a database connection from {host_options}'):
            with SSHTunnelForwarder(
                    (bd_ip, ssh_port),
                    ssh_username=ssh_username,
                    ssh_pkey=ssh_private_key,
                    remote_bind_address=remote_bind_address
            ) as server:
                server.start()
                con = psycopg2.connect(
                    host='localhost',
                    port=server.local_bind_port,
                    user=user,
                    password=password,
                    dbname=database
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
        help='Укажите значение браузера, по умолчанию Chrome'
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
