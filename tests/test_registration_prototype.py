from pages.registration_page import RegisterAccountPage, RegistrationSuccessPage
from tests.browser import Driver
from tests.person import Director
from tests.prototype import build_prot
from tests.proxy import Field, number


def test_prototype():
    chrome = Driver().connect()
    director = Director()
    builder = build_prot()
    director.builder = builder
    director.build_registration()
    registration = RegisterAccountPage()
    registration.open()
    person = str(builder.person.list_parts()).split(",")
    registration.fill_personal_details(
        person[Field.NAME.value],
        person[Field.LAST_NAME.value],
        person[Field.EMAIL.value] + number(),
        person[Field.PHONE.value],
        person[Field.PASSWORD.value],
    )
    registration.press_continue()
    assert RegistrationSuccessPage(chrome).loaded()
