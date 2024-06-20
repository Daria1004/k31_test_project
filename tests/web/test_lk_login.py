import config

from k31_test_project.pages.web.login_page import login_page


def test_login_success():
    login_page.open()
    login_page.header_should_have_text('Вход в личный кабинет пациента')
    login_page.send_login(config.user_login)
    login_page.send_password(config.user_password)
    login_page.should_have_username(config.user_webname)

def test_login_fail():
    login_page.open()
    login_page.header_should_have_text('Вход в личный кабинет пациента')
    login_page.send_login(config.user_login)
    login_page.send_wrong_password(config.user_wrong_password)
    login_page.should_have_error_text('Введенный код неверен')

def test_logout(logged_in):
    logged_in.logout()
    logged_in.header_should_have_text('Вход в личный кабинет пациента')
