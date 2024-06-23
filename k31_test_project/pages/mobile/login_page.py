import allure
import config
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class LoginPage:

    @staticmethod
    def skip_health():
        with allure.step('Пропуск окна настроек разрешений здоровья'):
            if config.context == 'bstack':
                browser.element((AppiumBy.ID, 'com.android.healthconnect.controller:id/go_back_button')).click()
            else:
                browser.element((AppiumBy.ID, 'com.android.healthconnect.controller:id/cancel')).click()

    @staticmethod
    def open_login():
        with allure.step('Переход на экран входа'):
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="ВХОД/РЕГИСТРАЦИЯ"]')).click()

    @staticmethod
    def send_login(value):
        with allure.step('Установка логина'):
            browser.element((AppiumBy.XPATH, '//android.widget.EditText')).type(value)
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="ПРОДОЛЖИТЬ"]')).click()

    @staticmethod
    def send_password(value):
        with allure.step('Установка пароля'):
            browser.element((AppiumBy.XPATH, '//android.widget.EditText')).type(value)
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="ВОЙТИ"]')).click()

    @staticmethod
    def skip_allow():
        with allure.step('Пропуск окна настроек уведомлений'):
            browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')).click()

    @staticmethod
    def send_pin():
        with allure.step('Установка пинкода'):
            for i in range(12):
                browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="1"]')).click()

    @staticmethod
    def should_have_username(value):
        with allure.step('Проверка имени пользователя после логина'):
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Иванов Петр"]')).should(have.text(value))

    @staticmethod
    def should_have_login_error():
        with allure.step('Проверка наличия ошибки'):
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="ВОЙТИ"]')).should(be.visible)

    @staticmethod
    def should_have_error_text(value):
        with allure.step('Проверка наличия ошибки'):
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Неверный код"]')).should(have.text(value))

    @staticmethod
    def logout():
        browser.element('.menu__user-logout').click()

    @staticmethod
    def header_should_have_text(text):
        with allure.step('Поиск проверочной строки'):
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Вход в личный кабинет пациента"]')).should(
                have.text(text))

    @staticmethod
    def open_menu():
        with allure.step('Открытие главного меню'):
            if config.context == 'bstack':
                browser.element((AppiumBy.XPATH, '//android.widget.Button[@text=""]')).click()
            else:
                browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="точки меню"]')).click()

    @staticmethod
    def should_have_title(value):
        with allure.step('Поиск проверочной строки'):
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Меню"]')).should(have.text(value))

    @staticmethod
    def open_program():
        with allure.step('Открытие раздела программ'):
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Комплексные программы"]')).should(be.visible)
            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Комплексные программы"]')).click()

    @staticmethod
    def search_program():
        with allure.step('Поиск программы'):
            browser.element((AppiumBy.XPATH, '//android.widget.EditText')).click()
            browser.element((AppiumBy.XPATH, '//android.widget.EditText')).type('обследование')

    @staticmethod
    def check_results():
        with ((allure.step('Поиск проверочной строки'))):
            (browser.all((AppiumBy.XPATH, '//android.widget.TextView[@text="Кардиологическое обследование"]'))
             .first.should(have.text("Кардиологическое обследование")))


login_page = LoginPage()
