import allure
from selene import browser, have, be


class LoginPage:

    @staticmethod
    def open():
        with allure.step('Открытие страницы с аутентификацией в Личный кабинет пациента'):
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
        with allure.step('Открытие страницы Личный кабинет'):
            browser.element('.menu__user-name').should(have.text(value))

    @staticmethod
    def should_have_error_text(value):
        with allure.step('Запрет входа при неправильном пароле'):
            browser.element('.error.help-block').should(have.text(value))

    @staticmethod
    def logout():
        with allure.step('Выход из Личного кабинета'):
            browser.element('.menu__user-logout').click()

    @staticmethod
    def header_should_have_text(text):
        with allure.step('Открытие страницы с аутентификацией в Личный кабинет пациента'):
            browser.element('.title').should(have.text(text))

    @staticmethod
    def open_profile():
        with allure.step('Открытие пункта меню Мой профиль'):
            browser.wait_until(browser.element('a[href="/profile/details"]').should(be.visible))
            browser.element('a[href="/profile/details"]').click()

    @staticmethod
    def profile_should_have_phone(value):
        with allure.step('Проверка номера телефона в Профиле'):
            browser.element('.profile-personal__item:nth-child(3)').element('.profile-personal__info').should(have.text(f'7{value}'))


login_page = LoginPage()
