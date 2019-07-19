from pages.registration_page import RegisterAccountPage, RegistrationSuccessPage
from modules.browser import Driver
from modules.proxy import Field, number
from modules.abstract_factory import full_person


def test_prototype():
    chrome = Driver().connect()
    registration = RegisterAccountPage()
    registration.open()
    person = full_person('Cyrillic').split(",")
    registration.fill_personal_details(
        person[Field.NAME.value],
        person[Field.LAST_NAME.value],
        person[Field.EMAIL.value] + number(),
        person[Field.PHONE.value],
        person[Field.PASSWORD.value],
    )
    registration.press_continue()
    assert RegistrationSuccessPage(chrome).loaded()
