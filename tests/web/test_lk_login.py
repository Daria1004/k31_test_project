import allure
import pytest
from allure_commons.types import Severity

import config

from k31_test_project.pages.web.login_page import login_page


@allure.epic('Authentication')
@allure.feature('Login')
@allure.story('Login user with correct data')
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Daria Jakuszewicz")
@allure.label("layer", "web")
@pytest.mark.web
@pytest.mark.login
@pytest.mark.positive
def test_login_success():
    login_page.open()
    login_page.header_should_have_text('Вход в личный кабинет пациента')
    login_page.send_login(config.user_login)
    login_page.send_password(config.user_password)
    login_page.should_have_username(config.user_webname)


@allure.epic('Authentication')
@allure.feature('Login')
@allure.story('Login user with incorrect data')
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Daria Jakuszewicz")
@allure.label("layer", "web")
@pytest.mark.web
@pytest.mark.login
@pytest.mark.negative
def test_login_fail():
    login_page.open()
    login_page.header_should_have_text('Вход в личный кабинет пациента')
    login_page.send_login(config.user_login)
    login_page.send_wrong_password(config.user_wrong_password)
    login_page.should_have_error_text('Введенный код неверен')


@allure.epic('Authentication')
@allure.feature('Logout')
@allure.story('Logout')
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Daria Jakuszewicz")
@allure.label("layer", "web")
@pytest.mark.web
@pytest.mark.login
@pytest.mark.positive
def test_logout(logged_in):
    logged_in.logout()
    logged_in.header_should_have_text('Вход в личный кабинет пациента')
