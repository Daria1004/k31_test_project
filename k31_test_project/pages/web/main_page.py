import allure
from selene import browser, have


class MainPage:

    def open(self):
        with allure.step("Открытие страницы Личный кабинет без аутентификации"):
            browser.open('/')

    def header_should_have_text(self, text):
        with allure.step("Наличие надписи об ограничении"):
            browser.element('.modal-header>.the-text').should(have.text(text))


main_page = MainPage()
