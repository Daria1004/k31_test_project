import allure
from selene import browser, have, be


class LoginPage:

    def open(self):
        with allure.step("Откытие страницы с аутентификацией в Личный кабинет пациента"):
            browser.open('/auth/phone')

    def send_login(self, value):
        with allure.step("Ввод логина"):
            browser.element('.password-input>input').type(value)
            browser.element('button.custom-btn').should(have.text("ПРОДОЛЖИТЬ")).click()

    def send_password(self, value):
        with allure.step("Ввод пароля"):
            browser.element('.password-input>input').type(value)
            browser.element('button.custom-btn').should(have.text("ВОЙТИ")).click()

    def send_wrong_password(self, value):
        with allure.step("Ввод пароля"):
            browser.element('.password-input>input').type(value)
            browser.element('button.custom-btn').should(have.text("ВОЙТИ")).click()

    def should_have_username(self, value):
        with allure.step("Открытие страницы Личный кабинет"):
            browser.element('.menu__user-name').should(have.text(value))

    def should_have_error_text(self, value):
        with allure.step("Запрет входа при неправильном пароле"):
            browser.element('.error.help-block').should(have.text(value))

    def logout(self):
        with allure.step("Выход из Личного кабинета"):
            browser.element('.menu__user-logout').click()

    def header_should_have_text(self, text):
        with allure.step("Откытие страницы с аутентификацией в Личный кабинет пациента"):
            browser.element('div.title').should(have.text(text))

    def open_profile(self):
        with allure.step("Открытие пункта меню Мой профиль"):
            browser.wait_until(browser.element('a[href="/profile/details"]').should(be.visible))
            browser.element('a[href="/profile/details"]').click()

    def profile_should_have_phone(self, value):
        with allure.step("Проверка номера телефона в Профиле"):
            browser.element('.profile-personal__item:nth-child(3)').element('.profile-personal__info').should(have.text(f'7{value}'))


login_page = LoginPage()
