import allure
import pytest
from allure_commons.types import Severity

import config

from k31_test_project.pages.web.main_page import main_page
from k31_test_project.pages.web.program_page import program_page


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "Daria Jakuszewicz")
@allure.label("layer", "web")
@pytest.mark.web
@pytest.mark.pages
@pytest.mark.positive
def test_open():
    main_page.open()
    main_page.header_should_have_text('Часть функционала доступна только после входа')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Daria Jakuszewicz")
@allure.label("layer", "web")
@pytest.mark.web
@pytest.mark.pages
@pytest.mark.positive
def test_complex_programs():
    program_page.open()
    program_page.search('здоровье')
    program_page.program_list_should_not_be_empty()
    program_page.shold_have_program('Управление здоровьем женщины')


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Daria Jakuszewicz")
@allure.label("layer", "web")
@pytest.mark.web
@pytest.mark.pages
@pytest.mark.negative
def test_complex_programs_not_found():
    program_page.open()
    program_page.search('samsung')
    program_page.program_list_should_be_empty()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Daria Jakuszewicz")
@allure.label("layer", "web")
@pytest.mark.web
@pytest.mark.pages
@pytest.mark.positive
def test_profile_phone_is_valid(logged_in):
    logged_in.open_profile()
    logged_in.profile_should_have_phone(config.user_login)
