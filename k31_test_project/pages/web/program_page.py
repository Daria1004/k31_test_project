import allure
from selene import browser, have, be


class ProgramPage:

    @staticmethod
    def open():
        with allure.step('Открытие страницы Программы'):
            browser.open('/program/all')

    @staticmethod
    def search(value):
        with allure.step('Поиск на странице Программы'):
            browser.element('.search__input').type(value)

    @staticmethod
    def program_list_should_not_be_empty():
        with allure.step('Проверка что вернулся не пустой результат'):
            browser.element('.program__list').should(have.size(0).not_)

    @staticmethod
    def should_have_program(text):
        with allure.step('Проверка результата поиска на соответствие запросу'):
            browser.element('.the-program__title').should(have.text(text))

    @staticmethod
    def program_list_should_be_empty():
        with allure.step('Проверка что вернулся пустой результат'):
            browser.element('.program__list').matching(be.not_.visible)


program_page = ProgramPage()
