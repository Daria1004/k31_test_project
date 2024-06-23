import allure
from selene import browser, have


class MainPage:

    @staticmethod
    def open():
        with allure.step('Открытие страницы Личный кабинет без аутентификации'):
            browser.open('/')

    @staticmethod
    def header_should_have_text(text):
        with allure.step('Наличие надписи об ограничении'):
            browser.element('.the-text').should(have.text(text))


main_page = MainPage()
