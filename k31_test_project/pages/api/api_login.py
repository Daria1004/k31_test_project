import allure
from selene import browser, have
from k31_test_project.pages.web.login_page import LoginPage


class LoginApi:

    @staticmethod
    def open():
        with allure.step('Открытие страницы Личный кабинет'):
            browser.open('/auth/phone')

    @staticmethod
    def send_login(value):
        with allure.step('Ввод логина'):
            browser.element('.password-input>input').type(value)
            browser.element('.custom-btn').should(have.text("ПРОДОЛЖИТЬ")).click()

    @staticmethod
    def send_password(value):
        with allure.step('Ввод пароля'):
            browser.element('.password-input>input').type(value)
            browser.element('.custom-btn').should(have.text("ВОЙТИ")).click()

    @staticmethod
    def should_have_username(value):
        with allure.step('Проверка имени пользователя'):
            browser.element('.menu__user-name').should(have.text(value))

    @staticmethod
    def should_have_error_text(value):
        with allure.step('Проверка сообщения об ошибке'):
            browser.element('.error.help-block').should(have.text(value))


login_page = LoginPage()
