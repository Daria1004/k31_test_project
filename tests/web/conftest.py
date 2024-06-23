import pytest
from selene import browser
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import config
from k31_test_project.pages.web.login_page import login_page
from k31_test_project.utils import utils_allure

DEFAULT_BROWSER_VERSION = '100.0'


def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    login = config.selenoid_login
    password = config.selenoid_password

    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@{config.selenoid_url}/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = config.base_url
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    utils_allure.attach_screenshot()
    utils_allure.attach_logs(browser)
    utils_allure.attach_html(browser)
    utils_allure.attach_video(browser)

    browser.quit()


@pytest.fixture(scope='function')
def logged_in():
    login_page.open()
    login_page.send_login(config.user_login)
    login_page.send_password(config.user_password)

    yield login_page
