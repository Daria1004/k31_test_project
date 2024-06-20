import config

from k31_test_project.pages.web.main_page import main_page
from k31_test_project.pages.web.program_page import program_page


def test_open():
    main_page.open()
    main_page.header_should_have_text('Часть функционала доступна только после входа')


def test_complex_programs():
    program_page.open()
    program_page.search('здоровье')
    program_page.program_list_should_not_be_empty()
    program_page.shold_have_program('Управление здоровьем женщины')


def test_complex_programs_not_found():
    program_page.open()
    program_page.search('samsung')
    program_page.program_list_should_be_empty()


def test_profile_phone_is_valid(logged_in):
    logged_in.open_profile()
    logged_in.profile_should_have_phone(config.user_login)
