import allure
from selene import browser, have, be


class ProgramPage:

    def open(self):
        with allure.step("Открытие страницы Программы"):
            browser.open('/program/all')

    def search(self, value):
        with allure.step("Поиск на странице Программы"):
            browser.element('.search__input').type(value)

    def program_list_should_not_be_empty(self):
        with allure.step("Проверка что вернулся не пустой результат"):
            browser.element('.program__list').should(have.size(0).not_)

    def shold_have_program(self, text):
        with allure.step("Проверка результата поиска на соответствие запросу"):
            browser.element('h4.the-program__title').should(have.text(text))

    def program_list_should_be_empty(self):
        with allure.step("Проверка что вернулся пустой результат"):
            browser.element('.program__list').matching(be.not_.visible)


program_page = ProgramPage()

