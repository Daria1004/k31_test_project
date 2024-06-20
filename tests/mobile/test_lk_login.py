import config
from k31_test_project.pages.mobile.login_page import login_page


def test_login_success():
    login_page.skip_health()
    login_page.open_login()
    login_page.header_should_have_text('Вход в личный кабинет пациента')
    login_page.send_login(config.user_login)
    login_page.send_password(config.user_password)
    login_page.skip_allow()
    login_page.send_pin()
    login_page.skip_health()
    login_page.open_menu()
    login_page.should_have_username(config.user_mobilename)

def test_login_fail():
    login_page.skip_health()
    login_page.open_login()
    login_page.header_should_have_text('Вход в личный кабинет пациента')
    login_page.send_login(config.user_login)
    login_page.send_password(config.user_wrong_password)
    login_page.should_have_login_error()

def test_complex_programs():
    login_page.skip_health()
    login_page.open_menu()
    login_page.should_have_title("Меню")
    login_page.open_program()
    login_page.search_program()
    login_page.check_results()
