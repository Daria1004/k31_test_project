import allure
from selene import browser, have
from k31_test_project.pages.web.login_page import LoginPage


class LoginApi:

    def open(self):
        with allure.step("Открытие страницы Личный кабинет"):
            browser.open('/auth/phone')

    def send_login(self, value):
        browser.element('.password-input>input').type(value)
        browser.element('button.custom-btn').should(have.text("ПРОДОЛЖИТЬ")).click()

    def send_password(self, value):
        browser.element('.password-input>input').type(value)
        browser.element('button.custom-btn').should(have.text("ВОЙТИ")).click()

    def should_have_username(self, value):
        browser.element('.menu__user-name').should(have.text(value))

    def should_have_error_text(self, value):
        browser.element('.error.help-block').should(have.text(value))

login_page = LoginPage()