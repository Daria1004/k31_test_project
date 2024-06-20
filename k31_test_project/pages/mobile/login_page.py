import allure
import config
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class LoginPage:

    def skip_health(self):
        # with allure.step("Открытие страницы Личный кабинет"):
        if (config.context == 'bstack'):
            browser.element((AppiumBy.ID, 'com.android.healthconnect.controller:id/go_back_button')).click()
        else:
            browser.element((AppiumBy.ID, 'com.android.healthconnect.controller:id/cancel')).click()

    def open_login(self):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="ВХОД/РЕГИСТРАЦИЯ"]')).click()

    def send_login(self, value):
        browser.element((AppiumBy.XPATH, '//android.widget.EditText')).type(value)
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="ПРОДОЛЖИТЬ"]')).click()

    def send_password(self, value):
        browser.element((AppiumBy.XPATH, '//android.widget.EditText')).type(value)
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="ВОЙТИ"]')).click()

    def skip_allow(self):
        # if (config.context != 'bstack'):
        browser.element((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')).click()

    def send_pin(self):
        for i in range(12):
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="1"]')).click()

    def should_have_username(self, value):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Иванов Петр"]')).should(have.text(value))

    def should_have_login_error(self):
        browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="ВОЙТИ"]')).should(be.visible)

    def should_have_error_text(self, value):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Неверный код"]')).should(have.text(value))

    def logout(self):
        browser.element('.menu__user-logout').click()

    def header_should_have_text(self, text):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Вход в личный кабинет пациента"]')).should(have.text(text))

    def open_menu(self):
        if (config.context == 'bstack'):
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@text=""]')).click()
        else:
            browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="точки меню"]')).click()

    def should_have_title(self, value):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Меню"]')).should(have.text(value))

    def open_program(self):
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Комплексные программы"]')).should(be.visible)
        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Комплексные программы"]')).click()

    def search_program(self):
        browser.element((AppiumBy.XPATH, '//android.widget.EditText')).click()
        browser.element((AppiumBy.XPATH, '//android.widget.EditText')).type('обследование')

    def check_results(self):
        with allure.step('Verify content found'):
            browser.all((AppiumBy.XPATH, '//android.widget.TextView[@text="Кардиологическое обследование"]')).first.should(have.text("Кардиологическое обследование"))

login_page = LoginPage()