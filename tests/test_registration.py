from tests.browser import Driver
from mimesis import Person
from pages.registration_page import RegisterAccountPage, RegistrationSuccessPage


def test_registration() -> None:
    chrome = Driver().connect()
    registration = RegisterAccountPage(chrome)
    registration.open()
    generator = Person()
    registration.fill_personal_details(
        generator.name(), generator.last_name(), generator.email(), generator.telephone()
    )
    registration.fill_password(generator.password())
    registration.press_continue()
    assert RegistrationSuccessPage(chrome).loaded()
